library(shiny)
library(RMySQL)
library(dplyr)
library(ggplot2)
library(tidyr)
library(stringr)
library(igraph)

source("../app_themes.R")

## Load McRae word list
mcrae.words <- read.csv("mcrae.words.csv",stringsAsFactors=FALSE) %>%
  filter(McRae.word == 1) %>%
  select(-McRae.word)

# Load McRae conceptual feature association network
c.assoc.mat <- as.data.frame(read.csv(file = "c_assoc_mat.csv"))

# Make an weighted graph from feature overlap
make.weighted.graph <- function(c,mat,first.ind,last.ind){
  c.mat <- mat[as.logical(ws.data[c,first.ind:last.ind]),
               as.logical(ws.data[c,first.ind:last.ind])]
  if(length(c.mat) < 2)
    return(NA)
  else
    return(graph.adjacency(as.matrix(c.mat),mode="undirected",weighted=TRUE))
}

# Open database connection
wordbank <- src_mysql(dbname='wordbank',host="54.200.225.86", 
                      user="wordbank",password="wordbank")

# Load relevant tables
admin.table <- tbl(wordbank,"common_administration")
child.table <- tbl(wordbank,"common_child")
ws.table <- tbl(wordbank,"instruments_ws")

# Select just the MCDI words in the McRae set
ws.vocab.words <- as.data.frame(select(ws.table,
                                       basetable_ptr_id,
                                       col_baabaa:col_connthen)) %>%
  rename(id = basetable_ptr_id) %>%# Rename the id
  select(id,one_of(mcrae.words$col.name)) #grab just the mcRae words

# Relabel names to be English-readable
names(ws.vocab.words)[2:length(ws.vocab.words)] <- 
        sapply(names(ws.vocab.words)[2:length(ws.vocab.words)], 
               function(w) mcrae.words[
                 which(mcrae.words$col.name == w),"English.label"],
               USE.NAMES = FALSE)

# Get the age of each child
admins <- admin.table %>%
  select(data_id,child_id,age,source_id) %>%
  rename(id = data_id, child.id = child_id,source.id = source_id) 
admins <- as.data.frame(admins)

# Get demographic variables for each child
demos <- select(child.table,id,gender,mom_ed,birth_order) %>%
  rename(child.id = id) # Rename id fields
demos <- as.data.frame(demos)

# Join age and demographics together
child.data <- as.tbl(left_join(admins,demos))

# Join demographics to production data
ws.data <- left_join(ws.vocab.words, child.data) %>%
  filter(age >= 16 & age <= 30) %>% # Just the original norming data
  select(-child.id,-source.id) #drop redundant columns

#Find all indices of ws.data that point to cdi words
first.ind <- which(names(ws.data)=="alligator")
last.ind <- which(names(ws.data)=="house")

c.weighted.graphs <- system.time(sapply(1:nrow(ws.data),
                            function(c){make.weighted.graph(c,c.assoc.mat,
                                                            first.ind,
                                                            last.ind)}))


coeffs <- lapply(c.weighted.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,transitivity(x))})
ws.data$coeff <- sapply(coeffs,function(x){unlist(x)[1]})

diams <- lapply(c.weighted.graphs,
                  FUN=function(x){ifelse(is.na(x),NA,diameter(x))})
ws.data$diam <- sapply(diams,function(x){unlist(x)[1]})

shinyServer(function(input, output) {
  
  n.measure <- input$n.measure
  demo.var <- input$demo.var
  
  network.stats <- ws.data %>%
    regroup(c("age",as.symbol(demo.var))) %.%
  
  ddd <- kid.words %>% 
    filter(!is.na(vocab), 
           instrument == input$instrument) %>% 
    filter(age == input$age) %>%
    group_by(age) %>%
    mutate(p = rank(vocab)/length(vocab),
           q = cut(p, breaks=cuts, 
                   labels=cuts[2:length(cuts)]-qs/2))
  
  output$plot <- renderPlot({
    with(subset(wordle.data, wordle.data$age==input$age),
         wordcloud_rep(word,floor(vocab*100),
                       scale=c(1.5,.02),
                       min.freq = input$freq, 
                       max.words=input$max,
                       colors=brewer.pal(8, "Dark2")))
  })
  
})
