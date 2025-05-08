echo 0 | gmx gyrate -s qty_cis_solu.gro -f qty_cis_solu.xtc -o qty_cis_gyrate.xvg -n qty_solu.ndx -tu ns
echo 0 | gmx gyrate -s qty_trans_solu.gro -f qty_trans_solu.xtc -o qty_trans_gyrate.xvg -n qty_solu.ndx -tu ns
echo 32 | gmx gyrate -s wt_cis_solu.gro -f wt_cis_solu.xtc -o wt_cis_gyrate.xvg -n wt_solu.ndx -tu ns
echo 32 | gmx gyrate -s wt_trans_solu.gro -f wt_trans_solu.xtc -o wt_trans_gyrate.xvg -n wt_solu.ndx -tu ns