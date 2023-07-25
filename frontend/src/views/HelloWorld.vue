<template>
  <div>
    <v-card>
      <v-card max-width="mx-auto" class="mx-auto" color="grey-lighten-3">
        <v-app-bar color="grey-darken-3">
          <template v-slot:prepend>
            <v-app-bar-nav-icon v-on:click.stop="drawer = !drawer"></v-app-bar-nav-icon>
          </template>

          <v-app-bar-title>Visual-GPU</v-app-bar-title>

          <v-spacer></v-spacer>

          <v-btn icon @click="reloadPage">
            <v-icon>mdi-reload</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </v-app-bar>
      </v-card>
      <v-navigation-drawer v-model="drawer" fixed temporary left location="left">
        <v-list nav dense>
          <v-list-item-group>
            <v-list-item>
            </v-list-item>
            <v-list-item color="grey-darken-3" v-for="menu in menus" :key="menu.name" @click="handleClick(menu.name)">
              <v-list-item-title><v-icon>{{ menu.icon }}</v-icon> {{ menu.name }}</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
      <div v-if="fetchwait == true">
        <ViG :gpuInfo_dic="propsGPUInfo" class="animated-item" />
      </div>
    </v-card>
  </div>
</template>

<script>
import ViG from '../components/VisualGPU.vue';

export default {
  name: "my-cool-component",
  components: {
    ViG,
  },
  data: () => ({
    gpuInfo_dic: {},
    propsGPUInfo: [],
    apiUrls: [
      // 'https://gmc.cps.akita-pu.ac.jp/abert/',
      'https://gmc.cps.akita-pu.ac.jp/baker/',
      // 'https://gmc.cps.akita-pu.ac.jp/casa/',
      'https://gmc.cps.akita-pu.ac.jp/dusia/',
      'https://gmc.cps.akita-pu.ac.jp/erie/',
      // 'https://gmc.cps.akita-pu.ac.jp/fern/',
      // 'https://gmc.cps.akita-pu.ac.jp/gouin/',
      // 'https://gmc.cps.akita-pu.ac.jp/hazen/',
      'https://gmc.cps.akita-pu.ac.jp/ibera/',
      'https://gmc.cps.akita-pu.ac.jp/junin/',
      // 'https://gmc.cps.akita-pu.ac.jp/kezar/',
    ],
    imgUrls: [
      // "/img/abert.png",
      "/img/baker.png",
      // "/img/casa.png",
      "/img/dusia.png",
      "/img/erie.png",
      // "/img/fern.png",
      // "/img/gouin.png",
      // "/img/hazen.png",
      "/img/ibera.png",
      "/img/junin.png",
      // "/img/kezar.png",
    ],
    fetchwait: false,
    requirePage: 'Home',
    drawer: false,
    menus: [
      { name: 'Home', icon: 'mdi-home' },
      { name: 'Available', icon: 'mdi-check-circle-outline' },
      { name: 'Used', icon: 'mdi-chart-line-stacked' },
    ],
  }),
  async mounted() {
    await this.fetchGPUInfo();
    this.fetchwait = true;
  },
  methods: {
    async fetchGPUInfo() {
      const gpuInfo_dic = {
        "Home": [],
        "Available": [],
        "Used": []
      }
      for (const apiUrl of this.apiUrls) {
        const response = await fetch(apiUrl);
        const data = await response.json();
        gpuInfo_dic["Home"].push(data);
        for (const item of data) {
          if (item.Utilization === '0%' || item.Utilization === '0%/0%') {
            gpuInfo_dic["Available"].push(data);
        } else {
          gpuInfo_dic["Used"].push(data);
        }
        }
      }
      this.gpuInfo_dic = gpuInfo_dic
      this.propsGPUInfo = gpuInfo_dic['Home']
      console.log(this.propsGPUInfo)
    },
    handleClick(name) {
      this.requirePage = name
      this.propsGPUInfo = this.gpuInfo_dic[name]
      this.drawer = false
    },
    reloadPage() {
      location.reload();
    },
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active below version 2.1.8 */
  {
  opacity: 0;
}
</style>
