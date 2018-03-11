library(tidyverse)
library(readxl)

wg_demos <- read_excel("incoming_data/Korean_Yim/K-CDI_data_totals_extra info.xlsx", sheet = 1) %>%
  select(`X__1`, `subject ID`, `Test date`, `birth order`, `maternal education`)
  

ws_demos <- read_excel("incoming_data/Korean_Yim/K-CDI_data_totals_extra info.xlsx", sheet = 2) %>%
  select(`X__1`, `subject ID`, `Test date`, `Birth order`, `Maternal Education`)

wg_data <- read_csv("raw_data/Korean_WG/KoreanWG_Yim_data.csv")

ws_data <- read_csv("raw_data/Korean_WS/KoreanWS_Yim_data.csv") %>%
  mutate(subj_num = case_when(
    subj_num == "201" ~ "TO3001",
    subj_num == "202" ~ "TO3002",
    subj_num == "203" ~ "TO3003",
    subj_num == "204" ~ "TO3004",
    subj_num == "205" ~ "TO3005",
    TRUE ~ subj_num
  ))