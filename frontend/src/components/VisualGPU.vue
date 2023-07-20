<template>
    <v-sheet :elevation="5">
        <div v-for="gpu in gpuInfo" :key="gpu.GPU">
            <v-card class="mx-auto" max-width="5000">
                <v-img :src="imgUrl" max-width="100%" max-height="500"></v-img>
                <v-card-item :title="gpu.MachineName" max-width="5000">
                    <template v-slot:subtitle>
                        <div style="display: flex; align-items: center;">
                            <v-img src="/img/nvidia.png" alt="NVIDIA" width="16" height="16" contain></v-img>
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
                            <v-container fluid style="height: 60px">
                                <v-row justify="center">
                                    <v-menu min-width="200px" rounded>
                                        <template v-slot:activator="{ props }">
                                            <v-btn icon v-bind="props">
                                                <v-avatar :color="randomColor" size="x-large">
                                                    <span class="text-sm">{{ gpu.LoginUser }}</span>
                                                </v-avatar>
                                            </v-btn>
                                        </template>
                                        <v-card>
                                            <v-card-text>
                                                <div class="mx-auto text-center">
                                                    <v-avatar :color="randomColor" size="large">
                                                        <span class="text-sm">{{ gpu.LoginUser }}</span>
                                                    </v-avatar>
                                                    <p v-for="user in gpu.DetailUser" :key="user" class="text-caption mt-1">
                                                        {{ user }}
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
                        <v-list-item-subtitle>{{ gpu.FanSpeed }} </v-list-item-subtitle>
                    </v-list-item>
                    <v-list-item density="dense" prepend-icon="mdi-memory">
                        <v-list-item-subtitle>{{ gpu.UsedMemory }} </v-list-item-subtitle>
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
                                        <v-list-item-title class="text-h10">Machine Name: {{ gpu.MachineName }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">GPU Name: {{ gpu.Name }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">Login User: {{ gpu.LoginUser }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">Utilization: {{ gpu.Utilization }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">Temperature: {{ gpu.Temperature }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">Fan Speed: {{ gpu.FanSpeed }}</v-list-item-title>
                                        <v-list-item-title class="text-h10">Memory: {{ gpu.UsedMemory }}</v-list-item-title>
                                    </v-list-item-content>
                                </template>
                            </v-list-item>
                        </v-list>
                    </div>
                </v-expand-transition>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-btn @click="fullReportClik">
                        {{ !expand ? 'Full Report' : 'Hide Report' }}
                    </v-btn>
                </v-card-actions>
            </v-card>
        </div>
    </v-sheet>
    <div class="space"></div>
</template>

<script setup>

const user = {
    initials: 'TO',
    fullName: 'Tomoaki Ohkawa',
    email: 'tomoaki.ohkawa@cps.akita-pu.ac.jp',
}

</script>

<script>
export default {
    name: "my-cool-component",
    props: {
        apiUrl: {
            type: String,
            required: true
        },
        imgUrl: {
            type: String,
            required: true
        },
    },
    components: {
    },
    data: () => ({
        gpuInfo: [],
        expand: false,
        colors: ['red', 'blue', 'green', 'yellow', 'orange', 'purple'],
    }),
    mounted() {
        this.fetchGPUInfo();
    },
    methods: {
        async fetchGPUInfo() {
            try {
                const response = await fetch(this.apiUrl);
                const data = await response.json();
                this.gpuInfo = data;
                console.log(data);
            } catch (error) {
                console.log(error);
            }
        },
        fullReportClik() {
            this.expand = !this.expand;
            // this.fetchGPUInfo();
        }
    },
    computed: {
        randomColor() {
            const randomIndex = Math.floor(Math.random() * this.colors.length);
            return this.colors[randomIndex];
        },
    },
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

.element.style {
    z-index: 900;
    position: relative;
    overflow: hidden;
}

.space {
    height: 16px;
    /* 空間の高さ */
}

/* .text-h6 {
  font-size: 0.6rem; /* 例えば、フォントサイズを1.25remに設定 */
  /* font-weight: bold; フォントの太さを太字に設定 */
  /* margin-bottom: 0.5rem; 下のマージンを0.5remに設定 */
/* } */

</style>