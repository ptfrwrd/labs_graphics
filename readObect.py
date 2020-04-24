import numpy as np
import model

def read_object():
    with open('file.obj', encoding='utf-8') as file:
        all_points = np.empty((0, 3), dtype=np.float32)
        f_polig = np.empty((0, 3, 3), dtype=np.int)
        for line in file:
            line = line.rstrip('\n')
            str = line.split()
            count = 0
            if len(str) == 0:
                continue
            if str[0] == 'v':
                ++count
                points_line = np.array(([[float(str[1]), float(str[2]), float(str[3])]]))
                all_points = np.append(all_points, points_line, axis = 0)
            if str[0] == 'f':
                ++count
                first = str[1].split('/')
                second = str[2].split('/')
                third = str[3].split('/')
                p1 = np.array([int(first[0]),int(first[1]), int(first[2])])
                p2 = np.array([int(second[0]), int(second[1]), int(second[2])])
                p3 = np.array([int(third[0]), int(third[1]), int(third[2])])
                points_line = np.array([[p1, p2, p3]])
                f_polig = np.append(f_polig, points_line, axis=0)
    return all_points, f_polig

