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
  
#   color_set <- function(k, set) {
#     if (k == 0) {
#       return(set)
#     } else {
#       return(c(color_set(k - 1, set), color_order[k]))
#     }
#   }
  
#  palette <- colors[Filter(function(color) color %in% color_set(n, c()), names(colors))]
  palette <- colors[Filter(function(color) color %in% color_order[1:n], names(colors))]  
  names(palette) <- NULL
  return(palette)
}