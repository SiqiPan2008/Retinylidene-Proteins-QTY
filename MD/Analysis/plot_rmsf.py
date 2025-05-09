import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def load_xvg_rmsf(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")) and len(line.split()) > 0 \
                and int(line.split()[0]) < 323:
                data.append([int(line.split()[i]) if i == 0 else float(line.split()[i]) for i in range(2)])
    return np.array(data)

matplotlib.rcParams["font.family"] = "Calibri"
targetname = "rmsf"
for protein in ["qty", "wt"]:
    data_cis = load_xvg_rmsf(f"{protein}_cis_{targetname}.xvg")
    data_trans = load_xvg_rmsf(f"{protein}_trans_{targetname}.xvg")
    fig, ax = plt.subplots(figsize=(8, 4))
    bar_width = 1.0
    x = data_cis[:, 0]
    y_cis=data_cis[:, 1]
    y_trans=data_trans[:, 1]
    for i in range(len(x)):
        if y_cis[i] >= y_trans[i]:
            ax.bar(x[i], y_cis[i], color="#0000FF", width=bar_width, alpha=0.8, align="edge")
            ax.bar(x[i], y_trans[i], color="#CCCC00", width=bar_width, alpha=0.8, align="edge")
            
        else:
            ax.bar(x[i], y_trans[i], color="#CCCC00", width=bar_width, alpha=0.8, align="edge")
            ax.bar(x[i], y_cis[i], color="#0000FF", width=bar_width, alpha=0.8, align="edge")
    ax.set_xticks([0.5] + [x[i] + 0.5 for i in range(14, 323, 15)])
    ax.set_xticklabels([1] + [int(x[i]) for i in range(14, 323, 15)])
    ax.set_xlim(0.5, 323.5)
    ax.set_xlabel("Residue Number")
    ax.set_ylabel("RMS Fluctuation (nm)")
    ax.set_ylim(0, 0.75)
    #ax.legend()
    plt.savefig(f"{protein}_{targetname}.pdf", format="pdf", bbox_inches="tight")
    plt.show()