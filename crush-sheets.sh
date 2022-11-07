#!/bin/bash

rm -rf bark-slices-crushed-cropped-sheets-crushed
mkdir bark-slices-crushed-cropped-sheets-crushed

# slow one-at-a-time crush
#for f in bark-slices-crushed-cropped-sheets/*.png; do
#    echo $f
#    pngquant --output bark-slices-crushed-cropped-sheets-crushed/slice-$(basename $f) $f
#done

#fast parallel crush
parallel -n 3 pngquant -- \
$(for f in bark-slices-crushed-cropped-sheets/*.png; do
    echo -ne "--output bark-slices-crushed-cropped-sheets-crushed/slice-$(basename $f) $f "
done)

echo ...sheet crush done.
