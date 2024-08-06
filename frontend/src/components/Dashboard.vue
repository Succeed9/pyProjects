<template>
    <div class="dashboard">
      <h1>Dashboard</h1>
      <line-chart :chart-data="chartData"></line-chart>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import LineChart from '@/components/LineChart';
  
  export default {
    components: {
      LineChart
    },
    data() {
      return {
        chartData: null
      };
    },
    async created() {
      const token = localStorage.getItem('token');
      const response = await axios.get('http://localhost:5000/data', {
        headers: { Authorization: `Bearer ${token}` }
      });
      this.chartData = {
        labels: response.data.map(d => d.timestamp),
        datasets: [
          {
            label: 'Dataset',
            data: response.data.map(d => d.value),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }
        ]
      };
    }
  };
  </script>
  