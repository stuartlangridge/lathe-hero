#!/bin/bash

rm -rf bark-slices-crushed-cropped-sheets-crushed
mkdir bark-slices-crushed-cropped-sheets-crushed
for f in bark-slices-crushed-cropped-sheets/*.png; do
    echo $f
    pngquant --output bark-slices-crushed-cropped-sheets-crushed/slice-$(basename $f) $f
done
