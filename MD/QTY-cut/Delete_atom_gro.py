import re

def delete_atom_and_update_indices(file_path, write_path, target_delete_atoms, target_delete_residues):
    with open(file_path, "r") as file:
        lines = file.readlines()
    updated_lines = []
    num_deleted = 0
    num_res_deleted = 0
    res_deleted = []

    for line in lines:
        line_splitted = line.split()
        if len(line_splitted) != 6:
            updated_lines.append(line)
            continue
        atom_index = int(line_splitted[2])
        line_0 = line_splitted[0]
        res_index = int(line_0[:-3])
        res_index -= num_res_deleted
        res_name = line_0[-3:]
        if atom_index > 62450:
            pass
        if atom_index in target_delete_atoms:
            num_deleted += 1
            if res_index in target_delete_residues and res_index not in res_deleted:
                num_res_deleted += 1
                res_deleted.append(res_index)
            continue
        new_line_splitted = [str(res_index), res_name, line_splitted[1], str(atom_index - num_deleted)] + line_splitted[3:]
        formatted_line = "{:>5}{:>3}{:>7}{:>5}{:>8}{:>8}{:>8}\n".format(*new_line_splitted)
        updated_lines.append(formatted_line)

    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "solv_ions_again.gro"
write_path = "solv_ions_again_new.gro"
target_delete_atoms = [
    62459, 62460, 62461, 
    62501, 62502, 62503, 
    78107, 78108, 78109, 
    78110, 78111, 78112, 
    78116, 78117, 78118, 
    78146, 78147, 78148, 
    78167, 78168, 78169
]
target_delete_residues = [
    19472,
    19486,
    24688,
    24689,
    24691,
    24701,
    24708
]
delete_atom_and_update_indices(file_path, write_path, target_delete_atoms, target_delete_residues)

# Remember to manually edit the total atom count!