import numpy as np
from PIL import Image
import urllib.request
import os

full_image = Image.open("root/10kpunks.png") #Image file with all 10,000 punk faces.
copy_image = full_image
#Each punk needed to be cropped in 24X24px which provides the right amount of safe spacing.
x1 = 0
y1 = 0
x2 = 24
y2 = 24
increment = 24
for column in range(1, 101):
    for row in range(1, 101):
        cropped = copy_image.crop((x1, y1, x2, y2))
        cropped.save(f"root/PunkHeads/{column}-{row}.png")
        x1 = row * 24
        x2 = x1 + 24
    x1 = 0
    y1 = column * increment
    x2 = 24
    y2 = (column * increment) + 24
