#!/usr/bin/env python3

from PIL import Image
import shutil
import os

try:
    shutil.rmtree("bark-slices-crushed-cropped-sheets")
except FileNotFoundError:
    pass
os.mkdir("bark-slices-crushed-cropped-sheets")

FRAMES_PER_SLICE = 8
SLICES = 60
TOTAL_FRAMES_BARK = FRAMES_PER_SLICE * SLICES

for slice in range(SLICES):
    y = 0
    sheet = None
    for xi in range(FRAMES_PER_SLICE):
        fn = slice * FRAMES_PER_SLICE + xi
        try:
            ifn = f"bark-slices-crushed-cropped/{fn:04d}.png"
            im = Image.open(ifn)
            im = im.convert("RGBA")
            if sheet is None:
                sheet = Image.new("RGBA", (8 * im.size[0], 2*im.size[1]))
            pos = (xi * im.size[0], y)
            sheet.alpha_composite(im, pos)
            print(f"{ifn} @ {pos}")
            yadd = im.size[1]
        except FileNotFoundError:
            print("failed", ifn)

    for xi in range(FRAMES_PER_SLICE):
        flip_slice = SLICES - 1 - slice
        yfn = flip_slice * FRAMES_PER_SLICE + xi + TOTAL_FRAMES_BARK
        try:
            ifn = f"bark-slices-crushed-cropped/{yfn:04d}.png"
            im = Image.open(ifn)
            im = im.convert("RGBA")
            pos = (xi * im.size[0], yadd)
            sheet.alpha_composite(im, pos)
            print(f"{ifn} @ {pos}")
        except FileNotFoundError:
            print("failed", ifn)
    sheet.save(f"bark-slices-crushed-cropped-sheets/{slice:04d}.png")
