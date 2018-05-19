
/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Close
 * index 5 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

function getUsersData() {
  var queryUrl = `http://localhost:5000/api`;
  Plotly.d3.json(queryUrl, function(error, response) {
    console.log('response')
    console.log(response)
    // message_count
    var trace1 = {
      x: unpack(response,'realname'),
      y: unpack(response,'message_count'),
      type: 'bar',
      text: unpack(response,'slack_name'),
      marker: {
        color: 'rgb(142,124,195)'
      }
    };
    
    var data = [trace1];
    
    var layout = {
      title: 'Number of Slack Messages Made by Students',
      font:{
        family: 'Raleway, snas-serif'
      },
      showlegend: false,
      xaxis: {
        tickangle: -45
      },
      yaxis: {
        zeroline: false,
        gridwidth: 2
      },
      bargap :0.05
    };
    
    Plotly.newPlot('plot', data, layout);


    

    // 
  });
}
getUsersData()
