library(tidyverse)

raw_wg_data <- read_csv("incoming_data/Portuguese_Cadime/MacArthur 8-15 months WordBank.csv")

raw_ws_data <- read_csv("incoming_data/Portuguese_Cadime/MacArthur 16-30 months WordBank.csv")


wg_data <- raw_wg_data
ws_data <- raw_ws_data

comprehension_locs <- grep("VR_",names(wg_data))
production_locs <- grep("VE_",names(wg_data))

names(wg_data)[comprehension_locs] <- paste0(gsub("^VR_", "", names(wg_data)[comprehension_locs]), "u")
names(wg_data)[production_locs] <- paste0(gsub("^VE_", "", names(wg_data)[production_locs]), "p")

write_csv(wg_data, "incoming_data/Portuguese_Cadime/PortugueseEuropeanWG_Kadime_data.csv", na = "")
write_csv(ws_data, "incoming_data/Portuguese_Cadime/PortugueseEuropeanWS_Kadime_data.csv", na = "")