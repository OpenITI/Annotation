library(readr)
ID_TAGS <- read_delim("~/_OpenITI/Annotation/ID_TAGS.txt", 
                      "\t", escape_double = FALSE, col_names = FALSE, 
                      trim_ws = TRUE)

length(ID_TAGS$X1)
unique(length(ID_TAGS$X1))

GAL <- read_delim("~/_OpenITI/Annotation/GAL/gal_first_run_GAL_tags_for_merge.csv", 
                                               "\t", escape_double = FALSE, col_names = FALSE, 
                                               trim_ws = TRUE)

length(GAL$X1)
unique(length(GAL$X1))

library(tidyverse)

new <- full_join(ID_TAGS, GAL, by="X1")

new <- unique(new)

target = "~/_OpenITI/Annotation/GAL/GAL_tags.csv"
write.table(new, target, sep="\t", row.names = FALSE, col.names = FALSE)


test <- read_delim("~/_OpenITI/Annotation/GAL/GAL_tags_clean.csv", 
                  "\t", escape_double = FALSE, col_names = FALSE, 
                  trim_ws = TRUE)

length(unique(test$X1))
test1 <- test$X1

dupes <- unique(test1[duplicated(test1)])
dupes

#[1] "Shamela0021546" "Shamela0023578" "Shia002529Vols" "NOTEXTFILE"     "Shamela0012061" "Shia004518"    
#[7] "Shia004519" 


t1 <- test$X1
t1 <- t1[t1==dupes]

miniTable <- test %>%
  filter(X1 %in% dupes)

t2 <- unique(miniTable)
