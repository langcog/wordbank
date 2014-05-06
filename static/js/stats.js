d3.json('static/json/stats.json', function(data_json) {

//var data_json = $.parseJSON($('#data').val());
var data = crossfilter(data_json);
var all = data.groupAll();
var ageChart = dc.lineChart('#ageChart'); 
var ageChartRange = dc.barChart('#ageChartRange');
var genderChart = dc.pieChart('#genderChart');
var momedChart = dc.lineChart('#momedChart'); 
var momedChartRange = dc.barChart('#momedChartRange');

var reduceAdd = function(p, v) {
  ++p.count;
  p.total += v['total'];
  return p;
};
var reduceRemove = function(p, v) {
  --p.count;
  p.total -= v['total'];
  return p;
};
var reduceInitial = function() {
  return {count: 0, total: 0};
};

var ages = data.dimension(function(d) {
  return d['age'];
});
var agesGroup = ages.group().reduce(reduceAdd, reduceRemove, reduceInitial);
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

ageChart.renderArea(true)
        .width(800)
        .height(300)
        .transitionDuration(1000)
        .margins({top: 30, right: 50, bottom: 25, left: 80})
        .dimension(ages)
        .mouseZoomable(false)
        .x(d3.scale.linear().domain([15,31]))
        .rangeChart(ageChartRange)
        //.round(d3.time.month.round)
        //.xUnits(d3.time.months)
        .elasticY(true)
        .renderHorizontalGridLines(true)
        //.legend(dc.legend().x(800).y(10).itemHeight(13).gap(5))
        .brushOn(false)

        .group(agesGroup)
        .valueAccessor(function (d) {
            return d.value.count > 0 ? d.value.total / d.value.count : 0;
        });

ageChartRange.width(800)
        .height(40)
        .margins({top: 0, right: 40, bottom: 20, left: 80})
        .dimension(ages)
        .group(agesGroup)
        .x(d3.scale.linear().domain([15,31]))
        .centerBar(true)
        .gap(1)
        .valueAccessor(function (d) {
            return d.value.count > 0 ? d.value.total / d.value.count : 0;
        });
        //.round(d3.time.month.round)
        //.alwaysUseRounding(true)
        //.xUnits(d3.time.months);

genderChart.width(320)
        .height(320)
        .radius(150)
        .dimension(genders)
        .group(gendersGroup)
        .label(function (d) {
            return d.key + ": " + d.value;
        })
        .renderLabel(true)
        .transitionDuration(500)

momedChart.renderArea(true)
        .width(900)
        .height(300)
        .transitionDuration(1000)                                                  
        .margins({top: 30, right: 50, bottom: 25, left: 100})                       
        .dimension(ages)                                                           
        .mouseZoomable(false)
        .x(d3.scale.linear().domain([0,18]))                                      
        .rangeChart(momedChartRange)
        .elasticY(true)                                                            
        .renderHorizontalGridLines(true)
        //.legend(dc.legend().x(800).y(10).itemHeight(13).gap(5))                  
        .brushOn(false)                                                            
        .group(momedsGroup)
        .valueAccessor(function (d) {
            return d.value.count > 0 ? d.value.total / d.value.count : 0;
        });

momedChartRange.width(900)
        .height(40)
        .margins({top: 0, right: 40, bottom: 20, left: 100})
        .dimension(momeds)
        .group(momedsGroup)
        .centerBar(true)
        .gap(1)
        .x(d3.scale.linear().domain([0,18]))                                      
        .valueAccessor(function (d) {
            return d.value.count > 0 ? d.value.total / d.value.count : 0;
        });

dc.renderAll();
});
