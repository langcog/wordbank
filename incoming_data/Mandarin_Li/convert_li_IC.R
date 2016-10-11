library(readxl)
library(dplyr)
setwd("~/Documents/repo/wordbank/incoming_data/Mandarin_Li/")
ping_comp = "12-16 comprehension raw data.xls"
ping_prod = "12-16 production raw data.xls"
ping_items <- "[Mandarin_IC].csv"
instrument <- read.csv(ping_items)

read_ping <- function(age, file) {
  ping <- read_excel(file, as.character(age))
  ping[is.na(ping) | ping == "0" | ping == " " | ping == "9"] <- ""
  ping[ping == "2" | ping == "11" | ping == "1.000000"] <- "1"
  
  ping_t <- as.data.frame(t(ping))
  ping_t$study_id <- trimws(toupper(row.names(ping_t)), "both")
  row.names(ping_t) <- NULL
  ping_t$age <- age
  a <- match("study_id", colnames(ping_t))
  ping_t[,c(a,(a+1),1:(a-1))]
}

ping_all_comp <- bind_rows(mapply(read_ping, seq(12,16,1), ping_comp))
ping_all_comp$V233 <- NULL
colnames(ping_all_comp)[3:ncol(ping_all_comp)] <- paste0(instrument$item,1:nrow(instrument),"u", sep="_")
ping_all_comp[is.na(ping_all_comp)] <- ""
ping_all_comp$study_id[ping_all_comp$study_id=="S372"] <- "S1372"

ping_all_prod <- bind_rows(mapply(read_ping, seq(12,16,1), ping_prod))
colnames(ping_all_prod)[3:ncol(ping_all_prod)] <- paste0(instrument$item,1:nrow(instrument),"p", sep="_")
ping_all_prod[is.na(ping_all_prod)] <- ""
ping_all_prod$study_id[ping_all_prod$study_id=="1208.000000"] <- "S1208"

a <- anti_join(ping_all_comp,ping_all_prod)
ping_all <- left_join(ping_all_prod, ping_all_comp)
sorted_items <- paste0(rep(colnames(ping_all_prod, each = 2)))
ping_sorted <- ping_all[,c("study_id","age", sorted_items)]

data_file <- file("MandarinTC_Li_data.csv",
                  encoding = "utf8")
write.csv(ping_sorted, row.names = FALSE,
          file = data_file)

cols <- instrument$itemID
fields <- data.frame(field = paste("item", 1:nrow(instrument), sep = "_"),
                     column = cols,
                     group = "item",
                     type = "word")
write.csv(fields, row.names = FALSE,
          file = "MandarinTC_Li_fields.csv")
