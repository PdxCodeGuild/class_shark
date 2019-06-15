# from PIL import Image
# img = Image.open('./Images/Lenna_(test_image).png')
# width, height = img.size
# pixels = img.load()
#
# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#
#
#
#         pixels[i, j] = (r, g, b)
#
# img.show()


from PIL import Image
# from random import randrange
img = Image.new('RGB', (50, 50))
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = (int(255*(((i+j)//2)/img.size[0])),
                        int(255*(i/img.size[0])),
                        int(255*(j/img.size[1])))
img.show()
