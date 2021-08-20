var formatter = new Intl.NumberFormat('en-US', {
	style: 'currency',
	currency: 'USD',
	minimumFractionDigits: 2
  });
  var nf = new Intl.NumberFormat('en-US', {
	minimumFractionDigits: 2

  });

  

function buildMetadata(QQ) {
	var data1 = d3.select("#sample-metadata").html("") 
	var data2 = d3.select("#sample-metadata2").html("") 
	var data3 = d3.select("#sample-metadata3").html("") 

	d3.json(`/metadata/${QQ}`).then(function(d){
	  var c = d
		
	y_val=[]
	y_val2=[]
    y_val=d[`TTL`];
    y_val2=d[`TTL $`]
	
	
	
	var total = 0;
	for(var i = 0; i < y_val.length; i++) {
	total += y_val[i];
	var avg = total / y_val.length;
}	var stdv= (math.std(y_val));

	var count = 0;
	for(var i = 0; i < y_val.length; ++i){
		if( y_val[i] < avg)
			count++;
}
	console.log(count)

	var max = y_val.reduce(function(a, b) {
		return Math.max(a, b);
	});
	var min = y_val.reduce(function(a, b) {
		return Math.min(a, b);
	});


	var total2 = 0;
	for(var i = 0; i < y_val2.length; i++) {
	total2 += y_val2[i];
	var avg1 = (total2 / y_val2.length);
	var stdv1= (math.std(y_val2));
}
	var count2 = 0;
	for(var i = 0; i < y_val2.length; ++i){
		if( y_val2[i] < avg1)
			count2++;
}
	var max1 = y_val2.reduce(function(a, b) {
		return (Math.max(a, b));
	});
	var min1 = y_val2.reduce(function(a, b) {
		return (Math.min(a, b));
	});




	data1.append("h6").append("b").style("font-size", "15px").text(`${QQ}`)


	  Object.entries(c).forEach(([key, value]) => {
	  var cell = data1.append("h6").append("b").style("font-size", "15px")
  
	  cell.text(`${key}(Year to Date) : ${nf.format(value.reduce((a, b) => a + b, 0))}`);
	});

	data2.append("h6").append("b").style("font-size", "15px").text(`Average: ${nf.format(avg)}`)
	data2.append("h6").append("b").style("font-size", "15px").text(`Standard Deviation: ${nf.format(stdv)}`)
	data2.append("h6").append("b").style("font-size", "15px").text(`High: ${nf.format(max)}`)
	data2.append("h6").append("b").style("font-size", "15px").text(`Low: ${nf.format(min)}`)
	data2.append("h6").append("b").style("font-size", "15px").text(`Total Week(s) Below Average: ${count}`)

	data3.append("h6").append("b").style("font-size", "15px").text(`Average: ${formatter.format(avg1)}`)
	data3.append("h6").append("b").style("font-size", "15px").text(`Standard Deviation: ${formatter.format(stdv1)}`)
	data3.append("h6").append("b").style("font-size", "15px").text(`High: ${formatter.format(max1)}`)
	data3.append("h6").append("b").style("font-size", "15px").text(`Low: ${formatter.format(min1)}`)
	data3.append("h6").append("b").style("font-size", "15px").text(`Total Week(s) Below Average: ${count2}`)




	})}

var x_axis=[6,7,8,9,10,11,12,13,14,15,16,17,18,19]





function buildGDPCharts(QQ) {

   d3.json(`/metadata/${QQ}`).then(function(d){
    Plotly.purge('myDiv')

	y_val=[]
	y_val2=[]
    y_val=d[`TTL`];
    y_val2=d[`TTL $`]
	
	


	
	var total = 0;
	for(var i = 0; i < y_val.length; i++) {
    total += y_val[i];
}
	var avg = total / y_val.length;

	var total2 = 0;
	for(var i = 0; i < y_val2.length; i++) {
    total2 += y_val2[i];
}
	var avg2 = total2 / y_val2.length;



    var trace={
    	x:x_axis,
		y:y_val,
    	mode: 'lines+markers',
 		type: 'bar',
 		name: 'Case Volume',

        };

    var trace2 = {
		  x: x_axis,
		  y: y_val2,
		  xaxis: 'x2',
		  yaxis: 'y2',
		 mode: 'lines+markers',
 		type: 'bar',
 		name:`Spend $`,
		};


    var layout = {
		grid: {rows: 1, columns: 2, pattern: 'independent'},
    	showlegend: false,
 		 title: `${QQ}`,
 		 xaxis:{
 		 	title:"Week",
 		 	domain:[0,0.46]
 		 },
 		 yaxis:{
 		 	title:"Case Volume",
 		 },
		  
 		xaxis2: {domain: [0.54, 1],
 			title:"Week",
 		},
  		yaxis2: {anchor: 'x2',
  		title:"Spend $"
				},
				shapes: [
					{
						type: 'line',
						xref: 'x1',
						yref: 'y1',
						x0: 6,
						y0: avg,
						x1: 19,
						y1: avg,
						line:{
							color: 'rgb(255, 0, 0)',
							width: 4,
							dash:'dot'
						}
					}
					,
					{
						type: 'line',
						xref: 'x2',
						yref: 'y2',
						x0: 6,
						y0: avg2,
						x1: 19,
						y1: avg2,
						line:{
							color: 'rgb(255, 0, 0)',
							width: 4,
							dash:'rect'
						}
					
					}
					]
}

    var data=[trace,trace2]
    Plotly.newPlot('myDiv', data,layout);
})}


function init(){
	var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((countryNames) => {
    countryNames.forEach((QQ) => {
      selector
        .append("option")	
        .text(QQ)
        .property("value", QQ);
    });
    const DC=countryNames[0]
	buildGDPCharts(DC)
	buildMetadata(DC)

})}

function optionChanged(newDC) {
	buildGDPCharts(newDC)
	buildMetadata(newDC)
};
init();