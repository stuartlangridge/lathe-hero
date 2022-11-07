#!/usr/bin/env python3

import glob
from PIL import Image
import os
import shutil
import json

try:
    shutil.rmtree("bark-slices-crushed-cropped")
except FileNotFoundError:
    pass
os.mkdir("bark-slices-crushed-cropped")

print("...first calculate the largest bounding box...")
maxh = 0
maxw = 0
for ifn in sorted(glob.glob("bark-slices-crushed/*.png")):
    print(ifn, end="\r")
    fn = os.path.split(ifn)[1]
    val = int(fn.split(".")[0])
    nval = val - 1
    nfn = f"{nval:04d}.png"
    ofn = os.path.join("bark-slices-crushed-cropped", nfn)
    im = Image.open(ifn)
    l, t, r, b = im.getbbox()
    h = b - t
    w = r - l
    if h > maxh: maxh = h
    if w > maxw: maxw = w

# Also fix 1-indexing to be 0-indexing
bboxes = {}
print("\n...now crop and 0-index")
for ifn in sorted(glob.glob("bark-slices-crushed/*.png")):
    print(ifn, end="\r")
    fn = os.path.split(ifn)[1]
    val = int(fn.split(".")[0])
    nval = val - 1
    nfn = f"{nval:04d}.png"
    ofn = os.path.join("bark-slices-crushed-cropped", nfn)
    im = Image.open(ifn)
    bbox = im.getbbox()
    bboxes[nval] = {"t": bbox[1], "l": bbox[0]}
    nim = im.crop(bbox)
    nim = nim.convert("RGBA")
    nnim = Image.new("RGBA", (maxw, maxh))
    x = int((maxw - nim.size[0]) / 2)
    nnim.alpha_composite(nim, (x, 0))
    nnim.save(ofn)

with open("bboxes.json", mode="w") as fp:
    json.dump(bboxes, fp, indent=2)

print("\n...cropped.")
