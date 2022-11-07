#!/bin/bash

echo Crush images
bash crush.sh
echo Cropping images
python3 strip.py
echo Combining images into sprite sheets
python3 sheets.py
echo Crushing sprite sheets
bash crush-sheets.sh