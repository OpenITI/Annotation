import csv, json

inputData = "OpenITI_metadata_light.csv"

inputFile = csv.DictReader(open(inputData), delimiter="\t")

l = []

for r in inputFile:
	#print(r)
	l.append(r)

dic = {}
dic["data"] = l

with open(inputData.replace(".csv", ".json"), "w") as f9:
	json.dump(dic, f9)

