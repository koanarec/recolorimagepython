#imports libary needed to access photo
from PIL import Image

#Opens and loads the image that it processes
money = Image.open("money.png")
pixels = money.load()

#Sets two vairables for the loops that go through each pixel
width, height = money.size

#Nested loop for each pixel
for a in range(0,width):
    for b in range(0,height):
        #Checks if the pixel is dark
        if pixels[a,b][0]  not in  range(200,256):
            #if the pixel is dark then it makes it black
            pixels[a,b] = (0,0,0)
        else:
            pixels[a,b] = (255,255,255)
            
#saves the image
money.save("money.png")
