import re

def delete_atom_and_update_indices(file_path, write_path, target_delete_atoms):
    with open(file_path, "r") as file:
        lines = file.readlines()
    updated_lines = []

    section = []
    for line in lines:
        if "[" in line:
            updated_line = ""
            count = 0
            for index in section:
                if count == 15:
                    updated_lines.append(updated_line + "\n")
                    count = 0
                    updated_line = ""
                updated_line += index + " "
            updated_lines.append(line)
            section = []
            continue
        line_splitted = line.split()
        for index in line_splitted:
            if int(index) not in target_delete_atoms:
                section.append(index)
    count = 0
    for index in section:
        if count == 15:
            updated_lines.append(updated_line + "\n")
            count = 0
            updated_line = ""
        updated_line += index + " "
        updated_lines.append(line)
    
    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "index.ndx"
write_path = "index_new.ndx"
target_delete_atoms = [i for i in range(4966, 5303)]
delete_atom_and_update_indices(file_path, write_path, target_delete_atoms)