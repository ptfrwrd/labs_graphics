import numpy as np

class Model:
    #point_count = ''
    #mass_points = []

    def set_array(point_count, mass_point):
        points_array = np.ndarray((point_count, 3), buffer=mass_point, dtype=np.float32)
        return points_array

    def get_3D_by_index(points_array, index):
        return points_array[index]

    def get_2D_index(points_array, index):
        return points_array[index][:2]



#count = 3
#mass = np.array([[1,2,3],[2,3,4],[5,6,7]])
#coordinat = Model.set_array(count,mass)
#el = Model.get_3D_by_index(coordinat,2)
#el2 = Model.get_2D_index(coordinat, 1)
#print(coordinat, '\n', el, '\n', '\n', el2)