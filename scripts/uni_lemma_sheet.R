library(wordbankr)
library(dplyr)
library(googlesheets)
library(purrr)

languages <- c(
  # "British Sign Language" = FALSE,  # not mapped, no stemmer, not in CHILDES
  "Croatian" = FALSE,  # no stemmer
  "Danish" = FALSE,  # not mapped
  "English" = TRUE,
  "French (Quebec)" = FALSE,  # not mapped
  # "Hebrew" = FALSE,  # no stemmer, CHILDES transcription problems
  "Italian" = TRUE,
  "Norwegian" = TRUE,
  "Russian" = TRUE,
  # "Slovak" = FALSE,  # not mapped, no stemmer, not in CHILDES
  "Spanish" = TRUE,
  "Swedish" = TRUE,
  "Turkish" = TRUE
)

#uni_sheet <- gs_new("Wordbank translation equivalents")
uni_sheet <- gs_title("Wordbank translation equivalents")

wg_items <- get_item_data(form = "WG", mode = "local")
wg_words <- wg_items %>%
  filter(type == "word") %>%
  select(language, item_id, category, definition, uni_lemma)

create_lang_sheet <- function(lang) {
  lang_lemmas <- wg_words %>% filter(language == lang)
  lang_input <- lang_lemmas %>%
    select(-language) %>%
    rename(translation = uni_lemma) %>%
    arrange(category, definition)
  blank_cols <- c("Is translation good?", "Alternative translation", "Notes")
  walk(blank_cols, ~lang_input[[.x]] <- "")
  gs_ws_new(uni_sheet, ws_title = lang, input = lang_input)
}

languages %>%
  keep(~.x) %>%
  names() %>%
  walk(create_lang_sheet)

uni_lemmas <- wg_words %>%
  select(uni_lemma) %>%
  distinct() %>%
  arrange(uni_lemma)
gs_ws_new(uni_sheet, ws_title = "Bank", input = uni_lemmas)
