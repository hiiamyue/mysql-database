import React, { useState, useEffect } from 'react';
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'

function range(start, stop, step) {
    if (typeof stop == 'undefined') {
        // one param defined
        stop = start;
        start = 0;
    }

    if (typeof step == 'undefined') {
        step = 1;
    }

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
        return [];
    }

    var result = [];
    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
        result.push(i);
    }

    return result;
};

function gamma(z) {
    const g = 7;
    const c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
               771.32342877765313, -176.61502916214059, 12.507343278686905,
               -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
    if (z < 0.5) {
      return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
    } else {
      z -= 1;
      let x = c[0];
      for (let i = 1; i < g + 2; i++) {
        x += c[i] / (z + i);
      }
      const t = z + g + 0.5;
      return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
    }
  }

function tDistribution(x, xBar, s, n) {
    const degreesOfFreedom = n - 1;
    const t = (x - xBar) / (s / Math.sqrt(n));
  
    // Calculate the probability using the t-distribution formula
    const numerator = gamma((degreesOfFreedom + 1) / 2) * Math.pow((1 + Math.pow(t, 2) / degreesOfFreedom), -(degreesOfFreedom + 1) / 2);
    const denominator = Math.sqrt(degreesOfFreedom * Math.PI) * gamma(degreesOfFreedom / 2);
    const probability = numerator / denominator;
  
    return probability;
  }

const NormalDistribRating = ({mean, stdDev}) => {
    
    const normalY = (x, mean, stdDev) => Math.exp((-0.5) * Math.pow((x - mean) / stdDev, 2));
    
    let errorMargin = 2.01 * (stdDev / Math.sqrt(50))  
    let upperBound = mean + errorMargin                                                                                                                     
    let lowerBound = mean - errorMargin
    let points = range(lowerBound - 0.5, upperBound + 0.5, 0.005);
    let y = points.map(x => ({ x, y: tDistribution(x, mean, stdDev, 50)}));
    var Highcharts = require('highcharts');

    React.useEffect(() => {
        console.log(upperBound)
        console.log(lowerBound)
        console.log(mean)
        console.log(stdDev)
        console.log(tDistribution(upperBound, mean, stdDev, 50))
        console.log(tDistribution(lowerBound, mean, stdDev, 50))
    })

    const options = {
        chart: {
            type: 'area',
            height: 300,
            backgroundColor: 'transparent',
            style: {
                fontFamily: 'monospace',
                color: "#0000"
            }
    
        },
        title: {
            text: '95%',
            y: 200,
            style: {
                fontFamily: 'roboto',
                color: "#e879f9"
            }    
        },
        yAxis: {
        labels: {
            enabled: false,  	
                },
          gridLineWidth: 0,
          title: ''
        },
        xAxis: {
            labels: {
                style: {
                   color: '#FFFF',
                   font: '11px Roboto, sans-serif'
            }
          }
        },
        tooltip: {
           enabled: true,
           valueDecimals: 3
        },
        legend: {
            enabled: false,
        },
        series: [{
            data: y,
        }],
        plotOptions: {
            area: {
            
            color: '#e879f9',
            fillColor: 'rgba(240, 171, 252,0.2)',
            zoneAxis: 'x',
            zones: [{
            //fillColor gets the inside of the graph, color would change the lines
            fillColor: 'transparent',
            // everything below this value has this style applied to it
            value: lowerBound,
          },{
            value: upperBound,
          },{
            fillColor: 'transparent',
          }]
        }
    }};

    return (
        <div id="container">
            {mean === ""?
            <p className='text-6xl font-extrabold text-fuchsia-400 text-center'>?</p>
            :
            <HighchartsReact highcharts={Highcharts}  options={options}/>
            }
            
        </div>
    );
}

export default NormalDistribRating