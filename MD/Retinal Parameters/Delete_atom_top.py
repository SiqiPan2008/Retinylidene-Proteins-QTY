import re

def delete_atom_and_update_indices(file_path, write_path, atom_index):
    with open(file_path, "r") as file:
        lines = file.readlines()

    atom_index = int(atom_index)
    atom_section = 0
    current_section = ""
    sections_to_update = ["[ pairs ]", "[ bonds ]", "[ angles ]", "[ dihedrals ]", "[ cmap ]"]
    section_to_format = {
        "[ pairs ]": "{:>5}{:>6}{:>6}",
        "[ bonds ]": "{:>5}{:>6}{:>6}",
        "[ angles ]": "{:>5}{:>6}{:>6}{:>6}",
        "[ dihedrals ]": "{:>5}{:>6}{:>6}{:>6}{:>6}",
        "[ cmap ]": "{:>5}{:>6}{:>6}{:>6}{:>6}{:>6}"
    }
    updated_lines = []
    atom_indices_to_delete = set()

    for line in lines:
        if line.strip().startswith("[ atoms ]"):
            atom_section = 1
        elif line.strip().startswith("["):
            atom_section = -1

        if atom_section == 0:
            updated_lines.append(line)
            continue
        elif atom_section == 1:
            updated_lines.append(line)
            atom_section = 2
        elif atom_section == 2:
            if line.strip() and not line.strip().startswith(";"):
                parts = line.split()
                if int(parts[0]) == atom_index:
                    atom_indices_to_delete.add(atom_index)
                    continue
                elif int(parts[0]) > atom_index:
                    parts[0] = str(int(parts[0]) - 1)
                formatted_line = "{:>7}{:>11}{:>7}{:>7}{:>7}{:>7}{:>11}{:>11}".format(*parts)
                updated_lines.append(formatted_line + "\n")
            else:
                updated_lines.append(line)
        elif atom_section == -1:
            updated_lines.append(line)
            if any(line.strip().startswith(section) for section in sections_to_update):
                atom_section = -2
                current_section = line.strip()
            else:
                atom_section = -3
        elif atom_section == -2:
            if line.strip() and not line.strip().startswith(";")  and not line.strip().startswith("#"):
                parts = line.split()
                if any(int(index) in atom_indices_to_delete for index in parts[:-1]):
                    continue
                parts = [str(int(index) - 1) if int(index) > atom_index else index for index in parts]
                formatted_line = section_to_format[current_section].format(*parts)
                updated_lines.append(formatted_line + "\n")
            else:
                updated_lines.append(line)
        elif atom_section == -3:
            updated_lines.append(line)

    with open(write_path, "w") as file:
        file.writelines(updated_lines)

file_path = "my_ret.itp"
write_path = "my_ret_new.itp"
target_delete_atoms = [34, 34]
for i in range(len(target_delete_atoms)):
    delete_atom_and_update_indices(file_path, write_path, target_delete_atoms[i])
    if i == 0:
        file_path = write_path
    
# REMEMBER TO FIX CHARGE GROUPS MANUALLY!