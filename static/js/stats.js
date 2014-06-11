d3.json('static/json/stats.json', function(data_json) {

var data = crossfilter(data_json);
var all = data.groupAll();

// var sourceChart = dc.rowChart('#sourceChart')
// var ethnicityChart = dc.rowChart('#ethnicityChart')

var ageChildChart = dc.barChart('#ageChildChart');
var instrumentsChart = dc.pieChart('#instrumentsChart');
var genderChart = dc.pieChart('#genderChart');

//var ageChart = dc.lineChart('#ageChart');
//var ageChartRange = dc.barChart('#ageChartRange');

var wgMeanProductionChart = dc.lineChart('#wgMeanProductionChart');
var wgMeanComprehensionChart = dc.lineChart('#wgMeanComprehensionChart');
var wsMeanProductionChart = dc.lineChart('#wsMeanProductionChart');
// var ageChartRange = dc.barChart('#ageChartRange');

// var ageComprehensionChart = dc.lineChart('#ageComprehensionChart');
// var ageComprehensionChartRange = dc.barChart('#ageComprehensionChartRange');

// var momedChart = dc.lineChart('#momedChart');
// var momedChartRange = dc.barChart('#momedChartRange');
// var momedComprehensionChart = dc.lineChart('#momedComprehensionChart');
// var momedComprehensionChartRange = dc.barChart('#momedComprehensionChartRange');

// var ageMedianProductionChart = dc.lineChart('#ageMedianProductionChart');
// var ageMedianProductionChartRange = dc.barChart('#ageMedianProductionChartRange');
// var ageMedianComprehensionChart = dc.lineChart('#ageMedianComprehensionChart');
// var ageMedianComprehensionChartRange = dc.barChart('#ageMedianComprehensionChartRange');

var lineChartWidth = 500;
var pieChartWidth = 260;
var pieChartRadius = 100;

var reduceAdd = function(p, v) {
  ++p.count;
  p.production += v['production'];
  p.comprehension += v['comprehension'];
  return p;
};
var reduceRemove = function(p, v) {
  --p.count;
  p.production -= v['production'];
  p.comprehension -= v['comprehension'];
  return p;
};
var reduceInitial = function() {
  return {count: 0, production: 0, comprehension: 0};
};
var medianInitial = function() {
  return {count: 0, productions: [], comprehensions: []};
}
var medianAdd = function(p, v) {
  p.count++;
  p.productions.push(v['production']);
  p.comprehensions.push(v['comprehension']);
  return p;
}
var medianRemove = function(p, v) {
  p.count--;
  p.productions.splice(p.productions.length - 1, 1);
  p.comprehensions.splice(p.comprehensions.length - 1, 1);
  return p;
}

// var ethnicities = data.dimension(function(d) {
//   return d['ethnicity']
// });
// var ethnicitiesGroup = ethnicities.group().reduceSum(function(d) {
//   return 1;
// });
// var sources = data.dimension(function(d) {
//   return d['source'];
// });
// var sourcesGroup = sources.group().reduceSum(function(d) {
//   return 1;
// });

var ages = data.dimension(function(d) {
  return d['age'];
});
var ageChild = data.dimension(function(d) {
  return d['age'];
});
var agesGroup = ages.group().reduce(reduceAdd, reduceRemove, reduceInitial);
// var agesMedianGroup = ages.group().reduce(medianAdd, medianRemove, medianInitial);
var ageChildGroup = ageChild.group().reduceSum(function(d) {
  return 1;
});
var instruments = data.dimension(function(d) {
  return d['instrument'];
});
var instrumentsGroup = instruments.group().reduceSum(function(d) {
  return 1;
});
var genders = data.dimension(function(d) {
  return d['gender'];
});
var gendersGroup = genders.group().reduceSum(function(d) {
  return 1;
});
var momeds = data.dimension(function(d) {
  return d['mom_ed'];
});
var momedsGroup = momeds.group().reduce(reduceAdd, reduceRemove, reduceInitial);

genderChart.width(pieChartWidth)
        .height(320)
        .radius(pieChartRadius)
        .dimension(genders)
        .group(gendersGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

instrumentsChart.width(pieChartWidth)
        .height(320)
        .radius(pieChartRadius)
        .dimension(instruments)
        .group(instrumentsGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)


ageChildChart.width(lineChartWidth)
             .height(300)
             .margins({top: 20, right: 40, bottom: 32, left: 40})
             .dimension(ages)
             .group(ageChildGroup)
             .centerBar(true)
             .elasticY(true)
             .gap(1)
             .x(d3.scale.linear().domain([7,30.5]))
             .xAxisLabel('Age (months)')
             .yAxisLabel('Number of Children')
             .valueAccessor(function (d) {
               return d.value;
             });

wgMeanProductionChart.renderArea(true)
        .width(lineChartWidth)
        .height(300)
        .transitionDuration(1000)
        .margins({top: 30, right: 50, bottom: 25, left: 80})
        .dimension(ages)
        .mouseZoomable(false)
        .x(d3.scale.linear().domain([8,18]))
        //.rangeChart(ageChartRange)
        //.round(d3.time.month.round)
        //.xUnits(d3.time.months)
        .elasticY(false)
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
          return d.value.count > 0 ? d.value.production / d.value.count : 0;
        })

wgMeanComprehensionChart.renderArea(true)
        .width(lineChartWidth)
        .height(300)
        .transitionDuration(1000)
        .margins({top: 30, right: 50, bottom: 25, left: 80})
        .dimension(ages)
        .mouseZoomable(false)
        .x(d3.scale.linear().domain([8,18]))
        //.rangeChart(ageChartRange)
        //.round(d3.time.month.round)
        //.xUnits(d3.time.months)
        .elasticY(false)
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
          return d.value.count > 0 ? d.value.comprehension / d.value.count : 0;
        })

wsMeanProductionChart.renderArea(true)
        .width(lineChartWidth)
        .height(300)
        .transitionDuration(1000)
        .margins({top: 30, right: 50, bottom: 25, left: 80})
        .dimension(ages)
        .mouseZoomable(false)
        .x(d3.scale.linear().domain([16,30]))
        //.rangeChart(ageChartRange)
        //.round(d3.time.month.round)
        //.xUnits(d3.time.months)
        .elasticY(false)
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
          return d.value.count > 0 ? d.value.production / d.value.count : 0;
        })



// ageChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 80})
//         .dimension(ages)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([7,31]))
//         //.rangeChart(ageChartRange)
//         //.round(d3.time.month.round)
//         //.xUnits(d3.time.months)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)

//         .group(agesGroup)
//         .valueAccessor(function (d) {
//           return d.value.count > 0 ? d.value.production / d.value.count : 0;
//         })

// ageChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 80})
//         .dimension(ageChild)
//         .group(agesGroup)
//         .x(d3.scale.linear().domain([7,31]))
//         .centerBar(true)
//         .gap(1)
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.production / d.value.count : 0;
//         })
//         .yAxis().ticks(0);
//         //.round(d3.time.month.round)
//         //.alwaysUseRounding(true)
//         //.xUnits(d3.time.months);

// ageComprehensionChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 80})
//         .dimension(ages)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .rangeChart(ageComprehensionChartRange)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)

//         .group(agesGroup)
//         .valueAccessor(function (d) {
//           return d.value.count > 0 ? d.value.comprehension / d.value.count : 0;
//         });

// ageComprehensionChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 80})
//         .dimension(ages)
//         .group(agesGroup)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .centerBar(true)
//         .gap(1)
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.comprehension / d.value.count : 0;
//         })
//         .yAxis().ticks(0);

// ageMedianProductionChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 80})
//         .dimension(ages)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .rangeChart(ageMedianProductionChartRange)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)

//         .group(agesMedianGroup)
//         .valueAccessor(function (d) {
//           return d.value.productions.sort()[Math.floor(d.value.count/2)];
//         });

// ageMedianProductionChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 80})
//         .dimension(ages)
//         .group(agesMedianGroup)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .centerBar(true)
//         .gap(1)
//         .valueAccessor(function (d) {
//           return d.value.productions.sort()[Math.floor(d.value.count/2)];
//         })
//         .yAxis().ticks(0);


// ageMedianComprehensionChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 80})
//         .dimension(ages)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .rangeChart(ageMedianComprehensionChartRange)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)

//         .group(agesMedianGroup)
//         .valueAccessor(function (d) {
//           return d.value.comprehensions.sort()[Math.floor(d.value.count/2)];
//         });

// ageMedianComprehensionChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 80})
//         .dimension(ages)
//         .group(agesMedianGroup)
//         .x(d3.scale.linear().domain([7.5,30.5]))
//         .centerBar(true)
//         .gap(1)
//         .valueAccessor(function (d) {
//           return 1;
//           return d.value.comprehensions.sort()[Math.floor(d.value.count/2)];
//         })
//         .yAxis().ticks(0);


// momedChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 100})
//         .dimension(momeds)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([0,18]))
//         .rangeChart(momedChartRange)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)
//         .group(momedsGroup)
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.production / d.value.count : 0;
//         })

// momedChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 100})
//         .dimension(momeds)
//         .group(momedsGroup)
//         .centerBar(true)
//         .gap(1)
//         .x(d3.scale.linear().domain([0,18]))
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.production / d.value.count : 0;
//         })
//         .yAxis().ticks(0);

// momedComprehensionChart.renderArea(true)
//         .width(lineChartWidth)
//         .height(300)
//         .transitionDuration(1000)
//         .margins({top: 30, right: 50, bottom: 25, left: 100})
//         .dimension(momeds)
//         .mouseZoomable(false)
//         .x(d3.scale.linear().domain([0,18]))
//         .rangeChart(momedChartRange)
//         .elasticY(true)
//         .renderHorizontalGridLines(true)
//         .brushOn(false)
//         .group(momedsGroup)
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.comprehension / d.value.count : 0;
//         })

// momedComprehensionChartRange.width(lineChartWidth)
//         .height(40)
//         .margins({top: 0, right: 40, bottom: 20, left: 100})
//         .dimension(momeds)
//         .group(momedsGroup)
//         .centerBar(true)
//         .gap(1)
//         .x(d3.scale.linear().domain([0,18]))
//         .valueAccessor(function (d) {
//             return d.value.count > 0 ? d.value.comprehension / d.value.count : 0;
//         })
//         .yAxis().ticks(0);


// ethnicityChart.width(lineChartWidth)
//         .height(300)
//         .dimension(ethnicities)
//         .group(ethnicitiesGroup)
//         .label(function (d) {
//             return d.key + ": " + d.value;
//         })
//         .renderLabel(true)
//         .transitionDuration(500)


// sourceChart.width(lineChartWidth)
//              .height(300)
//              .margins({top: 0, right: 40, bottom: 20, left: 30})
//              .dimension(sources)
//              .group(sourcesGroup)
//              .gap(1)
//              .label(function (d) {
//                return d.key + ": " + d.value;
//              })
// 	     //.x(d3.scale.ordinal().domain(['Original Norming data', 'San Diego State University', 'University of Wisconsin', 'UT Dallas', 'San Diego State University', 'Louisiana State University', 'University of Connecticut', 'University of California']))
//              .valueAccessor(function (d) {
//                return d.value;
//              });


dc.renderAll();
});
