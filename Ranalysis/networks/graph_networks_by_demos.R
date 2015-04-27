graph_networks_by_demos <- function(demo,type="threshold"){
  
  if(type == "weighted") {
    age.demo.coeffs <- child.data %.%
      select(-id) %.%
      regroup(c("age",as.symbol(demo))) %.%
      summarise(mean = na.mean(w.coeffs),
                ci.h = ci.high(w.coeffs),
                ci.l = ci.low(w.coeffs))
    
    age.demo.diams <- child.data %.%
      select(-id) %.%
      regroup(c("age",as.symbol(demo))) %.%
      summarise(mean = na.mean(w.diams),
                ci.h = ci.high(w.diams),
                ci.l = ci.low(w.diams))
  }
  else {
    age.demo.coeffs <- child.data %.%
      select(-id) %.%
      regroup(c("age",as.symbol(demo))) %.%
      summarise(mean = na.mean(t.coeffs),
                ci.h = ci.high(t.coeffs),
                ci.l = ci.low(t.coeffs))
    
    age.demo.diams <- child.data %.%
      select(-id) %.%
      regroup(c("age",as.symbol(demo))) %.%
      summarise(mean = na.mean(t.diams),
                ci.h = ci.high(t.diams),
                ci.l = ci.low(t.diams))
  }
  
 
  age.demo.coeffs$measure <- "Clustering Coefficient"
  age.demo.diams$measure <- "Diameter"
  
  age.demo.measures <- rbind(age.demo.coeffs,age.demo.diams)
 # age.demo.measures <- factor(age.demo.measures$demo)
  
 quartz(width=8,height=3.5)
 p <- ggplot(age.demo.measures, 
             aes_string(x="age", y="mean",colour=demo,label=demo,
             fill=demo))+
   facet_wrap(~measure,scales="free") +
   geom_pointrange(aes(ymin =mean-ci.l,
                       ymax =mean+ci.h),
                   size = .8) +
   geom_line(size=1) +
   scale_x_continuous(breaks=seq(16,30,2),
                      limits=c(16,30.5),
                      name = "Age (months)")+
   scale_y_continuous(name = "Mean Measure Value") +
   theme_bw(base_size=14) + 
   theme(legend.position="none") +
   scale_colour_brewer(palette="Set1") +
   geom_dl(method=list("last.qp",cex=1,dl.trans(x=x+0.2)))
 
 print(p)
 
 return(age.demo.measures)
  
#   age.gender.coeffs <- child.data %.%
#     select(-id) %.%
#     group_by(age,gender) %.%
#     summarise(age.mean = na.mean(coeffs),
#               ci.h = ci.high(coeffs),
#               ci.l = ci.low(coeffs))
#   age.gender.coeffs$graph.type = "Full"

#   age.gender.p.coeffs <- child.data %.%
#     select(-id) %.%
#     group_by(age,gender) %.%
#     summarise(age.mean = na.mean(p.coeffs),
#               ci.h = ci.high(p.coeffs),
#               ci.l = ci.low(p.coeffs))
#   age.gender.p.coeffs$graph.type = "Perceptual"
#   
#   age.gender.all.coeffs <- rbind(age.gender.coeffs,age.gender.c.coeffs,
#                                  age.gender.p.coeffs)

#   age.gender.diams <- child.data %.%
#     select(-id) %.%
#     group_by(age,gender) %.%
#     summarise(age.mean = na.mean(diameters),
#               ci.h = ci.high(diameters),
#               ci.l = ci.low(diameters))
#   age.gender.diams$graph.type = "Full"

#   age.gender.p.diams <- child.data %.%
#     select(-id) %.%
#     group_by(age,gender) %.%
#     summarise(age.mean = na.mean(p.diameters),
#               ci.h = ci.high(p.diameters),
#               ci.l = ci.low(p.diameters))
#   age.gender.p.diams$graph.type = "Perceptual"
#   
#   age.gender.all.diams <- rbind(age.gender.diams,age.gender.c.diams,
#                                 age.gender.p.diams)
}

