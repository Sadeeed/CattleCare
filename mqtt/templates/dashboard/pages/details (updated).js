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
      data: [0, 10, 5, 2, 20, 30],
    }]
  };

  const temperature = {
    labels: labels,
    datasets: [{
      label: 'values over time',
      backgroundColor: '#0cc2aa',
      borderColor: '#0cc2aa',
      data: [35.02, 35.88, 35.88, 35.75, 35.94, 36],
    }]
  };

  const bpm = {
    labels: labels,
    datasets: [{
      label: 'values over time',
      backgroundColor: '#0cc2aa',
      borderColor: '#0cc2aa',
      data: [29, 35, 36, 37, 39, 36],
    }]
  };

  const ketosis = {
    labels: labels,
    datasets: [{
      label: 'values over time',
      backgroundColor: '#0cc2aa',
      borderColor: '#0cc2aa',
      data: [0, 0, 1, 0, 0, 0],
    }]
  };

  const mvmt = {
    labels: labels,
    datasets: [{
      label: 'values over time',
      backgroundColor: '#0cc2aa',
      borderColor: '#0cc2aa',
      data: [1, 1, 1, 0, 1, 0],
    }]
  };

  const temperature_config = {
    type: 'line',
    data: temperature,
    options: {}
  };

    const bpm_config = {
    type: 'line',
    data: bpm,
    options: {}
  };

  const ketosis_config = {
    type: 'line',
    data: ketosis,
    options: {}
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

  const mvmt_config = {
    type: 'line',
    data: mvmt,
    options: {}
  };


  const myChart1 = new Chart(
    document.getElementById('myChart1'),
    temperature_config
  );

  const myChart2 = new Chart(
    document.getElementById('myChart2'),
    bpm_config
  );

  const myChart3 = new Chart(
    document.getElementById('myChart3'),
    ketosis_config
  );

  const myChart4 = new Chart(
    document.getElementById('myChart4'),
    config
  );

  const myChart5 = new Chart(
    document.getElementById('myChart5'),
    mvmt_config
  );

  const myChart6 = new Chart(
    document.getElementById('myChart6'),
    config
  );