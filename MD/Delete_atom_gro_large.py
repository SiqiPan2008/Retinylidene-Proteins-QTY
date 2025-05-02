import re

def delete_atom_and_update_indices(file_path, write_path, target_delete_atoms):
    with open(file_path, "r") as file:
        lines = file.readlines()
    updated_lines = []
    num_deleted = 0

    in_protein = 0
    for line in lines:
        line_splitted = line.split()
        if len(line_splitted) == 5:
            line_splitted = line_splitted[:1] + [line_splitted[1][:-5], line_splitted[1][-5:]] + line_splitted[2:]
        elif len(line_splitted) != 6:
            updated_lines.append(line)
            continue
        atom_index = int(line_splitted[2])
        if atom_index in target_delete_atoms and num_deleted < len(target_delete_atoms):
            num_deleted += 1
            continue
        new_line_splitted = line_splitted[:2] + [str(atom_index - num_deleted)] + line_splitted[3:]
        formatted_line = ""
        
        # below are specifically for the membrane system sice CHL1, POPC, POPE, POPS are all 4-letter residues
        if "RET" in line_splitted[0]:
            in_protein = 1
        elif in_protein == 1:
            in_protein = -1
            
        if in_protein == -1:
            formatted_line = "{:>9}{:>6}{:>5}{:>8}{:>8}{:>8}\n".format(*new_line_splitted)
        else:
            formatted_line = "{:>8}{:>7}{:>5}{:>8}{:>8}{:>8}\n".format(*new_line_splitted)
        
        updated_lines.append(formatted_line)

    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "step5_input_formatted.gro"
write_path = "step5_input.gro"
target_delete_atoms = [4686, 4687, 5497, 5498]
delete_atom_and_update_indices(file_path, write_path, target_delete_atoms)

# Remember to manually edit the total atom count!

# when there are over 10000 atoms, edit things like:
# 19908TIP3  OH21   -4   9.829   5.121   0.182
# 19908TIP3   H11   -3   9.893   5.189   0.208
# 19908TIP3   H21   -2   9.879   5.079   0.109
# 19909TIP3  OH21   -1   9.664   4.387   0.095
# 19909TIP3   H11    0   9.662   4.483   0.111