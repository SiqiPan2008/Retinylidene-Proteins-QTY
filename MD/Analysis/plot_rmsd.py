import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def load_xvg(filename, start = 0):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")):
                split = line.split()
                data.append([float(split[i]) + start if i == 0 else float(split[i]) for i in range(len(split))])
    return np.array(data)

def plot_running_avg(x, y, c="red", labelname=""):
    window_size = 500
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    plt.plot(x_avg, running_avg, label=labelname, color=c, linewidth=0.75)

matplotlib.rcParams['font.family'] = 'Calibri'
targetname = "rmsd"
subtargetnames = ["solu", "tm6", "pocket", "ret"]
labelnames = ["Protein and retinal", "TM6", "Binding pocket", "Retinal"]
colors = [
    ["#000000", "#000000"],
    ["#000077", "#0000FF"],
    ["#007700", "#00FF00"],
    ["#770000", "#FF0000"]
]
for protein in ["qty", "wt"]:
    plt.figure(figsize=(4, 2.5))
    plt.xlabel("Time (ns)")
    plt.ylabel("RMSD (nm)")
    plt.title("")
    plt.xlim(-10, 120)
    plt.xticks(np.arange(-10, 121, 10))
    plt.axvline(x=0, color='brown', linestyle='--', linewidth=1)
    plt.grid(False)
    for i in range(len(subtargetnames)):
        cis_data = load_xvg(f"{protein}_cis_{targetname}_{subtargetnames[i]}.xvg", -10)
        trans_data = load_xvg(f"{protein}_trans_{targetname}_{subtargetnames[i]}.xvg")
        data = np.concatenate((cis_data, trans_data), axis=0)
        x = data[:, 0]
        y = data[:, 1]
        #plt.plot(x, y, label=subtargetnames[i], color=colors[i][0], linewidth=0.5)
        plot_running_avg(x, y, c=colors[i][1], labelname=labelnames[i])
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=4)
    plt.savefig(f"{protein}_{targetname}.pdf", format="pdf", bbox_inches="tight")
    plt.show()