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
library(visNetwork)
library(stringr)

theme_set(theme_mikabr(base_size = 14))
font <- theme_mikabr()$text$family

######## DATA PROCESSING
c_assocs <- read_csv(file = "assocs/c_assoc_mat.csv") 
p_assocs <- read_csv(file = "assocs/p_assoc_mat.csv")
all_assocs <- read_csv(file = "assocs/assoc_mat.csv")

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

  ########## READ IN AOAS
  aoa_data <- reactive({
    if (input$instrument  == "WS") {
      raw_aoas <- ws_aoas
    } else if (input$instrument == "WG" & input$measure == "comprehension" ) {
      raw_aoas <- wg_comp_aoas
    }else if (input$instrument == "WG" & input$measure == "production" ) {
      raw_aoas <- wg_prod_aoas
    }
     
    raw_aoas %>%
      rename(label = definition) %>% 
      mutate(aoa = round(aoa))  
  })  
  
  ########## READ IN ASSOCIATIONS
  assoc_mat <- reactive({
    if (input$assocs == "conceptual") {
      assocs <- c_assocs 
    } else if (input$assocs == "perceptual") {
      assocs <- p_assocs
    } else if (input$assocs == "all") {
      assocs <- all_assocs
    }
    
    assoc_mat <- as.matrix(select(assocs, -in_node))
    assoc_mat[lower.tri(assoc_mat)] <- NA
    
    data.frame(assoc_mat, 
               in_node = assocs$in_node, 
               stringsAsFactors = FALSE)
  })
  
  ########## FILTER NODE DATA
  assoc_nodes <- reactive({
    # aoa_labels <- filter(aoa_data, aoa <= input$age)$label
    
    assoc_nodes <- data.frame(label = assoc_mat()$in_node, 
                              stringsAsFactors = FALSE) %>%
      mutate(id = 1:n(), 
             identity = 1) %>%
      left_join(aoa_data()) %>%
      filter(!is.na(aoa), aoa <= input$age) %>%
      select_("label", "id", input$group) %>%
      rename_("group" = input$group)
  })
  
  ########## PARSE EDGE DATA
  assoc_edge_data <- reactive({
    # get the matrix in an id-based form
    assoc_mat() %>%
      gather(out_node, width, -in_node) %>%
      filter(!is.na(width)) %>%
      rename(label = in_node) %>%
      left_join(assoc_nodes()) %>%
      select(-label) %>%
      rename(in_node = id, 
             label = out_node) %>%
      left_join(assoc_nodes()) %>%
      select(-label) %>%
      rename(out_node = id) %>%
      select(in_node, out_node, width)
  })
  
  ########## FILTER EDGES 
  assoc_edges <- reactive({
    req(input$weighted)
    
    #print(assoc_nodes())
    
    edges <- assoc_edge_data() %>%
      filter(width >= input$cutoff) 
    
    if (input$weighted == "TRUE") {
      edges
    } else {
      edges %>% select(-width) 
    }
  })
  
  ########## RENDER GRAPH
  output$network <- renderVisNetwork({
    
    
    
    visNetwork(assoc_nodes(), 
               rename(assoc_edges(), from = in_node, to = out_node), 
               width = "100%", height="100%") %>%
      visPhysics(stabilization = TRUE) %>%
      visEdges(smooth = FALSE)
    
  })
  
  output$loaded <- reactive(1)
})

