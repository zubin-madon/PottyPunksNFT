from PIL import Image
import os
skin = Image.open('layers/ALL_LAYERS_0016_BODY-COLOUR.png')
shirt_outline = Image.open('layers/Shirt_border_with_collar_0009_tee-border.png')
pant_outline = Image.open('layers/ALL_LAYERS_0014_pant-border.png')
potty_outline = Image.open('layers/ALL_LAYERS_0005_potty-border.png')

width, height = skin.size

for i in range(1, 101):
    for j in range(1, 101):
        filename = f'PunkHeads/{i}-{j}.png'
        punk = Image.open(filename)
        ''' This x,y coordinate (139, 226) taken at the neck of the punk, is chosen in such a way that all punk heads have their neck skin exposed at this coorinate.
        Punk heads and necks are of varying size and thickness, so I chose a coordinate where all 10k punks have their skin, without any obstruction from
        accessories or beards.
        '''
        punk_color = punk.getpixel((139, 226)) 
        for x in range(width):
            for y in range(height):
                current_color = skin.getpixel((x, y))
                a = current_color[-1]
                if a > 100:
                    skin.putpixel((x, y), punk_color) #change colour of body skin layer to match that of punk's face skin.
        foreground = punk
        background = skin
        foreground.convert('RGBA')
        background.convert('RGBA')
        shirt_outline.convert('RGBA')
        pant_outline.convert('RGBA')
        potty_outline.convert('RGBA')
        head_skin = Image.alpha_composite(background, foreground)
        head_skin_with_shirt = Image.alpha_composite(head_skin, shirt_outline)
        head_skin_shirt_pant = Image.alpha_composite(head_skin_with_shirt, pant_outline)
        punk_clothes_potty_outline = Image.alpha_composite(head_skin_shirt_pant, potty_outline)
        punk_clothes_potty_outline.save(f'layers/Punk_outlines/punk{i}-{j}.png')
