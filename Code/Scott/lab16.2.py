"""
Name:           Scott Tran
Date            6/25/2019
Assignment:     Use the colorsys library to increase the saturation, decrease the brightness, and rotate the hue. 

"""
from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

print(type(pixels))

for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            if h < 0.5 or h > 0.9:
                s = 0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

img.show()