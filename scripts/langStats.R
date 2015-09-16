library(dplyr)
library(jsonlite)
library(wordbankr)

admins <- get_administration_data(mode = "local")

lang_summary <- admins %>%
  group_by(language) %>%
  summarise(count = length(unique(data_id))) %>%
  rename(name = language)

lang_json <- toJSON(lang_summary, pretty = TRUE)

write(paste0('{"name": "", "children":\n', lang_json, '}'), "/home/ubuntu/wordbank/static/json/langStats.json")
