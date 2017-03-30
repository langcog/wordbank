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

ggplot(d, 
       aes(x = age, y = comprehension)) + 
  # geom_point() + 
  geom_line(data = preds, aes(x = age, y = pred, col = percentile, group = percentile)) + 
  ylim(0,400) + 
  xlim(7,19) + 
  ylab("Vocab") + 
  xlab("Age") + 
  scale_color_discrete(guide=FALSE) + 
  theme_xkcd()