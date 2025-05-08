gmx select -f qty_cis.xtc -s qty_cis.tpr -select "same residue as (resname SOL and within 0.5 of resname RET)" -os qty_cis_numwater.xvg -tu ns
gmx select -f qty_trans.xtc -s qty_trans.tpr -select "same residue as (resname SOL and within 0.5 of resname RET)" -os qty_trans_numwater.xvg -tu ns
gmx select -f wt_cis.xtc -s wt_cis.tpr -select "same residue as (resname SOL and within 0.5 of resname RET)" -os wt_cis_numwater.xvg -tu ns
gmx select -f wt_trans.xtc -s wt_trans.tpr -select "same residue as (resname SOL and within 0.5 of resname RET)" -os wt_trans_numwater.xvg -tu ns