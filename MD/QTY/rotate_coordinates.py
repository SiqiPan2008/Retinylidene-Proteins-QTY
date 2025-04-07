from math import *

def rotate_180(point, axis, ref_point):
    point = [point[i] - ref_point[i] for i in range(3)]
    dot_product = sum([point[i]*axis[i] for i in range(3)])
    norm_axis_sq = sum([axis[i]**2 for i in range(3)])
    proj = [dot_product/norm_axis_sq*axis[i] for i in range(3)]
    orth = [point[i] - proj[i] for i in range(3)]
    new_point = [proj[i] - orth[i] for i in range(3)]
    new_point = [new_point[i] + ref_point[i] for i in range(3)]
    return new_point

with open("coordinates_to_rotate.txt", "r") as file:
    lines = file.readlines()

ref_point_0 = [float(lines[0].strip().split()[i]) for i in [2, 3, 4]]
ref_point_1 = [float(lines[1].strip().split()[i]) for i in [2, 3, 4]]
axis = [ref_point_1[i] - ref_point_0[i] for i in [0, 1, 2]]

points_to_rotate = []
for i in range (3, len(lines)):
    points_to_rotate.append(lines[i].strip().split())

points_rotated = []
for point in points_to_rotate:
    point_id = [point[0], point[1]]
    rotated_pos = rotate_180([float(point[i]) for i in [2, 3, 4]], axis, ref_point_1)
    rotated_pos = [str(round(rotated_pos[i], 5)) for i in range(3)]
    rotated_vel = rotate_180([float(point[i]) for i in [5, 6, 7]], axis, [0, 0, 0])
    rotated_vel = [str(round(rotated_vel[i], 5)) for i in range(3)]
    points_rotated.append(point_id + rotated_pos + rotated_vel)

with open("coordinates_rotated.txt", "w") as file:
    lines = file.writelines([" ".join(point) + "\n" for point in points_rotated])