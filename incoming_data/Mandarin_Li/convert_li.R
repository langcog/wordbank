library(readxl)

ping_file = "~/Documents/projects/wordbank/raw_data/Mandarin_TC/MandarinTC_Li_source.xls"

read_ping <- function(age) {
  ping <- read_excel(ping_file, as.character(age))
  ping <- ping[!is.na(ping$item),]
  ping[is.na(ping) | ping == "0" | ping == " " | ping == "9"] <- ""
  ping[ping == "2" | ping == "11" | ping == "1.000000"] <- "1"
  row.names(ping) <- ping$item
  ping$item <- NULL
  
  ping_t <- as.data.frame(t(ping))
  ping_t$study_id <- row.names(ping_t)
  row.names(ping_t) <- NULL
  ping_t$age <- age
  ping_t
}

ping_all <- bind_rows(sapply(seq(17, 30, 1),
                             function(age) read_ping(age),
                             simplify = FALSE))

data_file <- file("~/Documents/projects/wordbank/raw_data/Mandarin_TC/MandarinTC_Li_data.csv",
                  encoding = "utf8")
write.csv(ping_all[,c(711, 712, 1:710)], row.names = FALSE,
          file = data_file)

cols <- names(select(ping_all, -study_id, -age))
fields <- data.frame(field = paste("item", 1:length(cols), sep = "_"),
                     column = cols,
                     group = "item",
                     type = "word")
write.csv(fields, row.names = FALSE,
          file = "~/Documents/projects/wordbank/raw_data/Mandarin_TC/MandarinTC_Li_fields.csv")
