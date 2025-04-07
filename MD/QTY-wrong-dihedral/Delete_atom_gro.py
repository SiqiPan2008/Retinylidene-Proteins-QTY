import re

def delete_atom_and_update_indices(file_path, write_path, target_delete_atoms):
    with open(file_path, "r") as file:
        lines = file.readlines()
    updated_lines = []
    num_deleted = 0

    for line in lines:
        line_splitted = line.split()
        if len(line_splitted) != 6:
            updated_lines.append(line)
            continue
        atom_index = int(line_splitted[2])
        if atom_index in target_delete_atoms:
            num_deleted += 1
            continue
        new_line_splitted = line_splitted[:2] + [str(atom_index - num_deleted)] + line_splitted[3:]
        formatted_line = "{:>8}{:>7}{:>5}{:>8}{:>8}{:>8}\n".format(*new_line_splitted)
        updated_lines.append(formatted_line)

    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "complex.gro"
write_path = "complex_new.gro"
target_delete_atoms = [4547, 4548, 5342, 5343]
delete_atom_and_update_indices(file_path, write_path, target_delete_atoms)

# Remember to manually edit the total atom count!