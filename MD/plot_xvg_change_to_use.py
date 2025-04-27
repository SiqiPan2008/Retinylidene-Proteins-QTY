import numpy as np
import matplotlib.pyplot as plt

def load_xvg(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")):
                data.append([float(x) for x in line.split()])
    return np.array(data)

def plot_running_avg(data):
    window_size = 10
    x = data[:, 0]
    y = data[:, 1]
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    plt.plot(x_avg, running_avg, label="10-ps Running Avg", color="red")

filename = "QTY/rmsd_transprot"
data = load_xvg(f"{filename}.xvg")
plt.figure(figsize=(8, 5))
plt.plot(data[:, 0], data[:, 1], label="", color="black")
#plot_running_avg(data)
plt.xlabel("time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("")
#plt.xlim(-180, 180)
#plt.legend()
plt.grid(False)
plt.savefig(f"{filename}.pdf", format="pdf", bbox_inches="tight")
plt.show()