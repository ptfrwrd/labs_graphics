import math
import lineImage
import numpy as np
from PIL import Image

def bar_coord (x, y, x0,y0,x1,y1,x2,y2):
    bool = True

    l0 = ((y-y2)*(x1-x2)-(x-x2)*(y1-y2))/((y0-y2)*(x1-x2)-(x0-x2)*(y1-y2))
    l1 = ((y - y0) * (x2 - x0) - (x - x0) * (y2 - y0)) / ((y1 - y0) * (x2 - x0) - (x1 - x0) * (y2 - y0))
    l2 = ((y - y1) * (x0 - x1) - (x - x1) * (y0 - y1)) / ((y2 - y1) * (x0 - x1) - (x2 - x1) * (y0 - y1))


    if (l0 < 0) or (l1 < 0) or (l2 < 0):
        bool = False
    return bool

def triangle (x0,y0,x1,y1,x2,y2,pix, color):
    x = [x0,x1,x2]
    y = [y0,y1,y2]
    for i in range(int(round(min(x))), int(round(max(x)))+1):
        for j in range(int(round(min(y))), int(round(max(y)))+1):
            if bar_coord(i, j, x0,y0,x1,y1,x2,y2):
                pix[i, j] = color

if __name__ == '__main__':
    img = triangle(10,50,50,50,30,30)

