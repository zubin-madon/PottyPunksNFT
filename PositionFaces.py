#Need to create 10k individual layers with face positioned on the Canvas exactly as it would be in the final artwork.
from PIL import Image
directory = 'C:/Users/Zubin/PycharmProjects/Pottypunks/PunkHeads'

for i in range(1, 101):
    for j in range(1, 101):
        filename = f'PunkHeads/{i}-{j}.png'
        foreground = Image.open(filename)
        back_transparent = Image.open(r"PATH\Transparent_Backgrnd_Layer.png") #This is a transparent canvas of the size required in the final artwork.
        back_transparent.paste(foreground, (25, 33), foreground) #The head needs to be positioned 25px on the x-axis and 33px on y-axis (top left corner of canvas is 0,0).
        back_transparent.save(f'PunkHeads/{i}-{j}.png')
