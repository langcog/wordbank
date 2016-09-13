library(dplyr)
library(haven)
library(readr)
library(foreign)

mandarin <- read_spss("CCDI.BJ.LF.Toddler.TotalScores.sav")
cantonese <- read_spss("~/Documents/projects/wordbank_extras/incoming_data/Mandarin_Tardif/CCDI.HK.LF.Toddler.TotalScores.sav")
#cantonese2 <- read_spss("~/Documents/projects/wordbank_extras/incoming_data/Mandarin_Tardif/CCDI.HK.LF.Toddler.SayChiData.sav")
#cantonese3 <- read_spss("~/Documents/projects/wordbank_extras/incoming_data/Mandarin_Tardif/CCDI.HK.LF.Toddler.SayEngOrChiData.sav")

write.csv(mandarin, "~/Documents/projects/wordbank_extras/incoming_data/mandarin.csv", row.names = FALSE)
write.csv(cantonese, "~/Documents/projects/wordbank_extras/incoming_data/cantonese.csv", row.names = FALSE)

mandarin %>%
  mutate(sex = as.character(CHISEX)) %>%
  select(sex) %>%
  group_by(sex) %>%
  summarise(n = n())

names(cantonese)
length(names(cantonese))
length(names(cantonese2))
length(names(cantonese3))

definition = sapply(names(cantonese),
                    function(col) iconv(attributes(cantonese[[col]])$label, from = "BIG5HKSCS", to = "UTF8"))

cantonese_fields <- data.frame(item = names(cantonese),
                               definition = sapply(names(cantonese),
                                                   function(col) iconv(attributes(cantonese[[col]])$label,
                                                                       from = "BIG5HKSCS",
                                                                       to = "UTF8")),
                               row.names = NULL)

write_csv(cantonese_fields, "~/Documents/projects/wordbank/raw_data/Cantonese_WS/[Cantonese_WS].csv")

comp_items <- Filter(function(item) substr(item, 1, 4) == "COMP", names(cantonese))
comp_values = sapply(comp_items, function(col) attributes(cantonese[[col]])$labels)

cantonese_values = sapply(names(cantonese), function(col) attributes(cantonese[[col]])$labels)

write.csv(cantonese_values, "~/Documents/projects/wordbank/raw_data/Cantonese_WS/CantoneseWS_Tardif_values.csv")


# get_label <- function(col) attributes(cantonese[[col]])$label
# cantonese_items <- data.frame(item = names(cantonese)) %>%
#   rowwise() %>%
#   do(definition = get_label(item))



mandarin_fields <- data.frame(item = names(mandarin),
                              definition = sapply(names(mandarin),
                                                  function(col) attributes(mandarin[[col]])$label),
                              row.names = NULL)
mandarin_values = sapply(names(mandarin), function(col) attributes(mandarin[[col]])$labels)

write_csv(mandarin_fields, "~/Documents/projects/wordbank/raw_data/Mandarin_WS/[Mandarin_WS].csv")
