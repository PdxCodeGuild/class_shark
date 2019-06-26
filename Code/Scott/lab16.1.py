"""
Name:           Scott Tran
Date            6/25/2019
Assignment:     Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.

"""

from PIL import Image

# https://www.codementor.io/isaib.cicourel/image-manipulation-in-python-du1089j1u

# # Open an Image
# def open_image(path):
#   newImage = Image.open(path)
#   return newImage

# # Save Image
# def save_image(image, path):
#   image.save(path, 'png')

# # Create a new image with the given size
# def create_image(i, j):
#   image = Image.new("RGB", (i, j), "white")
#   return image

# # Get the pixel from the given image
# def get_pixel(image, i, j):
#     # Inside image bounds?
#     width, height = image.size
#     if i > width or j > height:
#       return None

#     # Get Pixel
#     pixel = image.getpixel((i, j))
#     return pixel



# # The best choice for grayscale is the ITU-R Recommendation BT.601-7, which specifies methods for digitally coding video signals by normalizing the values.
# Y = 0.299*R + 0.587*G + 0.114*B


img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b

        pixels[i, j] = (int(y), int(y), int(y))

img.show()