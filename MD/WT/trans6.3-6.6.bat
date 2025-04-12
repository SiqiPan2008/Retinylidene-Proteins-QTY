gmx grompp -f trans6.3_equilibration.mdp -o trans6.3.tpr -p topol_trans.top -n index.ndx -c trans6.2.gro -r trans6.2.gro -t trans6.2.cpt
gmx mdrun -deffnm trans6.3 -v
gmx grompp -f trans6.4_equilibration.mdp -o trans6.4.tpr -p topol_trans.top -n index.ndx -c trans6.3.gro -r trans6.3.gro -t trans6.3.cpt
gmx mdrun -deffnm trans6.4 -v
gmx grompp -f trans6.5_equilibration.mdp -o trans6.5.tpr -p topol_trans.top -n index.ndx -c trans6.4.gro -r trans6.4.gro -t trans6.4.cpt
gmx mdrun -deffnm trans6.5 -v
gmx grompp -f trans6.6_equilibration.mdp -o trans6.6.tpr -p topol_trans.top -n index.ndx -c trans6.5.gro -r trans6.5.gro -t trans6.5.cpt
gmx mdrun -deffnm trans6.6 -v