library(tidyverse)
library(readxl)

wg_demos <- read_excel("incoming_data/Korean_Yim/K-CDI_data_totals_extra info.xlsx", sheet = 1) %>%
  select(`subject ID`, `birth order`, `maternal education`)

ws_demos <- read_excel("incoming_data/Korean_Yim/K-CDI_data_totals_extra info.xlsx", sheet = 2) %>%
  select(`subject ID`, `Birth order`, `Maternal Education`)

wg_data_loc <- "raw_data/Korean_WG/KoreanWG_Yim_data.csv"
wg_data <- read_csv(wg_data_loc) %>%
  left_join(wg_demos, by = c("subj_num" = "subject ID")) %>%
  select(s_no:age_months, `birth order`, `maternal education`, item_001:item_344)

ws_data_loc <- "raw_data/Korean_WS/KoreanWS_Yim_data.csv"
ws_data <- read_csv(ws_data_loc)%>%
  left_join(ws_demos, by = c("subj_num" = "subject ID")) %>%
  select(s_no:age_months, `Birth order`, `Maternal Education`, item_001:item_679)

write_csv(wg_data, wg_data_loc, na = "")
write_csv(ws_data, ws_data_loc, na = "")