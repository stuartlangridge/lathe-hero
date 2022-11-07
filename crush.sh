#!/bin/bash

rm -rf bark-slices-crushed
mkdir bark-slices-crushed
for f in bark-slices/*.png; do
    echo $f
    pngquant --output bark-slices-crushed/$(basename $f) $f
done
