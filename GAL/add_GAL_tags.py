def loadGAL():
    with open("gal_first_run_GAL_tags.csv", "r", encoding="utf8") as f1:
        data = f1.read().split("\n")[1:]

        dic = {}

        for d in data:
            d = d.split("\t")

            ID = d[0].split(".")[-1].split("-")[0]
            TAGS = d[2].replace(" ", "").strip()

            dic[ID] = TAGS

    return(dic)

gal = loadGAL()
#print(gal)

def updateTAGS():
    with open("../OpenITI_metadata_light.csv", "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        dataNew = [data[0]]

        for d in data[1:]:
            d = d.split("\t")

            # ID = d[4]
            # TAGS = d[9]

            if d[4] in gal:
                TAGS = gal[d[4]]
            else:
                TAGS = "GAL@nodata"

            d[9] = d[9]+";"+TAGS

            #input("\n".join(d))

            dataNew.append("\t".join(d))

    with open("../OpenITI_metadata_light_withGAL.csv", "w", encoding="utf8") as f9:
        f9.write("\n".join(dataNew))


updateTAGS()

