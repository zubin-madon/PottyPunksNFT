#Match socks to pant colour.
import numpy as np
from PIL import Image
import urllib.request
import os

directory = 'layers/layers_for_art_engine/Pant'
for filename in os.listdir(directory):
    image = os.path.join(directory, filename)
    pant = Image.open(image)
    socks = Image.open('layers/socks.png') #change the file path with your own of course!
    width, height = socks.size
    pant_color = pant.getpixel((200, 350))
    for x in range(width):
        for y in range(height):
            current_color = socks.getpixel((x, y))
            r = pant_color[0]
            g = pant_color[1]
            b = pant_color[2]
            a = current_color[-1]
            if current_color != (255, 255, 255, 0):
                socks.putpixel((x, y), (r, g, b, a))
    pant.paste(socks, (0, 0), socks) #combine the new coloured socks with the pant layer.
    pant.save(image)
