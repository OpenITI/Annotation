import re

inFile  = "gal_first_run.csv"
outFile = inFile.replace(".csv", "_stats.csv") 

def gen_gal_cats_I(inFile, outFile):
    with open(inFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        analysis = {}
        table    = []

        for d in data[1:]:
            d_list = d.strip().split("\t")[1].split(".")
            #print(d)

            for l in d_list:
                l = l.lower().strip()
                if l in analysis:
                    analysis[l] += 1
                else:
                    analysis[l]  = 1


        for k,v in analysis.items():
            table.append("\%09d\t%s" % (v, k))

        table = "\n".join(sorted(table, reverse=True))
        with open(outFile, "w", encoding="utf8") as f9:
            f9.write(table)
        
#gen_gal_cats_I(inFile, outFile)

inFile  = "gal_first_run_stats_manual.csv"
outFile = inFile.replace(".csv", "_stats.csv") 

def gen_gal_cats_II(inFile, outFile):
    with open(inFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        analysis = {}
        table    = []

        for d in data[1:]:
            d_list = d.strip().split("\t")[2].split(";")
            d_freq = int(d.strip().split("\t")[0])
            #print(d)

            for l in d_list:
                l = l.lower().strip()
                if l in analysis:
                    analysis[l] += d_freq
                else:
                    analysis[l]  = d_freq


        for k,v in analysis.items():
            table.append("%09d\t%s" % (v, k))

        table = "\n".join(sorted(table, reverse=True))
        with open(outFile, "w", encoding="utf8") as f9:
            f9.write(table)

#gen_gal_cats_II(inFile, outFile)


# UPDATE TAGS

# load dictionary

def loadDic(dicFile):
    with open(dicFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        dic = {}

        for d in data:
            d = d.split("\t")

            dic[d[1]] = d[2]

    return(dic)

matchingDic = loadDic("gal_first_run_stats_manual.csv")


import itertools
def applyCatScheme(metaFile):
    with open(metaFile, "r", encoding="utf8") as f1:
        data = f1.read().split("\n")

        head = data[0] + "\tGAL@Tags"

        newData = [head]
        edges   = []

        for d in data[1:]:
            d_list  = d.split("\t")
            d_cat   = d_list[1].strip().lower().split(".")
            d_title = d_list[0]

            new_Tags = []
            for c in d_cat:
                new_Tags.append(matchingDic[c.strip()])

            new_Tags = ";".join(new_Tags).replace(" ", "")
            new_Tags = re.sub(";$", "", new_Tags)
            new_Tags = new_Tags.strip().split(";")
            new_Tags = list(set(new_Tags))

            GALtags = "GAL@"+"; GAL@".join(new_Tags)
            print(GALtags)

            newData.append(d+"\t"+GALtags)
            print(new_Tags)

            # edges
            edges_temp = list(itertools.combinations(new_Tags,2))
            for e in edges_temp:
                edges.append("\t".join(sorted(e)))

    with open(metaFile.replace(".csv", "_GAL_tags.csv"), "w", encoding="utf8") as f9:
        f9.write("\n".join(newData))

    head = "Source\tTarget\n"
    with open(metaFile.replace(".csv", "_EDGES.csv"), "w", encoding="utf8") as f9:
        f9.write(head + "\n".join(edges))



applyCatScheme("gal_first_run.csv")

