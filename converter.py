# converter.py

"""
Uses luma function from luma.py to calculate pixel luminence values and orders them
"""

from PIL import Image
from luma import luma4

image = Image.open('galaxy.jpg')

max_luma = (0, 0, 0, 0)
for y in range(image.height):
    for x in range(image.width):
        r, g, b = image.getpixel((x, y))
        l = luma4(r, g, b)
        if l > max_luma[0]:
            max_luma = (l, r, g, b)
print(max_luma)

