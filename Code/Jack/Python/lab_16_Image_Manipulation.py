from PIL import Image
img = Image.open('./Images/Lenna_(test_image).png')
width, height = img.size
pixels = img.load()


def greyscale(r, g, b):
    y = 0.299*r + 0.587*g + 0.114*b
    r = int(y)
    g = int(y)
    b = int(y)
    return r, g, b


class Cascade(object):
    """docstring for Cascade."""
    o_core_pix = []
    i_core_color = 0


    def __init__(self, o_core_pix):
        self.o_core_pix = o_core_pix
        self.i_core_color = o_core_pix[i, j]

    def col_run(self):
        for r in range(0,101):
            for a in range(0, 6):
                


for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        r, g, b = greyscale(r, g, b)

        cas = Cascade(pixels)

        pixels[i, j] = (r, g, b)

img.show()


# from PIL import Image
# # from random import randrange
# img = Image.new('RGB', (50, 50))
# pixels = img.load()
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         pixels[i, j] = (int(255*(((i+j)//2)/img.size[0])),
#                         int(255*(i/img.size[0])),
#                         int(255*(j/img.size[1])))
# img.show()
