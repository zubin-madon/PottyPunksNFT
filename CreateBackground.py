import random
from PIL import Image
import palettes #importing palettes.py to access the RGB list we created.

back = Image.open(r"PATH\Transparent_Backgrnd_Layer.png") #This is a blank transparent rectangle of whatever canvas size you require for your artwork.
j= 0
i= 0
while i < 10001:
    for count in range(len(palettes.RGB_PALETTE)):
        palette_count = 0
        #local_palette = [palettes.RGB_PALETTE[x] for x in range(j, (j+4))]
        width = back.size[0]
        height = back.size[1]
        for a in range(0, width):  # process all pixels
            for b in range(0, height):
                back.putpixel((a, b), palettes.RGB_PALETTE[random.randrange(j, (j+4),1)])
                palette_count+=1
                if palette_count > 3:
                    palette_count=0
        fixed_height = 488
        height_percent = (fixed_height / float(back.size[1]))
        width_size = int((float(back.size[0]) * float(height_percent)))
        back = back.resize((width_size, fixed_height), Image.NEAREST)
        back.save(f'Backgrounds/scrambled-{count}.png')
        #back.show()
        j+=4
