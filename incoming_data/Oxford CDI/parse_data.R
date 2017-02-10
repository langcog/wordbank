library(readxl)
library(tidyverse)
setwd("~/Documents/repo/wordbank/incoming_data/Oxford CDI/")
raw_data <- read_excel("data for WordBank.xlsx", sheet=1)

variable_names_location <- seq(6,1259,3)
word_categories <- names(raw_data)[variable_names_location]
word_definition <- as.vector(raw_data[1,variable_names_location])
trimmed_data <- raw_data
trimmed_data[,variable_names_location] <- NULL
names(trimmed_data)[6:(ncol(trimmed_data)-2)] <- trimws(paste0(rep(1:length(word_definition), each=2),"_",trimws(rep(word_definition, each = 2)), c("u", "p")))

names(trimmed_data) <- gsub(" / ","_",names(trimmed_data))
names(trimmed_data) <- gsub(" ","_", names(trimmed_data))
names(trimmed_data) <- gsub("\\(","", names(trimmed_data))
names(trimmed_data) <- gsub("\\)","", names(trimmed_data))


trimmed_data <- trimmed_data %>% mutate(Agemonths = round(Agedays/30.42,1))
trimmed_data <- trimmed_data[,c(1:5, ncol(trimmed_data), 6:(ncol(trimmed_data)-1))]

write.csv(trimmed_data, "EnglishBritishOxford_Foccana_data.csv", row.names = F)

cross_data <- trimmed_data %>% group_by(childcode) %>% filter(n() == 1)
longi_data <- trimmed_data %>% group_by(childcode) %>% filter(n() > 1)

write.csv(cross_data, "EnglishBritishOxford_Floccia_crosssectional_data.csv", row.names = F)
write.csv(longi_data, "EnglishBritishOxford_Floccia_longitudinal_data.csv", row.names = F)

instrument <- data_frame(itemID = paste0("item_",1:length(word_definition)), item = trimws(paste0(1:length(word_definition),"_",trimws(word_definition))), category = word_categories, choices = "understands; produces", uni_lemma = "", definition = trimws(unname(unlist(word_definition))), gloss = "",complexity_category="")

instrument$item <- gsub(" / ","_",instrument$item)
instrument$item <- gsub(" ","_", instrument$item)
instrument$item <- gsub("\\(","", instrument$item)
instrument$item <- gsub("\\)","", instrument$item)

write.csv(instrument, "[EnglishBritishOxford].csv", row.names = F)
