<template>
  <div>
    <v-card>
      <AppBar />
    </v-card>
    <v-card>
      <v-layout>
        <v-row justify="center">
          <v-col cols="12" sm="6" md="5" lg="6">
            <ViG v-for="(url, index) in apiUrls" :key="index" :api-url="url" :img-url="imgUrls[index]" />
          </v-col>
        </v-row>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
import AppBar from '../components/AppBar.vue';
import ViG from '../components/VisualGPU.vue';
// import SvgIcon from '@jamescoyle/vue-icon'
// import { mdiAccount } from '@mdi/js'

export default {
  name: "my-cool-component",
  components: {
    AppBar,
    ViG,
  },
  data: () => ({
    apiUrls: [
        'https://gmc.cps.akita-pu.ac.jp/erie/',
        'https://gmc.cps.akita-pu.ac.jp/ibera/',
      ],
    imgUrls: [
      "/img/erie.png",
      "/img/ibera.png",
    ]
  }),
  mounted() {
  },
  methods: {
  }
}
</script>

<style></style>
