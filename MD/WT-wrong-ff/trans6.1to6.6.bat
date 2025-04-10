gmx grompp -f step6.1_equilibration.mdp -c trans6.0.gro -r trans6.0.gro -n index.ndx -o trans6.1.tpr
gmx mdrun -deffnm trans6.1 -v
gmx grompp -f step6.2_equilibration.mdp -c trans6.1.gro -r trans6.1.gro -t trans6.1.cpt -n index.ndx -o trans6.2.tpr
gmx mdrun -deffnm trans6.2 -v
gmx grompp -f step6.3_equilibration.mdp -c trans6.2.gro -r trans6.2.gro -t trans6.2.cpt -n index.ndx -o trans6.3.tpr
gmx mdrun -deffnm trans6.3 -v
gmx grompp -f step6.4_equilibration.mdp -c trans6.3.gro -r trans6.3.gro -t trans6.3.cpt -n index.ndx -o trans6.4.tpr
gmx mdrun -deffnm trans6.4 -v
gmx grompp -f step6.5_equilibration.mdp -c trans6.4.gro -r trans6.4.gro -t trans6.4.cpt -n index.ndx -o trans6.5.tpr
gmx mdrun -deffnm trans6.5 -v
gmx grompp -f step6.6_equilibration.mdp -c trans6.5.gro -r trans6.5.gro -t trans6.5.cpt -n index.ndx -o trans6.6.tpr
gmx mdrun -deffnm trans6.6 -v