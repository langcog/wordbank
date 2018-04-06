library(tidyverse)
library(readxl)

wg_comp <- read_csv("Taiwan_8-16_word comprehension.csv")
wg_prod <- read_csv("Taiwan_8-16_word expression.csv")
ws_data <- read_csv("Taiwan_16-36_word expression.csv")

names(wg_prod)[grepl('d[0-9]{2}_[0-9]{2}', names(wg_prod))] <- paste0(names(wg_prod)[grepl('d[0-9]{2}_[0-9]{2}', names(wg_prod))], "p")

names(wg_comp)[grepl('d[0-9]{2}_[0-9]{2}', names(wg_comp))] <- paste0(names(wg_comp)[grepl('d[0-9]{2}_[0-9]{2}', names(wg_comp))], "u")

wg_data <- bind_cols(wg_prod[,!grepl('d[0-9]{2}_[0-9]{2}', names(wg_prod))],
                     wg_comp[, grepl('d[0-9]{2}_[0-9]{2}', names(wg_comp))],
                     wg_prod[,grepl('d[0-9]{2}_[0-9]{2}', names(wg_prod))])

write_csv(wg_data, "../../raw_data/Mandarin_Taiwanese_WG/MandarinTaiwaneseWG_Liu_data.csv", na = "")
write_csv(ws_data, "../../raw_data/Mandarin_Taiwanese_WS/MandarinTaiwaneseWS_Liu_data.csv", na = "")

