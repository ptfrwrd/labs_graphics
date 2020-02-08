from PIL import Image
import math
import numpy as np

def draw_line(x0, y0, x1, y1, img):
    for t in map(lambda temp: temp/0.01, range(0, 1)):
        x = x0 * (1 - t)+x1*t
        y = y0 * (1 - t) + y1 * t
        img.putpixel((int(x), int(y)), (155, 155, 155))


x_start, y_start = 0, 0
img = Image.new('RGB', (200, 200))
pi = math.pi
for i in range(13):
    x_start = int(100 + math.cos((i+2*pi)/13*95))
    y_start = int(100 + math.cos((i+2*pi)/13*95))
    img.putpixel((x_start, y_start), (155, 155, 155))


draw_line(x_start, y_start, 160, 160, img)

img.save('вау.png')
img.show()
