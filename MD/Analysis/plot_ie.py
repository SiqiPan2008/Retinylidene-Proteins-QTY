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
for protein in ["qty", "wt"]:
    data_temp = []
    for group in groups:
        cis_data = load_xvg_ie(f"{protein}_cis_{targetname}_{group}.xvg", byres=False)
        data_temp.append(cis_data)
        #trans_data = load_ie_not_byres(f"{protein}_trans_{targetname}_{group}.xvg")
        #data_temp.append(np.concatenate((cis_data, trans_data), axis=0))
    cis_data = load_xvg_ie(f"{protein}_cis_{targetname}_byres.xvg", byres=True)
    data_temp.append(cis_data)
    #trans_data = load_ie_byres(f"{protein}_trans_{targetname}_{resname}.xvg")
    #data_temp.append(np.concatenate((cis_data, trans_data), axis=0))
    data = np.concatenate(data_temp, axis=0)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    vmax = np.max(np.abs(data))
    cax = ax.imshow(data, aspect="auto", cmap="RdBu_r", vmin=-vmax, vmax=vmax, origin="lower", interpolation="nearest")
    fig.colorbar(cax)
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("")
    ax.set_ylim(-0.5, 16.5)
    for y in np.arange(0.5, 17, 1):
        ax.axhline(y=y, color="black", linestyle="-", linewidth=1)
    ax.invert_yaxis()
    ax.set_xlim(0, (10 + 120) * 500)
    ax.set_xticks(np.arange(0, (10 + 120) * 500 + 1, 10 * 500))
    ax.set_xticklabels(np.arange(-10, 120 + 1, 10))
    ax.axvline(x=10*500, color='b', linestyle='--')
    plt.savefig(f"{protein}_{targetname}.pdf", format="pdf", bbox_inches="tight")
    plt.show()














