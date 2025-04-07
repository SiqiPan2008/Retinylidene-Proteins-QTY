with open("step5_input_shifted.txt", "r") as file:
    lines = file.readlines()
    
widths = [5, 4, 6, 5, 8, 8, 8]
new_lines = []
for line in lines:
    parts = line.split()
    new_parts = []
    for i in range(len(widths)):
        if i == 1:
            new_parts.append(parts[i].ljust(widths[i], " "))
        else:
            new_parts.append(parts[i].rjust(widths[i], " "))
    new_line = "".join(new_parts)
    new_lines.append(new_line + "\n")

with open("step5_input_formatted.txt", "w") as file:
    file.writelines(new_lines)