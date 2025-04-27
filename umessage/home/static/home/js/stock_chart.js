document.addEventListener('DOMContentLoaded', function() {

    const ctx = document.getElementById('stockChart').getContext('2d');
    const stockChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: window.chartData.dates,
            datasets: [{
                label: window.chartSymbol + ' - Price',
                data: window.chartData.prices,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false,
                tension: 0.1,
                pointRadius: 0,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
            mode: 'index',
            intersect: false,
            },
            plugins: {
                zoom: {
                zoom: {
                    wheel: {
                        enabled: true,
                        modifierKey: 'ctrl'
                    },
                    pinch: {
                        enabled: true
                    },
                    mode: 'xy',
                    speed: 0.1
                },
                pan: {
                    enabled: true,
                    mode: 'xy',
                    speed: 10,
                },
                limits: {
                    x: {
                        min: 0,
                        max: chartData.dates.length - 1
                    },
                    y: {
                        min: Math.min(...chartData.prices),
                        max: Math.max(...chartData.prices)
                    }
                }
                },
                tooltip: {
                    enabled: true,
                    mode: 'index',
                    intersect: false,
                    position: 'nearest'
                },
                crosshair: {
                    line: {
                    color: 'rgba(75, 192, 192, 1)',
                    width: 1
                    },
                    sync: {
                    enabled: false
                    },
                    zoom: {
                    enabled: false
                    },
                    snap: {
                    enabled: true
                    }
                }
            },
            elements: {
                line: {
                    tension: 0.1
                },
                point: {
                    radius: 0
                }
            },
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    bottom: 10
                }
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Date'
                    },
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 10,
                        maxRotation: 0,
                        minRotation: 0,
                    }
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: 'Price'
                    }
                }
            }
        }
    });

});