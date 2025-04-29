import numpy as np
import matplotlib.pyplot as plt

def load_xvg(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")):
                data.append([float(x) for x in line.split()])
    return np.array(data)

def plot_running_avg(x, y):
    window_size = 1000
    running_avg = np.convolve(y, np.ones(window_size) / window_size, mode="valid")
    x_avg = x[len(x) - len(running_avg) : ]
    plt.plot(x_avg, running_avg, label="X-ps Running Avg", color="red")

filename = "WT/rmsd_wt_SOLU"
data = load_xvg(f"{filename}.xvg")
x = [time - 10 for time in data[:, 0]]
y = data[:, 1]
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="", color="black")
plot_running_avg(x, y)
plt.xlabel("time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("")
plt.ylim(0, 0.4)
plt.axvline(x=0, color='b', linestyle='--')
#plt.xlim(-180, 180)
#plt.legend()
plt.grid(False)
plt.savefig(f"{filename}.pdf", format="pdf", bbox_inches="tight")
plt.show()