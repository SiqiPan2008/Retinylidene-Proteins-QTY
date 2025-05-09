gmx grompp -f qty_cis_ie_pocket.mdp -c qty_cis.gro -t qty_cis.cpt -p qty_cis.top -n qty_cis.ndx -o qty_cis_ie_pocket.tpr
gmx mdrun -rerun qty_cis.xtc -deffnm qty_cis_ie_pocket -nb cpu
echo 21 22 0 | gmx energy -f qty_cis_ie_pocket.edr -o qty_cis_ie_pocket.xvg

gmx grompp -f qty_cis_ie_prot.mdp -c qty_cis.gro -t qty_cis.cpt -p qty_cis.top -n qty_cis.ndx -o qty_cis_ie_prot.tpr
gmx mdrun -rerun qty_cis.xtc -deffnm qty_cis_ie_prot -nb cpu
echo 21 22 0 | gmx energy -f qty_cis_ie_prot.edr -o qty_cis_ie_prot.xvg