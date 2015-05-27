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
  num_cols <- length(color_order)
  palette <- c(rep.int(colors, n %/% num_cols),
               colors[Filter(function(color) color %in% color_order[0:(n %% num_cols)], names(colors))])
  names(palette) <- NULL
  return(palette)
}