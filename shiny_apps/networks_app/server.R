library(shiny)
library(RMySQL)
library(dplyr)
library(ggplot2)
library(tidyr)
library(stringr)
library(igraph)
library(bootstrap)
library(directlabels)
source("../app_themes.R")

## NA functions
na.mean <- function(x) {mean(x,na.rm=T)}

## for bootstrapping 95% confidence intervals
theta <- function(x,xdata,na.rm=T) {mean(xdata[x],na.rm=na.rm)}
ci.low <- function(x,na.rm=T) {
  mean(x,na.rm=na.rm) - quantile(bootstrap(1:length(x),1000,theta,x,na.rm=na.rm)$thetastar,.025,na.rm=na.rm)}
ci.high <- function(x,na.rm=T) {
  quantile(bootstrap(1:length(x),1000,theta,x,na.rm=na.rm)$thetastar,.975,na.rm=na.rm) - mean(x,na.rm=na.rm)}

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
  filter(age >= 16 & age <= 30, gender == "M"| gender == "F") %>%
  select(-child.id,-source.id) #drop redundant columns

#Find all indices of ws.data that point to cdi words
first.ind <- which(names(ws.data)=="alligator")
last.ind <- which(names(ws.data)=="house")

c.weighted.graphs <- sapply(1:nrow(ws.data),
                            function(c){make.weighted.graph(c,c.assoc.mat,
                                                            first.ind,
                                                            last.ind)})


coeffs <- lapply(c.weighted.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,transitivity(x))})
ws.data$coeff <- sapply(coeffs,function(x){unlist(x)[1]})

diams <- lapply(c.weighted.graphs,
                  FUN=function(x){ifelse(is.na(x),NA,diameter(x))})
ws.data$diam <- sapply(diams,function(x){unlist(x)[1]})

network.stats <- ws.data %>%
  select(id,age,gender,mom_ed,birth_order,coeff,diam)

network.stats$birth_order <- ifelse(network.stats$birth_order == 1, 
                                    "First Born",
                                   "Later Born")
network.stats$mom_ed = cut(network.stats$mom_ed, 
                           breaks = c(0,11.5,15.5,16.5,20),
                           labels = c("Primary School","Highschool",
                                      "College", "Graduate School"))

shinyServer(function(input, output) {
  
  output$plot <- renderPlot({
    
    measure.var <- input$n.measure
    demo.var <- input$demo.var
    
    data <- eval(substitute(mutate(network.stats, 
                                   demo.var = demo.var.name,
                                   measure.var = measure.var.name),
                                 list(demo.var.name = as.name(demo.var),
                                      measure.var.name = as.name(measure.var))))
    data <- data %>%
      group_by(age,demo.var) %>%
      summarise_each(funs(na.mean,ci.high,ci.low),c(measure.var))
    
    ggplot(data, aes(x=age, y=na.mean,colour=demo.var,label=demo.var,
                      fill=demo.var))+
      geom_pointrange(aes(ymin =na.mean-ci.low,
                          ymax =na.mean+ci.high),
                      size = .8) +
      geom_line(size=1) +
      scale_x_continuous(breaks=seq(16,30,2),
                         limits=c(16,30.5),
                         name = "Age (months)")+
      scale_y_continuous(name = "Mean Measure Value") +
      theme_bw(base_size=14) + 
      theme(legend.title=element_blank()) +
      scale_colour_brewer(palette="Set1") 
  })
  
})
