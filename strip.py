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
bboxes = {}

# Also fix 1-indexing to be 0-indexing

for ifn in sorted(glob.glob("bark-slices-crushed/*.png")):
    print(ifn)
    fn = os.path.split(ifn)[1]
    val = int(fn.split(".")[0])
    nval = val - 1
    nfn = f"{nval:04d}.png"
    ofn = os.path.join("bark-slices-crushed-cropped", nfn)
    im = Image.open(ifn)
    bbox = im.getbbox()
    nim = im.crop(bbox)
    nim.save(ofn)

with open("bboxes.json", mode="w") as fp:
    json.dump(bboxes, fp, indent=2)
