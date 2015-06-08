library(dplyr)
library(jsonlite)
source("/home/ubuntu/wordbank/shiny_apps/data_loading.R")

wordbank <- connect.to.wordbank("prod")

common.tables <- get.common.tables(wordbank)

admins <- get.administration.data(common.tables)

lang.summary <- admins %>%
  group_by(language) %>%
  summarise(count = length(unique(data_id))) %>%
  rename(name = language)

lang.json <- toJSON(lang.summary, pretty = TRUE)

write(paste0('{"name": "", "children":\n', lang.json, '}'), "/home/ubuntu/wordbank/static/json/langStats.json")