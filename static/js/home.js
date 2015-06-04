var diameter = 500,
    format = d3.format(",d"),
    color = d3.scale.category20c();//ordinal().range(['#268bd2', '#cb4b16', '#859900', '#993399', '#d33682', '#b58900', '#2aa198', '#6c71c4', '#dc322f']);
    //['#d33682', '#dc322f', '#cb4b16', '#b58900', '#859900', '#2aa198', '#268bd2', '#6c71c4', '#993399']

var bubble = d3.layout.pack()
    .sort(null)
    .size([diameter, diameter])
    .padding(2);

var svg = d3.select("#langStatsChart").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
    .attr("class", "bubble");

var tip = d3.tip()
  .attr('class', 'd3-tip')
//  .offset([0, 0])
  .html(function(d) {
    return format(d.value);
  })

svg.call(tip);

d3.json("static/json/langStats.json", function(error, root) {

  console.log(classes(root));
  var node = svg.selectAll(".node")
      .data(bubble.nodes(classes(root))
      .filter(function(d) { return !d.children; }))
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  node.append("title")
      .text(function(d) { return d.name + ": " + format(d.value); });

  node.append("circle")
      .attr("r", function(d) { return d.r ; })
      .style("fill", function(d) { return color(d.name); });

  node.append("text")
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
//      .text(function(d) { return d.name.substring(0, d.r / 3); })
      .text(function(d) { return d.name; })
      .style("font-size", function(d) { return Math.min(2 * d.r, (2 * d.r - 4) / this.getComputedTextLength() * 12) + "px"; })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide);

});

svg.call(tip);


// Returns a flattened hierarchy containing all leaf nodes under the root.
function classes(root) {
  var classes = [];

  function recurse(name, node) {
    if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
    else classes.push({name: node.name, value: node.count});
  }

  recurse(null, root);
  return {children: classes};
}

//d3.select("#langStatsChart").style("height", diameter + "px");