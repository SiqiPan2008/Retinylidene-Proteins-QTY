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

def plot_running_avg(x, y, c="red", labelname="", window=1):
    window_size = window * 500
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    plt.plot(x_avg, running_avg, label=labelname, color=c, linewidth=0.75)

matplotlib.rcParams['font.family'] = 'Calibri'
targetname = "rmsd"
subtargetids = [296, 265, 113, 181, 268, 207, 186, 191, 187, 188, 189, 117, 292, 212, 295, 208]
reslabels = {
    "qty": ["296K", "265W", "113E", "181E", "268Y", "207M", "186S", "191Y", "187C", "188G", "189I", "117A", "292A", "212Y", "295A", "208Y"], 
    "wt" : ["296K", "265W", "113E", "181E", "268Y", "207M", "186S", "191Y", "187C", "188G", "189I", "117A", "292A", "212F", "295A", "208F"]
}
subtargetnames = [int(subtargetid) for subtargetid in subtargetids]
cmap = plt.cm.get_cmap("tab20", 16)
colors = [cmap(i) for i in range(16)]
for protein in ["qty", "wt"]:
    plt.figure(figsize=(8, 4))
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
        plot_running_avg(x, y, c=colors[i], labelname=reslabels[protein][i], window=2)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=8)
    plt.savefig(f"{protein}_{targetname}_byres.pdf", format="pdf", bbox_inches="tight")
    plt.show()