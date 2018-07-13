#install.packages("rstudioapi")
library(rstudioapi)
current_path <- getActiveDocumentContext()$path 
setwd(dirname(current_path))
print(getwd())

openITImeta <- read.csv(file="../OpenITI_metadata_light_TAGS.csv",
                              header=T, sep="\t", quote="",
                              stringsAsFactors=FALSE)

openITIpri = openITImeta[openITImeta$status=="pri",]
openITIpri <- subset(openITIpri, select = -c(versionUri,status,url,instantiation))
openITIpri$count = 1

library(dplyr)
ppe = dplyr::filter(openITIpri, grepl('PPE', TAGS))
ppe = ppe[order(-ppe$length),]

authors = unique(ppe$author)

results = NULL

for (a in authors){
  row = c()
  row = c(row, a)

  temp = ppe[ppe$author==a,]
  temp = temp[order(-temp$length),]
  
  row = c(row, temp$book[1])
  row = c(row, temp$length[1])
  
  temp = openITIpri[openITIpri$author==a,]
  row = c(row, nrow(temp))
  row = c(row, sum(temp$length))
  
  results = rbind(results, row)
  
}

results = as.data.frame(results, stringsAsFactors=FALSE)

write.csv(results, "../polymaths.csv" )
