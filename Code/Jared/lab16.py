from PIL import Image

img = Image.open("lenna_(test_image).png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        r, g, b = y
        y = 0.299 *r + 0.587*g+ 0.114*b
        r, g, b = y
        pixels[i, j] = (r, g, b)
img.show()
