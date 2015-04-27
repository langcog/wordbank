library(igraph)

#load graphing function for examining network measures by demographics
source("graph_networks_by_demos.R") 

# Make an unweighted graph from feature overlap with a set threshold
make.threshold.graph <- function(c,mat,thresh){
  c.mat <- mat[which(mcrae.vocab[c,2:ncol(mcrae.vocab)]==1),
                     which(mcrae.vocab[c,2:ncol(mcrae.vocab)]==1)]   
  
  if(length(c.mat) <2)
    return(NA)
  
  c.mat[c.mat < thresh] <- 0
  c.mat[c.mat >= thresh] <- 1
  
  if(sum(c.mat) < 1)
    return(NA)
  else
    return(graph.adjacency(as.matrix(c.mat),mode="undirected"))
}

# Make an weighted graph from feature overlap
make.weighted.graph <- function(c,mat){
  
  c.mat <- mat[which(mcrae.vocab[c,2:ncol(mcrae.vocab)]==1),
               which(mcrae.vocab[c,2:ncol(mcrae.vocab)]==1)]   
  
  if(length(c.mat) < 2)
    return(NA)
  else
    return(graph.adjacency(as.matrix(c.mat),mode="undirected",weighted=TRUE))
}


mcrae.words <- read.csv(file= "mcrae.words.csv")

# grab the subset of cdi data for the mcrae words + child id
mcrae.names <- mcrae.words[mcrae.words$McRae.word == 1,"English.label"]
mcrae.vocab <- vocab.words[,c(1,which(mcrae.words$McRae.word == 1) + 1)]

# make graphs for each kid using the conceptual McRae network
c.assoc.mat <- as.data.frame(read.csv(file = "c_assoc_mat.csv"))

# make a graph for the conceptual McRae Network and plot it
c.assoc.graph <- graph.adjacency(as.matrix(c.assoc.mat),
                                 mode="undirected",weighted=TRUE)
quartz(width=7,height=7)
plot(c.assoc.graph,vertex.size=.01,vertex.label.cex=.8,
     layout=layout.fruchterman.reingold(c.assoc.graph, niter=10000, 
                                        area=40*vcount(c.assoc.graph)^2),
     edge.width=E(c.assoc.graph)$weight)

# Make both thresholded and weighted graphs for all children
c.thresh.graphs <- sapply(1:nrow(mcrae.vocab),
                          function(c){make.threshold.graph(c,c.assoc.mat,2)})
c.weighted.graphs <- sapply(1:nrow(mcrae.vocab),
                            function(c){make.weighted.graph(c,c.assoc.mat)})

# append clustering coefficients to child data
t.coeffs <- lapply(c.thresh.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,transitivity(x))})
w.coeffs <- lapply(c.weighted.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,transitivity(x))})
child.data$t.coeffs <- sapply(t.coeffs,function(x){unlist(x)[1]})
child.data$w.coeffs <- sapply(w.coeffs,function(x){unlist(x)[1]})

# append diameters to child data
t.diams <- lapply(c.thresh.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,diameter(x))})
w.diams <- lapply(c.weighted.graphs,
                   FUN=function(x){ifelse(is.na(x),NA,diameter(x))})
child.data$t.diams <- sapply(t.diams,function(x){unlist(x)[1]})
child.data$w.diams <- sapply(w.diams,function(x){unlist(x)[1]})

age.gender.measures <- graph_networks_by_demos(demo="gender",type="weighted")
