gmx grompp -f qty_trans_ie_byres.mdp -c qty_trans.gro -t qty_trans.cpt -p qty_trans.top -n qty_trans.ndx -o qty_trans_ie_byres.tpr
gmx mdrun -rerun qty_trans.xtc -deffnm qty_trans_ie_byres -nb cpu
echo 25 26 29 30 33 34 37 38 41 42 45 46 49 50 53 54 57 58 61 62 65 66 69 70 73 74 77 78 81 82 0 | gmx energy -f qty_trans_ie_byres.edr -o qty_trans_ie_byres.xvg

gmx grompp -f qty_trans_ie_pocket.mdp -c qty_trans.gro -t qty_trans.cpt -p qty_trans.top -n qty_trans.ndx -o qty_trans_ie_pocket.tpr
gmx mdrun -rerun qty_trans.xtc -deffnm qty_trans_ie_pocket -nb cpu
echo 21 22 0 | gmx energy -f qty_trans_ie_pocket.edr -o qty_trans_ie_pocket.xvg

gmx grompp -f qty_trans_ie_prot.mdp -c qty_trans.gro -t qty_trans.cpt -p qty_trans.top -n qty_trans.ndx -o qty_trans_ie_prot.tpr
gmx mdrun -rerun qty_trans.xtc -deffnm qty_trans_ie_prot -nb cpu
echo 21 22 0 | gmx energy -f qty_trans_ie_prot.edr -o qty_trans_ie_prot.xvg