# filename: "my_pillow.py"
from PIL import Image
from random import randrange
img = Image.new('RGB', (4, 4))
pixels = img.load()
for i in range(img.size[0]): # 4
    for j in range(img.size[1]): # 4
        pixels[i, j] = (0, int(255*(i/3)), int(255*(j/3)))
img.show()
