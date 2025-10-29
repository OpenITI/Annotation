import csv, json

inputData = "OpenITI_metadata_light.csv"

inputFile = csv.DictReader(open(inputData), delimiter="\t")

dic = {}

for r in inputFile:
	#print(r)
	dic[r["versionUri"]] = r


with open(inputData.replace(".csv", ".json"), "w") as f9:
	json.dump(dic, f9)

