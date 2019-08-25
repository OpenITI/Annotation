import csv, json

inputFile = csv.DictReader(open("OpenITI_metadata_light.csv"), delimiter="\t")

dic = {}

for r in inputFile:
	#print(r)
	dic[r["versionUri"]] = r


with open("OpenITI_metadata_complete.json", "w") as f9:
	json.dump(dic, f9)

