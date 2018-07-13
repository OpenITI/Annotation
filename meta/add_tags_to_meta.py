import os, shutil, time, zipfile

def loadDic(file):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")
        dic = {}
        for d in data:
            d = d.split("\t")
            dic[d[0]] = d[1]

    return(dic)

tagsDic = loadDic("../ID_TAGS.txt")

def update(file):
    with open(file, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")
        head = data[0]+"\tTAGS\n"

        dataNew = []
        for d in data[1:]:
            d = d.split("\t")
            if d[4] in tagsDic:
                tags = tagsDic[d[4]]
            else:
                tags = "NO_TAGS"
            d.append(tags)
            dataNew.append("\t".join(d))
            #print(tags)
            #print(d)
            #input(d[4])

    with open(file.replace(".csv", "_TAGS.csv"), "w", encoding="utf8") as f9:
        f9.write(head+"\n".join(dataNew))

update("../OpenITI_metadata_light.csv")
print("Done!")
