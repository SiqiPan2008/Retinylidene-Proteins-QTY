echo 0 | gmx rmsf -s qty_cis_solu.gro -f qty_cis_solu.xtc -o qty_cis_rmsf.xvg -res -n qty_solu.ndx
echo 0 | gmx rmsf -s qty_trans_solu.gro -f qty_trans_solu.xtc -o qty_trans_rmsf.xvg -res -n qty_solu.ndx
echo 32 | gmx rmsf -s wt_cis_solu.gro -f wt_cis_solu.xtc -o wt_cis_rmsf.xvg -res -n wt_solu.ndx
echo 32 | gmx rmsf -s wt_trans_solu.gro -f wt_trans_solu.xtc -o wt_trans_rmsf.xvg -res -n wt_solu.ndx