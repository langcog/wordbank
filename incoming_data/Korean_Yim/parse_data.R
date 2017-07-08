setwd("~/Documents/repo/wordbank/incoming_data/Korean_Yim/")

library(tidyverse)
library(lubridate)
library(magrittr)

korean_wg <- readxl::read_excel("Project Form_KMBCDI(infant)_Sample & Batch 2-3_16 40 Records (Consolidated Files)_Updated.xlsx",skip = 2)
korean_ws <- readxl::read_excel("Project Form_KMBCDI(toddler)_Sample & Batch 3-16 156 Records (Consolidated Files) 2.xlsx",skip = 2)

korean_words <- read_csv("Korean_subsections.csv")

subsections <- readxl::read_excel("K-CDI_data_EWHA.xlsx")
  
names(korean_wg)[1:6] <- c("s_no",	"subj_num",	"dot",	"dob",	"gender",	"age")
names(korean_ws)[1:6] <- c("s_no",	"subj_num",	"dot",	"dob",	"gender",	"age")

names(korean_wg)[7:ncol(korean_wg)] <- sprintf("item_%03d", seq(1,(ncol(korean_wg)-6)))
names(korean_ws)[7:ncol(korean_ws)] <- sprintf("item_%03d", seq(1,(ncol(korean_ws)-6)))

korean_wg %<>%
  filter(grepl('IN', subj_num))

korean_ws %<>%
  filter(grepl('TO', subj_num))

korean_wg$dot <- format(parse_date_time(korean_wg$dot, "Ymd", truncated = 3),"%m/%d/%Y")
korean_ws$dot <- format(parse_date_time(korean_ws$dot, "Ymd", truncated = 3),"%m/%d/%Y")
korean_wg$dob <- format(parse_date_time(korean_wg$dob, "Ymd", truncated = 3),"%m/%d/%Y")
korean_ws$dob <- format(parse_date_time(korean_ws$dob, "Ymd", truncated = 3),"%m/%d/%Y")

write_csv(korean_wg, "KoreanWG_Yim_data.csv", na = "")
write_csv(korean_ws, "KoreanWS_Yim_data.csv", na = "")

instrument_wg <- read_csv("[Korean_WG].csv")
uni_lemmas_wg <- read_csv("unilemma_korean_wg.csv") %>% filter(!is.na(itemID))
instrument_ws <- read_csv("[Korean_WS].csv")
uni_lemmas_ws <- read_csv("unilemma_korean_ws.csv") %>% filter(!is.na(itemID))


instrument_wg %<>% 
  left_join(uni_lemmas_wg %>% select(uni_list, itemID)) %>%
  rename(uni_lemma = uni_list)

instrument_ws %<>% 
  left_join(uni_lemmas_ws %>% select(uni_list, itemID)) %>%
  rename(uni_lemma = uni_list)


summed_wg <- korean_wg %>%
  gather(key = item_id, value = score, item_001:item_284) %>%
  left_join(filter(korean_words, form == 'infant')[,c("item_id","section")]) %>%
  group_by(subj_num, section) %>%
  summarise(comp = sum(score %in% c("U","P"), na.rm = T),
            prod = sum(score == "P", na.rm = T)) %>%
  group_by(subj_num) %>%
  summarise(total_prod = sum(prod), total_comp = sum(comp))

summed_ws <- korean_ws %>%
  gather(key = item_id, value = score, item_001:item_641) %>%
  left_join(filter(korean_words, form == 'toddler')[,c("item_id","section")]) %>%
  group_by(subj_num, section) %>%
  summarise(comp = sum(score %in% c("U","P"), na.rm = T),
            prod = sum(score == "P", na.rm = T)) %>%
  group_by(subj_num) %>%
  summarise(total_prod = sum(prod), total_comp = sum(comp))
  