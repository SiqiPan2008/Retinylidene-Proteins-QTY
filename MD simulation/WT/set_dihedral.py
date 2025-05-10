from math import *

def rotate(point, axis, ref_point, angle):
    rel_point = [point[i] - ref_point[i] for i in range(3)]
    rel_new_point = [0, 0, 0]
    angle_rad = angle *pi / 180
    axis_normalized = [axis[i] / sqrt(sum([axis[j]**2 for j in range(3)])) for i in range(3)]
    dot = sum([rel_point[i] * axis_normalized[i] for i in range(3)])
    cross = [rel_point[(i+1)%3]*axis_normalized[(i+2)%3] - rel_point[(i+2)%3]*axis_normalized[(i+1)%3] for i in range(3)]
    parallel = [axis_normalized[i] * dot for i in range(3)]
    perpendicular = [rel_point[i] - parallel[i] for i in range(3)]
    rotated_perpendicular = [perpendicular[i] * cos(angle_rad) + cross[i] * sin(angle_rad) for i in range(3)]
    rel_new_point = [parallel[i] + rotated_perpendicular[i] for i in range(3)]
    new_point = [rel_new_point[i] + ref_point[i] for i in range(3)]
    return new_point

def measure_dihedral(a, b, c, d):
    ab = [a[i] - b[i] for i in range(3)]
    bc = [b[i] - c[i] for i in range(3)]
    cd = [c[i] - d[i] for i in range(3)]
    ab_cross_bc = [ab[1]*bc[2] - ab[2]*bc[1], ab[2]*bc[0] - ab[0]*bc[2], ab[0]*bc[1] - ab[1]*bc[0]]
    bc_cross_cd = [bc[1]*cd[2] - bc[2]*cd[1], bc[2]*cd[0] - bc[0]*cd[2], bc[0]*cd[1] - bc[1]*cd[0]]
    ab_cross_bc_length = sqrt(sum([x**2 for x in ab_cross_bc]))
    bc_cross_cd_length = sqrt(sum([x**2 for x in bc_cross_cd]))
    cos_angle = sum([ab_cross_bc[i]*bc_cross_cd[i] for i in range(3)]) / (ab_cross_bc_length * bc_cross_cd_length)
    dihedral = acos(cos_angle) * 180 / pi
    return dihedral

with open("coordinates_to_rotate_new.txt", "r") as file:
    lines = file.readlines()

# axis is b-c
# pivot is c
# dihedral is a-b-c-d
# delete the first column of resi/resn in .gro file
a = [float(lines[0].strip().split()[i]) for i in [2, 3, 4]]
b = [float(lines[1].strip().split()[i]) for i in [2, 3, 4]]
c = [float(lines[2].strip().split()[i]) for i in [2, 3, 4]]
d = [float(lines[3].strip().split()[i]) for i in [2, 3, 4]]
axis = [b[i] - c[i] for i in [0, 1, 2]]

points_to_rotate = []
for i in range (5, len(lines)):
    points_to_rotate.append(lines[i].strip().split())

target_dihedral = 180
dihedral = measure_dihedral(a, b, c, d)
#angle = 180
angle = target_dihedral - dihedral

points_rotated = []
for point in points_to_rotate:
    point_id = [point[0], point[1]]
    rotated_pos = rotate([float(point[i]) for i in [2, 3, 4]], axis, c, angle)
    rotated_pos = [f"{rotated_pos[i]:.3f}" for i in range(3)]
    rotated_vel = rotate([float(point[i]) for i in [5, 6, 7]], axis, [0, 0, 0], angle)
    rotated_vel = [f"{rotated_vel[i]:.4f}" for i in range(3)]
    points_rotated.append(point_id + rotated_pos + rotated_vel)

with open("coordinates_rotated_new.txt", "w") as file:
    lines = file.writelines([" ".join(point) + "\n" for point in points_rotated])