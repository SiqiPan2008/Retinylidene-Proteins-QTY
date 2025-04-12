gmx grompp -f step6.3_equilibration.mdp -o cis6.3.tpr -p topol_cis.top -n index.ndx -c cis6.2.gro -r cis6.2.gro -t cis6.2.cpt
gmx mdrun -deffnm cis6.3 -v
gmx grompp -f step6.4_equilibration.mdp -o cis6.4.tpr -p topol_cis.top -n index.ndx -c cis6.3.gro -r cis6.3.gro -t cis6.3.cpt
gmx mdrun -deffnm cis6.4 -v
gmx grompp -f step6.5_equilibration.mdp -o cis6.5.tpr -p topol_cis.top -n index.ndx -c cis6.4.gro -r cis6.4.gro -t cis6.4.cpt
gmx mdrun -deffnm cis6.5 -v
gmx grompp -f step6.6_equilibration.mdp -o cis6.6.tpr -p topol_cis.top -n index.ndx -c cis6.5.gro -r cis6.5.gro -t cis6.5.cpt
gmx mdrun -deffnm cis6.6 -v