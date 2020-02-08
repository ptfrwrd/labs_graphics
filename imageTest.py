from PIL import Image
import readObect
import model

img = Image.new('RGB', (1000, 1000))
points = readObect.read_object()
for i in range(len(points)):
    points_2D = model.Model.get_2D_index(points, i)
    img.putpixel((int(points_2D[0]*4000)+500, int(points_2D[1]*-4000)+500), (155, 155, 155))
img.save('вау.png')
img.show()


