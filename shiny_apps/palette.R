colors <- c('magenta' = '#d33682',
            'red' = '#dc322f',
            'orange' = '#cb4b16',
            'yellow' = '#b58900',
            'green' = '#859900',
            'cyan' = '#2aa198',
            'blue' = '#268bd2',
            'violet' = '#6c71c4',
            'purple' = '#993399')

color_order <- c('blue', 'orange', 'green', 'purple', 'magenta', 'yellow', 'cyan', 'violet', 'red')


color_palette <- function(n) {
  
  color_set <- function(k, set) {
    if (k == 0) {
      return(set)
    } else {
      return(c(color_set(k - 1, set), color_order[k]))
    }
  }
  
  palette <- colors[Filter(function(color) color %in% color_set(n, c()), names(colors))]
  names(palette) <- NULL
  return(palette)
}


ggplot(data(), aes(x = age, y = vocab)) +
  geom_jitter(width = 0.1, size = 1, color = pt.color) +
  scale_x_continuous(name = "\nAge (months)",
                     breaks = seq(age.min(), age.max(), by = 2),
                     limits=c(age.min(), age.max())) +
  #ylab(paste(ylabel(), "\n", sep = "")) +
#  scale_colour_brewer(#name = color.legend.name(),
#                      palette = seq.palette) +
  scale_color_manual(values = rev(color_palette(length(unique(curves()$quantile))))) +
  theme(text=element_text(family=font)) +
  geom_line(data = curves(), size = 1, 
            aes(x = age, y = predicted, color = quantile)) +
  facet_wrap(~ demo)