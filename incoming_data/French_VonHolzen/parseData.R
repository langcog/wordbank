library(tidyverse)
library(stringr)
library(magrittr)
library(feather) # Version 0.3.1 (CSV format failed to parse neatly)

setwd("~/Documents/repo/wordbank/")
file_loc <- "incoming_data/French_VonHolzen/raw_data.feather"
voc <- read_feather(file_loc)
word_categories <- read_csv("incoming_data/French_VonHolzen/categories.csv")

if ("date.birth" %in% names(voc)) {
  voc %<>%
    mutate_at(vars("date.comp", "date.birth"), funs(gsub("^00","20",.))) %>%
    mutate(age = floor((parse_datetime(.data$date.comp, format = "%Y-%m-%d") - parse_datetime(.data$date.birth, format = "%Y-%m-%d"))/(365.2425/12))) %>%
    select(-age.days, -date.birth)
}

voc %<>%
  mutate(num_response = case_when(
    is.na(response) ~ 0,
    response == 0 ~ 0,
    response == 1 ~ 1,
    response == 2 ~ 2,
    response == 0.5 ~ 0,
    response == 10 ~ 1
  )) %>%
  select(-phon, -ends_with("seq")) %>%
  mutate(othro = ifelse(category == "grammar", gsub("/",";", othro), othro))

# french_items <- word_categories %>% 
#   left_join(unique(voc[,c("form.age", "category", "sub_category", "othro")]), 
#             by = c("form.age", "category", "sub_category")) %>%
#   group_by(form.age) %>%
#   arrange(desc(form.age), category_id, othro) %>%
#   mutate(itemID = paste0("item_", row_number(form.age)))

french_items <- bind_rows("French_WS" = read_csv("incoming_data/French_VonHolzen/[French_WS].csv"),
                       "French_WG" = read_csv("incoming_data/French_VonHolzen/[French_WG].csv"),
                       .id = "instrument") %>% 
  mutate(split_definition = ifelse(form.age == "16_30" & type == "complexity", 
                                   strsplit(as.character(definition), "/"), definition)) %>% 
  unnest(split_definition)

merged_words_gestures <- french_items %>%
  filter(!type %in% c("complexity", "verb_endings")) %>%
  full_join(voc %>% filter(category != "grammar") %>% mutate(othro = trimws(othro)),
            by = c("form.age", "orig_category" = "category","sub_category", "split_definition" = "othro"))

merged_grammar <- french_items %>%
  filter(type %in% c("complexity", "verb_endings")) %>%
  select(-sub_category) %>%
  mutate(split_definition = trimws(split_definition)) %>%
  full_join(voc %>% filter(category == "grammar") %>% mutate(othro = trimws(othro)),
            by = c("form.age", "orig_category" = "category", "split_definition" = "othro")) %>%
  mutate(grammar_correct = ifelse( sub_category == "correct" & num_response == 1, 1, 0)) %>%
  group_by_at(vars(-sub_category, -split_definition, -response, -num_response, -grammar_correct)) %>%
  summarise(num_response = ifelse(sum(grammar_correct) > 0, 1, 0))

scored_data <- bind_rows(merged_words_gestures, merged_grammar) %>%
  select(instrument, itemID, sub:num_response) %>%
  group_by_at(vars(-num_response)) %>%
  summarise(num_response = max(num_response)) %>% ungroup() %>%
  split(.$instrument) %>%
  map(function(x) {
    item_names <- filter(french_items, instrument == first(x$instrument))$itemID
    y <- x %>%
      group_by_at(vars(-itemID, -num_response, -age.months)) %>%
      spread(key = .data$itemID, value = .data$num_response) %>%
      mutate(new_sub = paste0(exp, "_", sub)) %>%
      select(instrument, new_sub, sub:age, item_names, -age.months)
    write_csv(y, paste0("incoming_data/French_VonHolzen/", first(y$instrument), "_VonHolzen_data.csv"), na = "")
    return(y)
  })
