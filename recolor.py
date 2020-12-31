#imports libary needed to access photo
from PIL import Image

#Opens and loads the image that it processes
money = Image.open("money.png")
money = money.convert("RGBA")
pixels = money.load()

#Sets two vairables for the loops that go through each pixel
width, height = money.size

#Nested loop for each pixel
for a in range(0,width):
    for b in range(0,height):
        if pixels[a,b][3] == 0:
            pixels[a,b] = (250,50,50,255)
            
#saves the image
money.save("money.png")
