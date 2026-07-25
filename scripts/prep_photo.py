"""
Prepare a portrait photo for clean ASCII conversion:
  1. remove the background (rembg) so the subject is isolated
  2. boost LOCAL contrast (CLAHE) so a flatly-lit face gains highlights and
     shadows - this is what turns a dark blob into a recognizable face
  3. composite the subject onto pure white so the background reads as blank
     (white -> spaces in the ascii ramp)

Output: source-prepped.png (grayscale), consumed by make_ascii_svg.py.
Run once whenever the source photo changes; the ascii SVG itself is static.

    python scripts/prep_photo.py <input.jpg> [output.png]
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import remove

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

# 1. cut out the subject
cut = remove(Image.open(INP).convert("RGBA"))
rgb = np.array(cut.convert("RGB"))
alpha = np.array(cut.split()[-1])                 # 0 = background

# 2. local-contrast the luminance (CLAHE)
gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8))
gray = clahe.apply(gray)

# a touch of global lift so the face sits in the sparse end of the ramp
gray = cv2.convertScaleAbs(gray, alpha=1.05, beta=18)

# 3. paste onto white using the alpha mask (feathered a hair to avoid a halo)
mask = (alpha.astype(np.float32) / 255.0)
mask = cv2.GaussianBlur(mask, (0, 0), 1.0)
out = gray.astype(np.float32) * mask + 255.0 * (1.0 - mask)
out = np.clip(out, 0, 255).astype(np.uint8)

# 4. crop to the subject's bounding box, then pad to the ascii aspect ratio
#    (100 cols x 8px  /  53 rows x 15px  ~=  1.006) so the face fills the frame.
#    HEIGHT_FRAC keeps only the top slice of the subject (head + shoulders);
#    a full-body crop shrinks the face until it stops reading as a face.
HEIGHT_FRAC = float(os.environ.get("HEIGHT_FRAC", "0.47"))

ys, xs = np.where(alpha > 12)
if len(ys):
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    y1 = y0 + int((y1 - y0) * HEIGHT_FRAC)
    out = out[y0:y1 + 1, x0:x1 + 1]
    # re-tighten horizontally against the kept slice only
    sub_alpha = alpha[y0:y1 + 1, x0:x1 + 1]
    sxs = np.where(sub_alpha.max(axis=0) > 12)[0]
    if len(sxs):
        out = out[:, sxs.min():sxs.max() + 1]

h, w = out.shape
target = (100 * 8) / (53 * 15)
if w / h < target:                       # too tall -> pad left/right
    new_w = int(round(h * target))
    pad = (new_w - w) // 2
    out = cv2.copyMakeBorder(out, 0, 0, pad, new_w - w - pad,
                             cv2.BORDER_CONSTANT, value=255)
else:                                    # too wide -> pad top/bottom
    new_h = int(round(w / target))
    pad = (new_h - h) // 2
    out = cv2.copyMakeBorder(out, pad, new_h - h - pad, 0, 0,
                             cv2.BORDER_CONSTANT, value=255)

Image.fromarray(out, mode="L").save(OUT)
print("wrote", OUT, out.shape)
