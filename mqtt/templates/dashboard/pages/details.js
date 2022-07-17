const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'values over time',
      backgroundColor: '#0cc2aa',
      borderColor: '#0cc2aa',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

  const myChart1 = new Chart(
    document.getElementById('myChart1'),
    config
  );

  const myChart2 = new Chart(
    document.getElementById('myChart2'),
    config
  );

  const myChart3 = new Chart(
    document.getElementById('myChart3'),
    config
  );

  const myChart4 = new Chart(
    document.getElementById('myChart4'),
    config
  );

  const myChart5 = new Chart(
    document.getElementById('myChart5'),
    config
  );

  const myChart6 = new Chart(
    document.getElementById('myChart6'),
    config
  );