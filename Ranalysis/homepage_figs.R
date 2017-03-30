# to get this to work
# 1. run this:
#    download.file("http://simonsoftware.se/other/xkcd.ttf", dest="~/Desktop/xkcd.ttf", mode="wb")
# 2. double click on font file and hit install
# 3. run:
#    font_import(pattern = "xkcd", prompt=FALSE)

source("../shiny_apps/vocab_norms/predictQR_fixed.R")
library(tidyverse)
library(quantregGrowth)
library(wordbankr)
library(xkcd)

d <- get_administration_data(language = "English", form = "WG")

taus <-  c(0.1, 0.25, 0.5, 0.75, 0.9)

mod <- gcrq(formula = comprehension ~ ps(age, monotone = 1, lambda = 1000), 
            tau = taus, data = d)

ages <- 8:18
newdata <- data.frame(age = ages)

preds <- predictQR_fixed(mod, newdata = newdata) %>%
  data.frame %>%
  mutate(age = ages) %>%
  gather(percentile, pred, starts_with("X")) %>%
  mutate(percentile = as.character(as.numeric(str_replace(percentile, "X", "")) * 100))

ggplot(preds, aes(x = age, y = pred)) + 
  geom_line(aes(col = percentile)) + 
  ylab("VOCAB") + 
  xkcdaxis(xrange = c(7,19), yrange = c(0,400)) + 
  theme_xkcd() + 
  theme(axis.line.x = element_line(colour="white"), 
        panel.border = element_rect(size= 0, colour = "white"))



