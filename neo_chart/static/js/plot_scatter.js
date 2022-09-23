// Create arrays
var v_rel = [];
var h = [];

// Load JSON data
$.getJSON("/api/scatterplot").then((neodata) => {
    console.log(neodata)
    neodata.forEach(function(x) {

        v_rel.push(x[0]);
        h.push(x[1]);
    })

// Scatter chart
var coords1 = v_rel.map((x, i) => ({ x, y: h[i] }));

const data1 = {
    datasets: [{
        label: 'Velocity (km/s) and magnitude (h)',
        data: coords1,
        backgroundColor: 'rgb(252, 165, 3, 0.4)'
    }],
};

const config1 = {
    type: 'scatter',
    data: data1,
    options: {
        animation: {
            duration: 3000,
            easing: 'easeInOutBounce',
            },
        plugins: {
            zoom: {
                pan: {
                    enabled: true,
                    mode: 'xy'
                },
                zoom: {
                    wheel: {
                        enabled : true,
                    },
                        pinch: {
                            enabled: true
                        },
                    mode: 'xy',
                }
            },
            legend: {
                display: false,
                },
            title: {
                display: true,
                text: 'Velocity vs Magnitude',
                font: {
                    size: 22
                }
                }
            },
        scales: {
        x: {
            grid: {
                borderColor: '#fff',
                color: 'rgba(255, 255, 255, 0.3)'
            },
            ticks: {
                color: '#fff'
            },
            type: 'linear',
            position: 'bottom',
            title: {
                color: '#fff',
                display: true,
                text: 'Velocity (km/s)'
                }
            },
        y: {
            grid: {
                borderColor: '#fff',
                color: 'rgba(255, 255, 255, 0.3)'
            },
            ticks: {
                color: '#fff'
            },
            title: {
                color: '#fff',
                display: true,
                text: 'Magnitude (h)'
                }
            }
            }
        },
        }

const chart1 = new Chart(
    document.getElementById('chart1'),
    config1
    );
    
    Chart.defaults.color = '#fff';
    Chart.defaults.font.size = 16;
});