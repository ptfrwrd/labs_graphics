from PIL import Image
import numpy as np
import math


def draw_line(x0, y0, x1, y1, pix):

   step = False

   if math.fabs(x0-x1) < math.fabs(y0-y1):
       x0, y0 = y0, x0
       x1, y1 = y1, x1
       step = True

   if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

   for x in range(x0, x1):
        t = (x - x0) / float(x1 - x0)
        y = y0 * (1 - t) + y1 * t
        if step:
            pix[round(y), round(x)] = (155, 155, 155)
        else:
            pix[round(x), round(y)] = (155, 155, 155)


def braz_line(x0, y0, x1, y1, pix):
    step = False

    if math.fabs(x0 - x1) < math.fabs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        step = True

    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0
    derror = math.fabs(dy) * 2
    error, y = 0, y0
    for x in range(x0, x1):
        if step:
            pix[int(round(y)), int(round(x))] = (155, 155, 155)
        else:
            pix[int(round(x)), int(round(y))] = (155, 155, 155)

        error += derror
        if error > dx:
            y += 1 if y1 > y0 else -1
            error -= 2 * dx


'''x_start, y_start = 0, 0
img = Image.new('RGB', (200, 200))
pix = img.load()
pi = math.pi
for i in range(13):
    x_start = int(100 + math.cos((i*2*pi)/13)*95)
    y_start = int(100 + math.sin((i*2*pi)/13)*95)
    img.putpixel((x_start, y_start), (155, 155, 155))
    draw_line(x_start, y_start, 100, 100, pix)
    braz_line(x_start, y_start, 100, 100, pix)

img.save('вау1.png')
img.show()'''
