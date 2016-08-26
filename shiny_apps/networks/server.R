# TODO
# - childes associations
# - cross-linguisic using unilemmas

library(shiny)
library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)
library(langcog)
library(wordbankr)
library(stringr)
library(networkD3)

theme_set(theme_mikabr(base_size = 14))
font <- theme_mikabr()$text$family

######## DATA PROCESSING
c_assocs <- read_csv(file = "assocs/c_assoc_mat.csv") 
p_assocs <- read_csv(file = "assocs/p_assoc_mat.csv")
all_assocs <- read_csv(file = "assocs/assoc_mat.csv")
w2v_assocs<- read_csv(file= 'assocs/w2v_assocs.csv')
# pb_assocs<- read_csv(file = 'assocs/books_word2vec.csv')

ws_aoas <- read_csv("aoas/eng_ws_production_aoas.csv") 
wg_comp_aoas <- read_csv("aoas/eng_wg_production_aoas.csv") 
wg_prod_aoas <- read_csv("aoas/eng_wg_comprehension_aoas.csv") 

###### SHINY SERVER ###### 

shinyServer(function(input, output) {
  output$loaded <- reactive(0)
  outputOptions(output, "loaded", suspendWhenHidden = FALSE)
  
  ########## GET MEASURE
  output$measure <- renderUI({
    req(input$instrument) 
    
    if (input$instrument == "WS") {
      choices <- c("Production" = "production")
    } else if (input$instrument == "WG") {
      choices <- c("Comprehension" = "comprehension", 
        "Production" = "production")
    }
    
    selectInput("measure", "AoA measure",
                   choices = choices,
                   selected = "production")
  })
  
  
  output$assoc_control <- renderUI({
    req(input$source)
    if(input$source == "MFN") {
    selectInput("assocs", "Association type",
              choices = c("Conceptual" = "conceptual", 
                          "Perceptual" = "perceptual", 
                          "All" = "all"),
              selected = "all")
    }
  })
  
  ####### CHOOSE A SCALE FOR CUTOFF
  output$cutoff <- renderUI({
    req(input$source)
    
    if (input$source == "W2V"){
      title <- "Minimum Cosine Similarity"
      high_point <- .2
      start_point <- .1
      low_point <- 0
      step_size <- .02
    # } else if (input$source == "PB"){
    #   title <- "Cosine Similarity"
    #   high_point <- 1
    #   start_point <- .6
    #   low_point <- -1
    #   step_size <- .1
    } else if (input$source == "MFN"){
      title <- "Number of Shared Features"
      high_point <- 4
      start_point <- 2
      low_point <- 1
      step_size <- 1
    }
  
    sliderInput("cutoff", label=title,
                  min = low_point, max = high_point, 
                  value = start_point, step = step_size)
  })

  ########## READ IN AOAS
  aoa_data <- reactive({
    
    req(input$source)
    
    if (input$instrument  == "WS") {
      raw_aoas <- ws_aoas
    } else if (input$instrument == "WG" & input$measure == "comprehension" ) {
      raw_aoas <- wg_comp_aoas
    }else if (input$instrument == "WG" & input$measure == "production" ) {
      raw_aoas <- wg_prod_aoas
    }
     
    if(input$source == "MFN") {
      raw_aoas %>%
        rename(label = definition) %>% 
        mutate(aoa = round(aoa))  
    }
    else {
      raw_aoas %>%
        rename(label = uni_lemma) %>% 
        mutate(aoa = round(aoa))  
    }
  })  
  
  ########## READ IN ASSOCIATIONS
  assoc_mat <- reactive({
    if (input$source == "MFR") {
      assocs <- all_assocs
    } else if (input$source == "W2V") {
        assocs <- w2v_assocs
    } else if (input$source == "PB") {
      assocs <- pb_assocs
    } else if (input$assocs == "conceptual") {
      assocs <- c_assocs 
    } else if (input$assocs == "perceptual") {
      assocs <- p_assocs
    } else if (input$assocs == "all") {
      assocs <- all_assocs
    }
    
    assoc_mat <- as.matrix(select(assocs, -in_node))
    assoc_mat[lower.tri(assoc_mat)] <- NA
    
    data.frame(assoc_mat, check.names = FALSE,
               in_node = assocs$in_node, 
               stringsAsFactors = FALSE)
  })
  
  ########## FILTER NODE DATA
  assoc_nodes <- reactive({
    # aoa_labels <- filter(aoa_data, aoa <= input$age)$label
    
    assoc_nodes <- data.frame(label = assoc_mat()$in_node, 
                              stringsAsFactors = FALSE) %>%
      left_join(aoa_data()) %>% #left_join in wide ? format version of english item csv with category
      filter(!is.na(aoa), aoa <= input$age) %>%
      mutate(id = 0:(n()-1), 
             identity = 1) %>%
      select_("label", "id", input$group) %>%
      rename_("group" = input$group)
  })
  
  ########## PARSE EDGE DATA
  assoc_edge_data <- reactive({
    nodes <- assoc_nodes()
    
    # get the matrix in an id-based form
    assoc_mat() %>%
      gather(out_node, width, -in_node) %>%
      filter(!is.na(width), in_node %in% nodes$label, 
             out_node %in% nodes$label) %>%
      rename(label = in_node) %>%
      left_join(nodes) %>%
      select(-label) %>%
      rename(in_node = id, 
             label = out_node) %>%
      select(label, width, in_node) %>%
      left_join(nodes) %>%
      select(-label) %>%
      rename(out_node = id) %>%
      select(in_node, out_node, width) %>%
      filter(in_node != out_node)
  })
      
  ########## FILTER EDGES 
  assoc_edges <- reactive({
    req(input$weighted)
    
    scaling = ifelse(input$source == "W2V", 10, 1)
    
    edges <- assoc_edge_data() %>%
      mutate(width = scaling*width) %>%
      filter(width >= (scaling*input$cutoff)) 
    
    if (input$weighted == "TRUE") {
      edges
    } else {
      edges %>% select(-width) 
    }
    
  })
  
  ########## RENDER GRAPH
  output$network <- renderForceNetwork({
    forceNetwork(Links = assoc_edges(), Nodes = assoc_nodes(), Source = "in_node",
                 Target = "out_node", Value = "width", NodeID = "label",
                 linkWidth = JS("function(d) { return d.value; }"),
                 Group = "group", opacity = .8, zoom = TRUE, opacityNoHover = .8,
                 legend = input$group != "identity",
                 linkColour = "#cccccc", fontSize = 12,
                 colourScale = ifelse(length(unique(assoc_nodes()$group)) > 10, 
                                      JS("d3.scale.category20()"),
                                      JS("d3.scale.category10()")))
  })
  
  # output$network <- renderVisNetwork({
  #   visNetwork(assoc_nodes(), 
  #              rename(assoc_edges(), from = in_node, to = out_node), 
  #              width = "100%", height="100%") %>%
  #     visPhysics(stabilization = TRUE) %>%
  #    visEdges(smooth = FALSE, selfReferenceSize= FALSE)
  #   
  # })
  
  output$loaded <- reactive(1)
})

