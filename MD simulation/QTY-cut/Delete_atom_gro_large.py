import re

def delete_atom_and_update_indices(file_path, write_path, target_delete_atoms, target_delete_residues):
    with open(file_path, "r") as file:
        lines = file.readlines()
    updated_lines = []
    num_deleted = 0
    num_res_deleted = 0
    res_deleted = []
    reached100000 = False

    for line in lines:
        line_splitted = line.split()
        if len(line_splitted) == 5:
            line_splitted = line_splitted[:1] + [line_splitted[1][:-5], line_splitted[1][-5:]] + line_splitted[2:]
        elif len(line_splitted) != 6:
            updated_lines.append(line)
            continue
        atom_index = int(line_splitted[2])
        line_0 = line_splitted[0]
        res_index = int(line_0[:-3])
        res_index -= num_res_deleted
        res_name = line_0[-3:]
        if reached100000:
           atom_index += 100000 
        if atom_index == 99999:
            reached100000 = True
        if atom_index in target_delete_atoms and num_deleted < len(target_delete_atoms):
            num_deleted += 1
            if res_index in target_delete_residues and res_index not in res_deleted:
                num_res_deleted += 1
                res_deleted.append(res_index)
            continue
        new_line_splitted = [str(res_index), res_name, line_splitted[1], str((atom_index - num_deleted) % 100000)] + line_splitted[3:]
        formatted_line = ""
        formatted_line = "{:>5}{:>3}{:>7}{:>5}{:>8}{:>8}{:>8}\n".format(*new_line_splitted)
        updated_lines.append(formatted_line)

    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "trans_em_again.gro"
write_path = "trans_em_again_delwater.gro"
target_delete_atoms = [
    5066,   5067,   5068, 
    7994,   7995,   7996, 
    8051,   8052,   8053, 
    39665,  39666,  39667, 
    62339,  62340,  62341, 
    62549,  62550,  62551, 
    67952,  67953,  67954, 
    78410,  78411,  78412, 
    86198,  86199,  86200, 
    93791,  93792,  93793, 
    94406,  94407,  94408, 
    96140,  96141,  96142, 
    104750, 104751, 104752, 
    109544, 109545, 109546, 
    126104, 126105, 126106
]
target_delete_residues = [
    341,
    1317,
    1336,
    11874,
    19432,
    19502,
    21303,
    24789,
    27385,
    29916,
    30121,
    30699,
    33569,
    35167,
    40687
]
delete_atom_and_update_indices(file_path, write_path, target_delete_atoms, target_delete_residues)

# Remember to manually edit the total atom count!

# when there are over 10000 atoms, edit things like:
# 19908TIP3  OH21   -4   9.829   5.121   0.182
# 19908TIP3   H11   -3   9.893   5.189   0.208
# 19908TIP3   H21   -2   9.879   5.079   0.109
# 19909TIP3  OH21   -1   9.664   4.387   0.095
# 19909TIP3   H11    0   9.662   4.483   0.111