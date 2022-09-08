library(tidyverse)

# insts <- read_csv("../raw_data/instruments.csv") |>
#   select(language, form, form_type)
# insts <- wordbankr::get_instruments() |> select(language, form, form_type)
# ds <- wordbankr::get_datasets() |>
#   select(dataset_origin_name, language, form, form_type)

FORM_DICT <- tribble(
  ~form, ~form_type,
  'WS', 'WS',
  'WG', 'WG',
  'IC', 'WG',
  'TC', 'WS',
  'TEDS Twos', 'WS',
  'TEDS Threes', 'WS',
  'FormA', 'WG',
  'FormBOne', 'WS',
  'FormBTwo', 'WS',
  'FormC', 'WS',
  'Oxford CDI', 'WG',
  'Swingley', 'WG',
  'FormOne', 'WG',
  'FormTwoA', 'WG',
  'FormTwoB', 'WG',
  'FormThree', 'WS',
  'CDITwo', 'WG',
  'WSShort', 'WS',
  'WGShort', 'WG',
  'OxfordShort', 'WG',
)

datasets <- jsonlite::fromJSON("../wordbank/static/json/datasets.json") |>
  as_tibble() |>
  mutate(dataset_origin_name = paste(name, dataset, instrument_language, instrument_form, sep = "_")) |>
  select(language = instrument_language, form = instrument_form, name, dataset,
         dataset_origin_name, file) |>
  left_join(FORM_DICT)

get_ds_vals <- function(ds_file) {
  vals_file <- paste0("../", str_replace(ds_file, ".csv", "_values.csv"))
  vals <- read_csv(vals_file)
  word_vals <- vals |>
    filter(type == "word", !is.na(value)) |>
    pull(value)
}

ds_vals <- datasets |>
  mutate(word_vals = map(file, get_ds_vals))

ds_comp <- ds_vals |>
  unnest(word_vals) |>
  filter(form_type == "WS") |>
  group_by(dataset_origin_name) |>
  mutate(has_understands = "understands" %in% word_vals) |>
  ungroup()

ds_comp |>
  filter(has_understands) |>
  distinct(language, form, name, dataset) |>
  arrange(language, form)

ds_comp |>
  group_by(language, form) |>
  filter(any(has_understands)) |>
  count(language, form, has_understands, name = "n_datasets") |>
  count(language, form) |>
  ungroup() |>
  filter(n == 1) |>
  select(-n)

ds_comp |>
  group_by(language, form) |>
  filter(any(has_understands), !all(has_understands)) |>
  ungroup() |>
  filter(has_understands) |>
  distinct(language, form, name, dataset)

  # nest(datasets = dataset_origin_name)

  count(language, form, has_understands, name = "n_datasets") |>
  group_by(language, form) |>
  filter(n() > 1)
