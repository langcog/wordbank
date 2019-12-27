d3.json('static/json/stats.json', function(data_json) {

var data = crossfilter(data_json);
var all = data.groupAll();

var ageChildChart = dc.barChart('#ageChildChart');

var languagesChart = dc.rowChart('#languagesChart');
var instrumentsChart = dc.pieChart('#instrumentsChart');

var sexChart = dc.pieChart('#sexChart');
var momedChart = dc.rowChart('#momedChart')
var birthorderChart = dc.rowChart('#birthorderChart')

var pieChartWidth = 450;
var pieChartHeight = 300;
var pieChartRadius = 100;
var barAgeLanguageHeight = 450;

var ageChild = data.dimension(function(d) {
  return d['age'];
});
var ageChildGroup = ageChild.group().reduceSum(function(d) {
  return 1;
});

var languages = data.dimension(function(d) {
  return d['language'];
});
var languagesGroup = languages.group().reduceSum(function(d) {
  return 1;
});

var instruments = data.dimension(function(d) {
  return d['form'];
});
var instrumentsGroup = instruments.group().reduceSum(function(d) {
  return 1;
});

var sexes = data.dimension(function(d) {
  return d['sex'];
});
var sexesGroup = sexes.group().reduceSum(function(d) {
  return 1;
});

var momeds = data.dimension(function(d) {
  return d['mom_ed'];
});
var momedsGroup = momeds.group().reduceSum(function(d) {
  return 1;
});

var birthorders = data.dimension(function(d) {
  return d['birth_order'];
});
var birthordersGroup = birthorders.group().reduceSum(function(d) {
  return 1;
});

ageChildChart.width(700)
             .height(barAgeLanguageHeight)
             .margins({top: 20, right: 40, bottom: 32, left: 40})
             .dimension(ageChild)
             .group(ageChildGroup)
             .centerBar(true)
             .elasticY(true)
             .gap(1)
             .x(d3.scale.linear().domain([7,37]))
             .xAxisLabel('Age (months)')
             .yAxisLabel('Number of Children')
             .valueAccessor(function (d) {
               return d.value;
             });

momedChart.width(330)
        .height(250)
        .dimension(momeds)
//        .margins({top: 20, right: 40, bottom: 45, left: 40})
        .group(momedsGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)
//        .xAxis().tickFormat(function(v) { return ""; })
        .xAxis().ticks(5)
//        .xAxisLabel('')

birthorderChart.width(330)
        .height(250)
        .dimension(birthorders)
//        .margins({top: 20, right: 40, bottom: 45, left: 40})
        .group(birthordersGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)
//        .xAxis().tickFormat(function(v) { return ""; })
        .xAxis().ticks(5)
//        .xAxisLabel('')

languagesChart.width(400)
        .height(barAgeLanguageHeight)
        .dimension(languages)
        .margins({top: 20, right: 40, bottom: 45, left: 40})
        .group(languagesGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)
//        .xAxis().tickFormat(function(v) { return ""; })
        .xAxis().ticks(5)
//        .xAxisLabel('')

//languagesChart.width(pieChartWidth)
//        .height(pieChartWidth)
//        .radius(pieChartRadius)
//        .dimension(languages)
//        .group(languagesGroup)
//        .label(function (d) {
//              return d.key;
//            return d.key + ": " + d.value;
//        })
//        .renderLabel(true)
//        .transitionDuration(500)

instrumentsChart.width(pieChartWidth)
        .height(pieChartHeight)
        .radius(pieChartRadius)
        .dimension(instruments)
        .group(instrumentsGroup)
        .slicesCap(5)
        .label(function (d) {
//              return d.key;
            return d.key + ": " + d.value;
        })
        .externalLabels(25)
        .minAngleForLabel(0.1)
        .renderLabel(true)
        .transitionDuration(500)

sexChart.width(pieChartWidth)
        .height(pieChartHeight)
        .radius(pieChartRadius)
        .dimension(sexes)
        .group(sexesGroup)
        .label(function (d) {
//              return d.key;
            return d.key + ": " + d.value;
        })
        .externalLabels(25)
        .minAngleForLabel(0.1)
        .renderLabel(true)
        .transitionDuration(500)

dc.renderAll();
});
