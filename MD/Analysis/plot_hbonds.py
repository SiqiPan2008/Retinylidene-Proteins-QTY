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

def plot_running_avg(x, y):
    window_size = 500
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    plt.plot(x_avg, running_avg, label="1-ns Running Avg", color="red")

matplotlib.rcParams['font.family'] = 'Calibri'
targetname = "hbonds"
for protein in ["qty", "wt"]:
    cis_data = load_xvg(f"{protein}_cis_{targetname}.xvg", -10)
    trans_data = load_xvg(f"{protein}_trans_{targetname}.xvg")
    data = np.concatenate((cis_data, trans_data), axis=0)
    x = data[:, 0]
    y = data[:, 1]
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="", color="black", linewidth=0.5)
    plot_running_avg(x, y)
    plt.xlabel("Time (ns)")
    plt.ylabel("Number of hydrogen bonds within binding pocket")
    plt.title("")
    plt.xlim(-10, 120)
    plt.xticks(np.arange(-10, 121, 10))
    plt.axvline(x=0, color='b', linestyle='--')
    #plt.legend()
    plt.grid(False)
    plt.savefig(f"{protein}_{targetname}.pdf", format="pdf", bbox_inches="tight")
    plt.show()