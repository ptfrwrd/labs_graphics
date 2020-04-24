from PIL import Image
import readObect
import model
import lineImage
import triangle
import random

img = Image.new('RGB', (1000, 1000))
pix = img.load()
points, polys = readObect.read_object()

for i in range(len(polys)):
    x0 = 7000 * points[polys[i][0][0]-1][0] + 500
    y0 = -7000 * points[polys[i][0][0]-1][1] + 900
    x1 = 7000 * points[polys[i][1][0]-1][0] + 500
    y1 = -7000 * points[polys[i][1][0]-1][1] + 900
    x2 = 7000 * points[polys[i][2][0] - 1][0] + 500
    y2 = -7000 * points[polys[i][2][0] - 1][1] + 900

    triangle.triangle(x0,y0,x1,y1,x2,y2, pix, (random.randrange(256),random.randrange(256),random.randrange(256)))
   # lineImage.braz_line(int(x0), int(y0), int(x1), int(y1), pix)
   # lineImage.braz_line(int(x0), int(y0), int(x2), int(y2), pix)
   # lineImage.braz_line(int(x1), int(y1), int(x2), int(y2), pix)

img.save('new.png')
img.show()


