d3.json('static/json/stats.json', function(data_json) {

var data = crossfilter(data_json);
var all = data.groupAll();

var ageChildChart = dc.barChart('#ageChildChart');

var languagesChart = dc.pieChart('#languagesChart');
var instrumentsChart = dc.pieChart('#instrumentsChart');

var sexChart = dc.pieChart('#sexChart');
var ethnicityChart = dc.rowChart('#ethnicityChart')
var momedChart = dc.rowChart('#momedChart')

var lineChartWidth = 400;
var pieChartWidth = 200;
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

var ages = data.dimension(function(d) {
  return d['age'];
});
var ageChild = data.dimension(function(d) {
  return d['age'];
});
var agesGroup = ages.group().reduce(reduceAdd, reduceRemove, reduceInitial);
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

var ethnicities = data.dimension(function(d) {
  return d['ethnicity']
});
var ethnicitiesGroup = ethnicities.group().reduceSum(function(d) {
  return 1;
});

var momeds = data.dimension(function(d) {
  return d['mom_ed'];
});
//var momedsGroup = momeds.group().reduce(reduceAdd, reduceRemove, reduceInitial);
var momedsGroup = momeds.group().reduceSum(function(d) {
  return 1;
});

ageChildChart.width(600)
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

languagesChart.width(pieChartWidth)
        .height(pieChartWidth)
        .radius(pieChartRadius)
        .dimension(languages)
        .group(languagesGroup)
        .label(function (d) {
              return d.key;
//            return d.key + ":\n" + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

instrumentsChart.width(pieChartWidth)
        .height(pieChartWidth)
        .radius(pieChartRadius)
        .dimension(instruments)
        .group(instrumentsGroup)
        .label(function (d) {
              return d.key;
//            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

sexChart.width(pieChartWidth)
        .height(pieChartWidth)
        .radius(pieChartRadius)
        .dimension(sexes)
        .group(sexesGroup)
        .label(function (d) {
              return d.key;
//            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

ethnicityChart.width(lineChartWidth)
        .height(300)
        .dimension(ethnicities)
        .group(ethnicitiesGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)
        .xAxis().tickFormat(function(v) { return ""; })

momedChart.width(lineChartWidth)
        .height(300)
        .dimension(momeds)
        .group(momedsGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)
        .xAxis().tickFormat(function(v) { return ""; })

dc.renderAll();
});