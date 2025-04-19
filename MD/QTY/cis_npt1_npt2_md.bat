gmx grompp -f cis_npt1.mdp -o cis_npt1.tpr -p topol_cis.top -c cis_nvt.gro -r cis_nvt.gro -t cis_nvt.cpt -n index.ndx
gmx mdrun -deffnm cis_npt1 -v
gmx grompp -f cis_npt2.mdp -o cis_npt2.tpr -p topol_cis.top -c cis_npt1.gro -r cis_npt1.gro -t cis_npt1.cpt -n index.ndx
gmx mdrun -deffnm cis_npt2 -v
gmx grompp -f cis_md.mdp -o cis_md.tpr -p topol_cis.top -c cis_npt2.gro -r cis_npt2.gro -t cis_npt2.cpt -n index.ndx
gmx mdrun -deffnm cis_md -v