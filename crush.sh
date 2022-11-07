#!/bin/bash

rm -rf bark-slices-crushed
mkdir bark-slices-crushed

# slow one-at-a-time crush
#for f in bark-slices/*.png; do
#    echo -ne $f '\r'
#    pngquant --output bark-slices-crushed/$(basename $f) $f
#done

# fast parallel crush
parallel -n 3 pngquant -- \
$(for f in bark-slices/*.png; do
    echo -ne "--output bark-slices-crushed/$(basename $f) $f "
done)

echo ...crushed.
