<template>
  <div v-for="gpu in gpuInfo" :key="gpu.GPU">
    <v-card class="mx-auto" max-width="368">
      <v-card-item title="erie">
        <template v-slot:subtitle>
          <div style="display: flex; align-items: center;">
            <v-img src="../assets/nvidia.png" alt="NVIDIA" width="16" height="16" contain></v-img>
            <span style="margin-left: 4px;">{{ gpu.Name }}</span>
          </div>
        </template>
      </v-card-item>
      <v-card-text class="py-0">
        <v-row align="center" no-gutters>
          <v-col class="text-h2" cols="10">
            {{ gpu.Temperature }}
          </v-col>
          <v-col cols="14" class="text-right">
            <!-- アイコンの表示 -->
            <v-container fluid style="height: 60px">
              <v-row justify="center">
                <v-menu min-width="200px" rounded>
                  <template v-slot:activator="{ props }">
                    <v-btn icon v-bind="props">
                      <v-avatar color="blue" size="large">
                        <span class="text-h5">{{ user.initials }}</span>
                      </v-avatar>
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-text>
                      <div class="mx-auto text-center">
                        <v-avatar color="blue">
                          <span class="text-h5">{{ user.initials }}</span>
                        </v-avatar>
                        <h3>{{ user.fullName }}</h3>
                        <p class="text-caption mt-1">
                          {{ user.email }}
                        </p>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-menu>
              </v-row>
            </v-container>
          </v-col>
        </v-row>
      </v-card-text>
      <div class="d-flex py-3 justify-space-between">
        <v-list-item density="compact" prepend-icon="mdi-weather-windy">
          <v-list-item-subtitle>{{ gpu['Fan Speed'] }} </v-list-item-subtitle>
        </v-list-item>
        <v-list-item density="dense" prepend-icon="mdi-memory">
          <v-list-item-subtitle>{{ gpu.Memory }} </v-list-item-subtitle>
        </v-list-item>
        <v-list-item density="dense" prepend-icon="mdi-server-minus">
          <v-list-item-subtitle>{{ gpu.Utilization }}</v-list-item-subtitle>
        </v-list-item>
      </div>

      <v-expand-transition>
        <div v-if="expand">
          <v-list class="bg-transparent">
            <v-list-item v-for="gpu in gpuInfo" :key="gpu.GPU">
              <template v-slot:default>
                <v-list-item-content>
                  <v-list-item-title>Machine Name: erie</v-list-item-title>
                  <v-list-item-title>GPU Name: {{ gpu.Name }}</v-list-item-title>
                  <v-list-item-title>Utilization: {{ gpu.Utilization }}</v-list-item-title>
                  <v-list-item-title>Fan Speed: {{ gpu['Fan Speed'] }}</v-list-item-title>
                  <v-list-item-title>Memory: {{ gpu.Memory }}</v-list-item-title>
                </v-list-item-content>
              </template>
              <v-list-item-action>
                <v-icon :color="getIconColor(gpu.Utilization)">mdi-server-minus</v-icon>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </div>
      </v-expand-transition>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn @click="expand = !expand">
          {{ !expand ? 'Full Report' : 'Hide Report' }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const user = {
  initials: 'TO',
  fullName: 'Tomoaki Ohkawa',
  email: 'tomoaki.ohkawa@cps.akita-pu.ac.jp',
}

const expand = ref(false)
// const time = ref(0)
</script>

<script>
// import SvgIcon from '@jamescoyle/vue-icon'
// import { mdiAccount } from '@mdi/js'

export default {
  name: "my-cool-component",
  components: {
    // SvgIcon
  },
  data: () => ({
    gpuInfo: [],
    expand: false,
  }),
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
    },
    
  }
}
</script>

<style>
.v-list-item__prepend {
  align-items: center;
  align-self: center;
  display: flex;
  grid-area: prepend;
  width: 40px;
}

.v-responsive {
  display: flex;
  flex: 1 0 auto;
  max-height: 10%;
  max-width: 6%;
  overflow: hidden;
  position: relative;
}
</style>
