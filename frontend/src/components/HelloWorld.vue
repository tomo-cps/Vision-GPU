<template>
  <div>
    <v-card>
      <AppBar />
      <!-- <SideBar /> -->
    <v-card>
      <v-layout>
        <!-- <transition-group name="fade" tag="div"> -->
          <v-row justify="center">
            <v-col cols="12" sm="6" md="5" lg="6">
              <ViG v-for="(url, index) in apiUrls" :key="index" :api-url="url" :img-url="imgUrls[index]" class="animated-item"/>
            </v-col>
          </v-row>
        <!-- </transition-group> -->
      </v-layout>
    </v-card>
  </v-card>
  </div>
</template>

<script>
import AppBar from '../components/AppBar.vue';
import SideBar from '../components/SideBar.vue';
import ViG from '../components/VisualGPU.vue';
// import SvgIcon from '@jamescoyle/vue-icon'
// import { mdiAccount } from '@mdi/js'

export default {
  name: "my-cool-component",
  components: {
    AppBar,
    SideBar,
    ViG,
  },
  data: () => ({
    apiUrls: [
      // 'https://gmc.cps.akita-pu.ac.jp/abert/',
      'https://gmc.cps.akita-pu.ac.jp/baker/',
      // 'https://gmc.cps.akita-pu.ac.jp/casa/',
      // 'https://gmc.cps.akita-pu.ac.jp/dusia/',
      'https://gmc.cps.akita-pu.ac.jp/erie/',
      // 'https://gmc.cps.akita-pu.ac.jp/fern/',
      // 'https://gmc.cps.akita-pu.ac.jp/gouin/',
      // 'https://gmc.cps.akita-pu.ac.jp/hazen/',
      'https://gmc.cps.akita-pu.ac.jp/ibera/',
      // 'https://gmc.cps.akita-pu.ac.jp/junin/',
      // 'https://gmc.cps.akita-pu.ac.jp/kezar/',
    ],
    imgUrls: [
      // "/img/abert.png",
      "/img/baker.png",
      // "/img/casa.png",
      // "/img/dusia.png",
      "/img/erie.png",
      // "/img/fern.png",
      // "/img/gouin.png",
      // "/img/hazen.png",
      "/img/ibera.png",
      // "/img/junin.png",
      // "/img/kezar.png",
    ]
  }),
  mounted() {
  },
  methods: {
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
}</style>
