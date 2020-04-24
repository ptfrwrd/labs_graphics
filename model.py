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