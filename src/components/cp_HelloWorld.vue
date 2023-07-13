<template>
  <div>
    <v-container fluid>
      <v-row justify="center" align="center">
        <v-col cols="12" sm="6" md="4">
          <v-card>
            <v-img src="../assets/erie.png" alt="Your Image" width="400" height="300" contain></v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
  <div>
    <table class="gpu-table">
      <thead>
        <tr>
          <th>GPU</th>
          <th>Name</th>
          <th>Memory</th>
          <th>Utilization</th>
          <th>Fan Speed</th>
          <th>Temperature</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="gpu in gpuInfo" :key="gpu.GPU">
          <td>{{ gpu.GPU }}</td>
          <td>{{ gpu.Name }}</td>
          <td>{{ gpu.Memory }}</td>
          <td>{{ gpu.Utilization }}</td>
          <td>{{ gpu['Fan Speed'] }}</td>
          <td>{{ gpu.Temperature }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gpuInfo: [],
      photos: [
        { id: 1, url: '../assets/erie.png' },
        // { id: 2, url: '../assets/logo.png' },
      ],
    };
  },
  mounted() {
    this.fetchGPUInfo();
  },
  methods: {
    async fetchGPUInfo() {
      try {
        const response = await fetch("https://gmc.cps.akita-pu.ac.jp/erie/");
        const data = await response.json();
        this.gpuInfo = data;
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>

<style>
.gpu-table {
  width: 100%;
  border-collapse: collapse;
}

.gpu-table th,
.gpu-table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.gpu-table th {
  background-color: #f2f2f2;
}

.gpu-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}
</style>


