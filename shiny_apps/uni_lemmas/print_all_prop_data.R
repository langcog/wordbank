
library(tidyverse)
library(langcog)
library(wordbankr)
library(boot)
library(lazyeval)
library(robustbase)
library(here)
theme_set(theme_mikabr() +
            theme(panel.grid = element_blank(),
                  strip.background = element_blank()))
font <- "Open Sans"

setwd(here())

# Connect to the Wordbank database and pull out the raw data.
data_mode <- "remote"

all_prop_data <- feather::read_feather("all_prop_data.feather")
uni_lemmas <- sort(unique(all_prop_data$uni_lemma))
start_lemma <- "dog"
kid_min <- 3
points_min <- 3

all_prop_data <- get_instruments(mode = data_mode) %>%
  split(list(.$language, .$form), drop = TRUE) %>%
  map_df(function(x){
    y <- get_instrument_data(language = x$language, form = x$form,
                             administrations = TRUE, iteminfo = TRUE, mode = data_mode)
    return(y)
  })  %>%
  filter(!is.na(uni_lemma)) %>%
  mutate(value = ifelse(!is.na(value), value, "")) %>%
  mutate(produces = ifelse(value == "produces", 1, 0),
         understands = ifelse(value %in% c("understands", "produces"), 1, 0)) %>%
  group_by(language, uni_lemma, age) %>%
  summarise(words = definition %>% strsplit(", ") %>% unlist() %>% unique() %>%
              paste(collapse = ", "),
            produces = mean(produces),
            understands = mean(understands),
            n = n_distinct(data_id)) %>%
  gather(key = "measure", value = "prop", produces, understands)

feather::write_feather(all_prop_data,"all_prop_data.feather")
write_csv(all_prop_data,"all_prop_data.csv", na = "")


