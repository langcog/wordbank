library(tidyverse)
library(stringr)
library(readxl)

setwd("~/Documents/repo/wordbank/")

Korean_WG <- read_csv("raw_data/Korean_WG/[Korean_WG].csv") %>%
  filter(type == "word")

Korean_WS <- read_csv("raw_data/Korean_WS/[Korean_WS].csv") %>%
  filter(type == "word")

categories_WG <- Korean_WG %>%
  group_by(category) %>%
  summarise(first_id = as.numeric(str_extract(first(itemID),"[0-9]+")),
            last_id = as.numeric(str_extract(last(itemID),"[0-9]+")),
            num_items = n()) %>%
  arrange(first_id) %>%
  mutate(category_id = row_number())

categories_WS <- Korean_WS %>%
  group_by(category) %>%
  summarise(first_id = as.numeric(str_extract(first(itemID),"[0-9]+")),
            last_id = as.numeric(str_extract(last(itemID),"[0-9]+")),
            num_items = n()) %>%
  arrange(first_id) %>%
  mutate(category_id = row_number())

raw_WS <- read_excel("~/Desktop/K M-B CDI_for wordbank_180205/K M-B CDI_full_1138pres_2002-2003.xlsx", skip = 1)  %>% 
  group_by(id) %>% filter(row_number() == 1)

write_csv(raw_WS, "raw_data/Korean_WS/KoreanWS_Pae_data.csv", na = "")

raw_WG <- read_excel("~/Desktop/K M-B CDI_for wordbank_180205/K M-B CDI_full_563inf_2002-2003.xlsx", skip = 1)

wg_items <- str_subset(names(raw_WG), "^mg[0-9]+_[0-9]+$")

raw_col_names <- c()
clean_col_names <- c()

for (i in 1:nrow(categories_WG)) {
  x <- categories_WG[i,]
  raw_col_names <- c(raw_col_names, paste0("mg", x$category_id,"_", 1:x$num_items, rep(c("p", "u"), each = x$num_items)))
  clean_col_names <- c(clean_col_names, paste0("mg", x$category_id,"_", 1:x$num_items))
}

cleaned_WG <- raw_WG

names(cleaned_WG)[grep("^mg[0-9]+_[0-9]+$", names(raw_WG))] <- raw_col_names

write_csv(cleaned_WG, "raw_data/Korean_WG/KoreanWG_Pae_data.csv", na = "")