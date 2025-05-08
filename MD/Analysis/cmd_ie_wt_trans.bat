gmx grompp -f wt_trans_ie_byres.mdp -c wt_trans.gro -t wt_trans.cpt -p wt_trans.top -n wt_trans.ndx -o wt_trans_ie_byres.tpr
gmx mdrun -rerun wt_trans.xtc -deffnm wt_trans_ie_byres -nb cpu
echo 25 26 29 30 33 34 37 38 41 42 45 46 49 50 53 54 57 58 61 62 65 66 69 70 73 74 77 78 81 82 0 | gmx energy -f wt_trans_ie_byres.edr -o wt_trans_ie_byres.xvg

gmx grompp -f wt_trans_ie_pocket.mdp -c wt_trans.gro -t wt_trans.cpt -p wt_trans.top -n wt_trans.ndx -o wt_trans_ie_pocket.tpr
gmx mdrun -rerun wt_trans.xtc -deffnm wt_trans_ie_pocket -nb cpu
echo 21 22 0 | gmx energy -f wt_trans_ie_pocket.edr -o wt_trans_ie_pocket.xvg

gmx grompp -f wt_trans_ie_prot.mdp -c wt_trans.gro -t wt_trans.cpt -p wt_trans.top -n wt_trans.ndx -o wt_trans_ie_prot.tpr
gmx mdrun -rerun wt_trans.xtc -deffnm wt_trans_ie_prot -nb cpu
echo 21 22 0 | gmx energy -f wt_trans_ie_prot.edr -o wt_trans_ie_prot.xvg