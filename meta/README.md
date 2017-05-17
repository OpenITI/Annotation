# Atomistic maintenance of OpenITI and its metadata

1. Metadata is kept in the folder with each text (`metadata.brief`), where it is limited to:
	1. URI (must include the unique file/lib ID)
	2. Status (PRI/SEC)
	3. LengthInWords
	4. LengthInWords300Run [this one is not applicable to newly run texts that have not been included into passim-300-04-04]
2. *Script1* (`meta_OpenArabic_complete_300runLengths_parse_into_folders.py`):
	1. parses data from `meta_OpenArabic_complete_300runLengths` into individual files (`metadata.brief`) into relevant folders, where it can then be edited on the need-to basis
	2. This script needs to run only once, after which both the script and the metadata file obsolete and can be retired. 
3. *Script2* (`OpenITI_masterMetadata_brief_collect.py`)
	1. Collects/updates masterMetadata (`OpenITI_masterMetadata_brief`) from individual records, which are modified and/or added on the need-to basis.
	2. This will allow to keep adding new text as well as fixing possible existing issues (different URIs assigned to the same authors; error/typo in the URI, etc.)
	3. This script is to be run periodically to make sure that everything is up to date. 
4. Format for `metadata.brief` files
	1. YAML-like: key-value lines
		1. `uri` : full uri (Lib_ID part must be unique as well)
		2. `status`: primary or secondary
		3. `len` : length in words
		4. `len300`: length in words as was in the passim-300-0404 run (there is some discrepancy between the lengths of texts in OpenITI and that passim-run; some of the texts in OpenITI seem to be over formatted --- too much got deleted in the process of automatic conversion)
5. Format for `OpenITI_masterMetadata_brief`