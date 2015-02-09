d3.json('static/json/stats.json', function(data_json) {

var data = crossfilter(data_json);
var all = data.groupAll();

var sourceChart = dc.rowChart('#sourceChart')
var ethnicityChart = dc.rowChart('#ethnicityChart')

var ageChildChart = dc.barChart('#ageChildChart');
//var languagesChart = dc.pieChart('#languagesChart');
var instrumentsChart = dc.pieChart('#instrumentsChart');
var genderChart = dc.pieChart('#genderChart');

var languagesChart = d3.layout.pack()
    .sort(null)
    .size()

var lineChartWidth = 400;
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

var ethnicities = data.dimension(function(d) {
  return d['ethnicity']
});
var ethnicitiesGroup = ethnicities.group().reduceSum(function(d) {
  return 1;
});

var sources = data.dimension(function(d) {
  return d['source'];
});
var sourcesGroup = sources.group().reduceSum(function(d) {
  return 1;
});

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

var genders = data.dimension(function(d) {
  return d['sex'];
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
//	    .x(d3.scale.ordinal().domain(['Male','Female','Unknown']))
        .renderLabel(true)
        .transitionDuration(500)

languagesChart.width(pieChartWidth)
        .height(320)
        .radius(pieChartRadius)
        .dimension(languages)
        .group(languagesGroup)
        .label(function (d) {
            return d.key + ":\n" + d.value;
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

ethnicityChart.width(lineChartWidth)
        .height(300)
        .dimension(ethnicities)
        .group(ethnicitiesGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

sourceChart.width(lineChartWidth)
             .height(300)
             .margins({top: 0, right: 40, bottom: 20, left: 30})
             .dimension(sources)
             .group(sourcesGroup)
             .gap(1)
             .label(function (d) {
               return d.key + ": " + d.value;
             })
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
        // .elasticY(true)
        .y(d3.scale.linear().domain([0, 396]))
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
	    instruments.filter("WG")
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
        // .elasticY(true)
        .y(d3.scale.linear().domain([0, 396]))
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
	    instruments.filter("WG")
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
        // .elasticY(true)
        .y(d3.scale.linear().domain([0, 680]))
        .renderHorizontalGridLines(true)
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
	    instruments.filter("WS")
            return d.value.count > 0 ? d.value.production / d.value.count : 0;
        })

dc.renderAll();
});
