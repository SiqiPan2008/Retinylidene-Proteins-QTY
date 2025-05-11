import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def load_xvg_ie(filename, byres = False):
    data = [[] for _ in range(15)] if byres else [[]]
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith(("#", "@")) and len(line.split()) > 0:
                split = line.split()
                if byres:
                    for i in range(15):
                        data[i].append(float(split[2 * i + 1]) + float(split[2 * i + 2]))
                else:
                    data[0].append(float(split[1]) + float(split[2]))
    return np.array(data)

matplotlib.rcParams['font.family'] = 'Calibri'
data = []
targetname = "ie"
reslabels = {
    "qty": ["265W", "113E", "181E", "268Y", "207M", "186S", "191Y", "187C", "188G", "189I", "117A", "292A", "212Y", "295A", "208Y"], 
    "wt" : ["265W", "113E", "181E", "268Y", "207M", "186S", "191Y", "187C", "188G", "189I", "117A", "292A", "212F", "295A", "208F"]
}
matplotlib.rcParams['font.family'] = 'Calibri'
targetname = "ie"
resids = [265, 113, 181, 268, 207, 186, 191, 187, 188, 189, 117, 292, 212, 295, 208]
resnames = [int(resid) for resid in resids]
groups = ["prot", "pocket"]
data = {"qty": 0, "wt": 0}
for protein in ["qty", "wt"]:
    data_temp = []
    for group in groups:
        cis_data = load_xvg_ie(f"{protein}_cis_{targetname}_{group}.xvg", byres=False)
        trans_data = load_xvg_ie(f"{protein}_trans_{targetname}_{group}.xvg", byres=False)
        data_temp.append(np.concatenate((cis_data, trans_data), axis=1))
    cis_data = load_xvg_ie(f"{protein}_cis_{targetname}_byres.xvg", byres=True)
    trans_data = load_xvg_ie(f"{protein}_trans_{targetname}_byres.xvg", byres=True)
    data_temp.append(np.concatenate((cis_data, trans_data), axis=1))
    data[protein] = np.concatenate(data_temp, axis=0)
    data[protein] = np.sign(data[protein]) * np.log1p(np.abs(data[protein]))

vmax = max(np.max(np.abs(data["qty"])), np.max(np.abs(data["wt"])))
for protein in ["qty", "wt"]:
    fig, ax = plt.subplots(figsize=(4.5, 4))
    cax = ax.imshow(data[protein], aspect="auto", cmap="RdBu_r", vmin=-vmax, vmax=vmax, origin="lower", interpolation="nearest")
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("")
    ax.set_yticks(range(17))
    ax.set_yticklabels(["Protein", "Pocket"] + reslabels[protein])
    ax.set_ylim(-0.5, 16.5)
    for y in np.arange(0.5, 17, 1):
        ax.axhline(y=y, color="black", linestyle="-", linewidth=1)
    ax.invert_yaxis()
    ax.set_xlim(0, (10 + 120) * 500)
    ax.set_xticks(np.arange(0, (10 + 120) * 500 + 1, 10 * 500))
    ax.set_xticklabels(np.arange(-10, 120 + 1, 10))
    ax.axvline(x=10*500, color='brown', linestyle='--', linewidth=1 )
    plt.savefig(f"{protein}_{targetname}.pdf", format="pdf", bbox_inches="tight")
    fig.colorbar(cax)
    plt.savefig(f"{protein}_{targetname}_colorbar.pdf", format="pdf", bbox_inches="tight")
    plt.show()














