gmx grompp -f step6.5_equilibration.mdp -c step6.4.gro -r step6.4.gro -t step6.4.cpt -n index.ndx -o step6.5.tpr
gmx mdrun -deffnm step6.5 -v
gmx grompp -f step6.6_equilibration.mdp -c step6.5.gro -r step6.5.gro -t step6.5.cpt -n index.ndx -o step6.6.tpr
gmx mdrun -deffnm step6.6 -v
gmx grompp -f step7_production.mdp -c step6.6.gro -r step6.6.gro -t step6.6.cpt -n index.ndx -o step7.tpr
gmx mdrun -deffnm step7 -v