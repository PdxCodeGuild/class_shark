# filename: "my_pillow.py"
from PIL import Image
from random import randrange
img = Image.new('RGB', (4, 4))
pixels = img.load()
for i in range(img.size[0]): # 50
    for j in range(img.size[1]):
        pixels[i, j] = (0, int(255*(i/4)), int(255*(j/4)))
img.show()
