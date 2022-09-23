// Create arrays
var dist_min = [];
var h = [];

// Load JSON data
$.getJSON("/api/bubblechart").then((neodata) => {
    neodata.forEach(function(x) {

        dist_min.push(x[0]);
        h.push(x[2]);
    
    })

// Create coords to plot, multiplying h to increase bubble size
const coords2 = dist_min.map((x, j) => ({x, y: 0, r: h[j]}));

const data2 = {
    datasets: [{
        label: 'Asteroids distance (au) and magnitude (h)',
        data: coords2,
        backgroundColor: 'rgb(70, 119, 184, 0.6)',
        borderWidth: 5
        }]
    };

    const config2 = {
        type: 'bubble',
        data: data2,
        options: {
            animation: {
                duration: 6000,
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
                    display: false
                    },
                title: {
                    display: true,
                    text: 'Potentially hazardous asteroids (PHAs)',
                    font: {
                        size: 22
                    }
                }
            },
            scales: {
                x: {
                    color: '#fff',
                    grid: {
                        color: 'rgba(255, 255, 255, 0.4)',
                        borderColor: '#fff'
                        },
                    ticks: {
                        color: '#fff'
                        },
                    title: {
                        color: '#fff',
                        display: true,
                        text: 'Distance (au)'
                        }
                    },
                y: {
                    display: false
                }
                },
            },
        };

        const chart2 = new Chart(
            document.getElementById('chart2'),
            config2
            )

            Chart.defaults.color = '#fff';
            Chart.defaults.font.size = 16;
});