# Annotation

`Books` are grouped into `authors`. All authors are grouped into 25 AH periods, based on the year of their death. These repositories are the main working loci—if any modifications are to be added or made to texts or metadata, all has to be done in files in these folders.

There are three types of text repositories:

- `RAWrabicaXXXXXX` repositories include *raw* texts as they were collected from various open-access online repositories and libraries. These texts are in their initial (*raw*) format and require reformatting and further integration into OpenITI. The overall current number of text files is over 40,000; slightly over 7,000 have been integrated into OpenITI.
- `XXXXAH` are the main working folders that include integrated texts (all coming from collections included into `RAWrabicaXXXXXX` repositories).
- `i.xxxxx` repositories are *instantiations* of the OpenITI corpus adapted for specific forms of analysis. At the moment, these include the following instantiations  (_in progress_):
	- `i.cex` with all texts split mechanically into 300 word units, converted into `cex` format.
	- `i.mech` with all texts split mechanically into 300 word units.
	- `i.logic` with all texts split into logical units (chapters, sections, etc.); only tagged texts are included here (~130 texts at the moment).
	-  `i.passim_new_mech` with all texts split mechanically into 300 word units, converted for the use with new `passim` (JSON).
	- [*not created yet*] `i.passim_new_mech_cluster` with all text split mechanically into 900 word units (3 milestones) with 300 word overlap; converted for the use with new `passim` (JSON).
	- `i.passim_old_mech` with all texts split mechanically into 300 word units, converted for the use with old `passim` (XML, gzipped).
	- `i.stylo` includes all texts from OpenITI (duplicates excluded) that are renamed and slightly reformatted (Arabic orthography is simplified) for the use with `stylo` R-package.
