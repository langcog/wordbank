library(tidyverse)
library(readxl)
library(lubridate)
library(janitor)
library(stringr)

setwd("~/Documents/repo/wordbank/")

grab_french_data <- function(filepath, grab = "instrument") {
  x <- read_excel(filepath)
  names(x) <- paste('col',1:ncol(x), sep = "_")
  
  demo_info <- x[seq(which(grepl('Prénom', x$col_1), arr.ind = T),
        which(grepl('DATE A LAQUELLE', x$col_1), arr.ind = T)),] %>%
    filter(!is.na(col_1)) %>%
    replace_na(list(col_2 = "", col_3 = "", col_4 = "")) %>%
    unite(value, col_2:col_4, sep = "") %>%
    rename(item_id = col_1) %>%
    select(item_id, value)
  
  cdi_info <- x[seq((which(x$col_1 == '1', arr.ind = T)-1),
                    which(x$col_1 == '683', arr.ind = T)),]
  
  category_label_locations <- grep("[a-zA-Z]", cdi_info$col_1)
  
  a <- vector(mode = "character")
  for (i in 1:length(category_label_locations)) {
    
    category_label_loc <- category_label_locations[i]
    category_label <- cdi_info$col_1[category_label_loc]
    
    if (i != length(category_label_locations)) {
      next_label_location <- category_label_locations[i+1]
    } else {
      next_label_location = nrow(cdi_info) + 1
    }
    
    a <- c(a, rep(category_label, times = (next_label_location - category_label_loc)))
  }
    
  cdi_info <- cdi_info %>%
    mutate(original_category = a) %>%
    filter(!is.na(col_2)) %>%
    mutate(item_id = paste('item', col_1, sep = "_"),
           value = ifelse(grepl('x', col_4, ignore.case = T), 
                          ifelse(grepl('x', col_3, ignore.case = T), 2, 1),
                          ifelse(grepl('x', col_3, ignore.case = T), 2, 0))) %>%
    rename(definition = col_2) %>%
    select(item_id, definition, original_category, value)

  if (grab == "instrument") {
    instrument <- select(cdi_info, -value)
    return(instrument)
  } else if (grab == "responses") {
    full_info <- bind_rows(demo_info,
              cdi_info %>%
                mutate(value = as.character(value)) %>%
                select(item_id, value)) %>%
      rename(!!gsub("_.*$", "", basename(filepath)):=value)
    return(full_info)
  }
}

cdi_files <- list.files("~/Downloads/14mois_CDI", pattern = "*.xls*", full.names = TRUE)

cdi_instrument <- grab_french_data(cdi_files[[1]], "instrument") %>%
  mutate(category = case_when(
    original_category == "Cris d'animaux et sons" ~ "sounds",
    original_category == "Véhicules ( vrais ou jouets)" ~ "vehicles",
    original_category == "Jouets" ~ "toys",
    original_category == "Noms d'animaux (vrais ou jouets)" ~ "animals",
    original_category == "Nourriture et boisson" ~ "food_drink",
    original_category == "Vêtements" ~ "clothing",
    original_category == "Parties du corps" ~ "body_parts",
    original_category == "Meubles et pièces" ~ "furniture_rooms",
    original_category == "Jeux et routines" ~ "games_routines",
    original_category == "Endroits où aller" ~ "places",
    original_category == "Prépositions et localisations" ~ "prepositions",
    original_category == "Interrogatifs" ~ "question_words",
    original_category == "Quantificateurs et articles" ~ "quantifiers",
    original_category == "Pronoms" ~ "pronouns",
    original_category == "Mots sur le temps" ~ "time_words",
    original_category == "Connecteurs" ~ "connecting_words",
    original_category == "Objets extérieurs" ~ "outside",
    original_category == "Personnes" ~ "people",
    original_category == "Auxiliaires" ~ "helping_verbs",
    original_category == "Petits objets ménagers" ~ "household",
    original_category == "Mots descriptifs" ~ "descriptive_words",
    original_category == "Mots d'action" ~ "action_words"
  ))

clean_up_dates <- function(x) {
  y <- list()
  
  for (item in x) {
    if (item == "") {
      y <- c(y, NA)
    } else {
      y <- c(y, as.Date(item, origin = "1899-12-30"))
    }
  }
  
  return(y)
}

cdi_data <- cdi_files %>%
  map(grab_french_data, "responses") %>%
  reduce(full_join, by = "item_id") %>%
  filter(item_id != "item_NA") %>%
  gather(subj, value, -item_id) %>%
  spread(item_id, value) %>%
  clean_names(.) %>%
  mutate_at(vars(starts_with("date")), funs( excel_numeric_to_date(as.numeric(.)) )) %>%
  mutate(age = floor(as.numeric(as.duration(
    interval(date_de_naissance, date_a_laquelle_vous_avez_rempli_ce_questionnaire)), 
    "d")/(365.2425/12))) %>%
  select(str_subset(names(.),"^(?!item).+"), cdi_instrument$item_id, -date_de_naissance) %>%
  mutate(sexe = as.character(forcats::fct_collapse(sexe,
                                      `F` = c("féminin", "F", "Féminin", "Feminin", "feminin"),
                                      `M` = c("M", "masculin", "Garçon", "Masculin", "garçon"))))

names(cdi_data) <- stringi::stri_trans_general(names(cdi_data), "Latin-ASCII")

write_csv(cdi_instrument, "incoming_data/French_Bergmann/french_instrument.csv", na = "")
write_csv(cdi_data, "incoming_data/French_Bergmann/french_data.csv", na = "")

write_csv(filter(french_items, instrument == "French_WS") %>%
            mutate(item = itemID) %>%
            select(itemID, item, type:uni_lemma), 
          "raw_data/French_France_WS/[French_France_WS].csv", na = "")

raw_merged_instrument <- french_items %>%
  filter(instrument == "French_WG") %>%
  mutate(item = itemID) %>%
  select(itemID, item, type:uni_lemma) %>%
  full_join(cdi_instrument, by = c("definition", "category"), suffix = c(" (VH)", " (B)"))

merged_instrument <- read_csv("raw_data/French_France_WG/[French_France_WG].csv")

write_csv(cdi_instrument, "raw_data/French_France_WG/FrenchFranceWG_Bergmann_data.csv", na = "")
write_csv(scored_data$French_WG, "raw_data/French_France_WG/FrenchFranceWG_VonHolzen_data.csv", na = "")

FrenchFranceWG_Bergmann_fields <- data_frame(column = names(cdi_data), group = NA) %>%
  left_join(merged_instrument %>%
              select(itemID, item_id, type) %>% 
              rename(field = itemID), 
            by = c("column" = "item_id")) %>%
  mutate(
    group = case_when(
      type == "word" ~ "item",
      column %in% c("subj", "sexe") ~ "child",
      column %in% c("date_a_laquelle_vous_avez_rempli_ce_questionnaire", "age") ~ "admin",
      TRUE ~ as.character(group)),
    field = case_when(
      column == "subj" ~ "study_id",
      column == "date_a_laquelle_vous_avez_rempli_ce_questionnaire" ~ "date_of_test",
      column == "sexe" ~ "sex",
      column == "age" ~ "data_age",
      TRUE ~ as.character(field)),
    type = case_when(
      column == "subj" ~ "study_id",
      column == "date_a_laquelle_vous_avez_rempli_ce_questionnaire" ~ "date_of_test",
      column == "sexe" ~ "sex",
      column == "age" ~ "data_age",
      TRUE ~ as.character(type))
    ) %>%
  select(field, column, group, type)

write_csv(FrenchFranceWG_Bergmann_fields, "raw_data/French_France_WG/FrenchFranceWG_Bergmann_fields.csv", na = "")

FrenchFranceWG_VonHolzen_fields <- data_frame(column = names(scored_data$French_WG), group = NA) %>%
  left_join(merged_instrument %>%
              select(itemID, type) %>% 
              mutate(field = itemID), 
            by = c("column" = "itemID")) %>%
  mutate(
    group = case_when(
      !is.na(type) ~ "item",
      column %in% c("new_sub") ~ "child",
      column %in% c("date.comp", "age") ~ "admin",
      TRUE ~ as.character(group)),
    field = case_when(
      column == "new_sub" ~ "study_id",
      column == "date.comp" ~ "date_of_test",
      column == "age" ~ "data_age",
      TRUE ~ as.character(field)),
    type = case_when(
      column == "new_sub" ~ "study_id",
      column == "date.comp" ~ "date_of_test",
      column == "age" ~ "data_age",
      TRUE ~ as.character(type))
  ) %>%
  select(field, column, group, type)

write_csv(FrenchFranceWG_VonHolzen_fields, "raw_data/French_France_WG/FrenchFranceWG_VonHolzen_fields.csv", na = "")

write_csv(scored_data$French_WS, "raw_data/French_France_WS/FrenchFranceWS_VonHolzen_data.csv", na = "")
