gmx grompp -f cis_em.mdp  -o cis_em.tpr -p topol_cis.top -c solv_ions.gro -r solv_ions.gro -n index.ndx
gmx mdrun -deffnm cis_em -v
gmx grompp -f cis_nvt.mdp -o cis_nvt.tpr -p topol_cis.top -c cis_em.gro -r cis_em.gro -n index.ndx
gmx mdrun -deffnm cis_nvt -v
gmx grompp -f cis_npt1.mdp -o cis_npt1.tpr -p topol_cis.top -c cis_nvt.gro -r cis_nvt.gro -t cis_nvt.cpt -n index.ndx
gmx mdrun -deffnm cis_npt1 -v
gmx grompp -f cis_npt2.mdp -o cis_npt2.tpr -p topol_cis.top -c cis_npt1.gro -r cis_npt1.gro -t cis_npt1.cpt -n index.ndx
gmx mdrun -deffnm cis_npt2 -v
gmx grompp -f cis_md.mdp -o cis_md.tpr -p topol_cis.top -c cis_npt2.gro -r cis_npt2.gro -t cis_npt2.cpt -n index.ndx
gmx mdrun -deffnm cis_md -v