library(tidyverse)
library(lubridate)

setwd("~/Documents/repo/wordbank/incoming_data/Spanish_Redux/")

spanishwg_instrument <- read_csv("../../raw_data/Spanish_WG/[Spanish_WG].csv")
spanishws_instrument <- read_csv("../../raw_data/Spanish_WS/[Spanish_WS].csv")

raw_spanishwg_fernald <- readxl::read_excel("SpanishWG_Fernald_Outreach.xlsx")
raw_spanishws_fernald <- readxl::read_excel("SpanishWS_Fernald_Outreach.xlsx")

raw_spanishwg_djm <- readxl::read_excel("SpanishWG_Marchman_Norming.xlsx")


spanishwg_fernald <- raw_spanishwg_fernald %>%
  mutate(BOrder = as.numeric(as.character(BOrder)),
         MotherEd = as.numeric(as.character(MotherEd)),
         DOB = round(as.numeric(CDIDate - DOB)/(365.2425/12.0))) %>%
  rename(DataAge = DOB)

spanishwg_fernald_words <- unique(gsub("/U|/P","", names(spanishwg_fernald)[grepl("/U|/P", names(spanishwg_fernald))]))


spanishwg_fernald_fields <- data_frame(field = NA, 
                                       column = c(names(spanishwg_fernald)[1:9],
                                                  spanishwg_fernald_words,
                                                  names(spanishwg_fernald)[866:963]), 
                                       group = NA, type = NA)

spanishwg_fernald_fields %<>% 
  left_join(select(spanishwg_instrument, itemID, item) %>%
            mutate(item = toupper(item)),
         by = c('column' = 'item')) %>%
  mutate(field = itemID) %>%
  select(-itemID)

names(spanishwg_fernald) <- gsub("/","",names(spanishwg_fernald))

