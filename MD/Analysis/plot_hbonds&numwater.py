import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def load_xvg_numwater(filename, start = 0):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")) and len(line.split()) > 0:
                split = line.split()
                data.append([float(split[i]) + start if i == 0 else int(float(split[i]) / 3) for i in range(len(split))])
    return np.array(data)

def load_xvg(filename, start = 0):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")):
                split = line.split()
                data.append([float(split[i]) + start if i == 0 else float(split[i]) for i in range(len(split))])
    return np.array(data)

def compute_running_avg(x, y):
    window_size = 500
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    return x_avg, running_avg

matplotlib.rcParams["font.family"] = "Calibri"

for protein in ["qty", "wt"]:
    target_water = "numwater"
    cis_water = load_xvg_numwater(f"{protein}_cis_{target_water}.xvg", -10)
    trans_water = load_xvg_numwater(f"{protein}_trans_{target_water}.xvg")
    water_data = np.concatenate((cis_water, trans_water), axis=0)
    x_water = water_data[:, 0]
    y_water = water_data[:, 1]
    x_water_avg, y_water_avg = compute_running_avg(x_water, y_water)

    target_hbond = "hbonds"
    cis_hbond = load_xvg(f"{protein}_cis_{target_hbond}.xvg", -10)
    trans_hbond = load_xvg(f"{protein}_trans_{target_hbond}.xvg")
    hbond_data = np.concatenate((cis_hbond, trans_hbond), axis=0)
    x_hbond = hbond_data[:, 0]
    y_hbond = hbond_data[:, 1]
    x_hbond_avg, y_hbond_avg = compute_running_avg(x_hbond, y_hbond)

    fig, ax1 = plt.subplots(figsize=(4, 2.5))
    ax2 = ax1.twinx()

    ax1.plot(x_hbond_avg, y_hbond_avg, color="blue", label="Number of hydrogen bonds (1ns running avg.)", linewidth=0.75)
    ax1.set_ylabel("Number of hydrogen bonds", color="blue")
    ax1.tick_params(axis="y", labelcolor="black")
    ax1.set_ylim((0, 9))

    ax2.plot(x_water_avg, y_water_avg, color="red", label="Number of water molecules (1ns running avg.)", linewidth=0.75)
    ax2.set_ylabel("Number of water molecules", color="red", rotation=-90, labelpad=12)
    ax2.tick_params(axis="y", labelcolor="black")
    ax2.set_ylim((0, 25))

    ax1.set_xlabel("Time (ns)")
    ax1.set_xlim(-10, 120)
    ax1.set_xticks(np.arange(-10, 121, 10))
    ax1.axvline(x=0, color="brown", linestyle="--", linewidth=1)

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    plt.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper center", bbox_to_anchor=(0.5, -0.3), ncol=2)

    plt.savefig(f"{protein}_hbonds&numwater.pdf", format="pdf", bbox_inches="tight")
    plt.show()