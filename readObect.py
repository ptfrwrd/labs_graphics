import numpy as np
import model

def read_object():
    with open('file.obj', encoding='utf-8') as file:
        all_points = np.empty((0, 3), dtype=np.float32)
        for line in file:
            line = line.rstrip('\n')
            str = file.readline().split()
            count = 0
            if len(str) == 0:
                continue
            if str[0] == 'v':
                ++count
                points_line = np.array(([[float(str[1]), float(str[2]), float(str[3])]]))
                all_points = np.append(all_points, points_line, axis = 0)
    return all_points

