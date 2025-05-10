The commands for analysis of molecular dynamics (MD) results are included in this folder. We also included the **.mdp** files for the extraction of interaction energy. This is a table of abbreviations used in the file names: 

| Abbreviation | Full name                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| cmd          | Commands run in Windows Command Prompt (with the exception of cmd_hbond, which was run in Git Bash). |
| WT           | The native OPN2.                                                                                     |
| QTY          | The QTY analog of OPN2.                                                                              |
| cis          | The state of the protein when retinal is in the 11-cis state.                                        |
| trans        | The state of the protein when retinal is in the all-trans state.                                     |
| gyrate       | Calculate the radius of gyration.                                                                    |
| hbond        | Count the number of hydrogen bonds formed between residues in the binding pocket.                    |
| ie           | Calculate the interaction energy.                                                                    |
| numwater     | Count the number of water molecules within the binding pocket.                                       |
| rmsd         | Calculate the root mean square distance.                                                             |
| rmsf         | Calculate the root mean square fluctuation.                                                          |
| byres        | Calculate the interaction energy with retinal residue-by-residue in the binding pocket.              |
| pocket       | Calculate the interaction energy with retinal, regarding the binding pocket as a whole.              |
| prot         | Calculate the interaction energy with retinal, regarding the protein as a whole.                     |
