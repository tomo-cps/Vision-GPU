<template>
    <v-card v-for="gpuInfo in gpuInfo_dic" :key="gpuInfo">
        <v-layout>
            <v-row justify="center">
                <v-col cols="12" sm="6" md="5" lg="6">
                    <v-sheet :elevation="5" min-width="500" max-width="500" style="align-items: center;">
                        <div v-for="gpu in gpuInfo" :key="gpu.GPU">
                            <v-card class="mx-auto" min-width="500" max-width="500">
                                <v-img :src="gpu.ImgPath" min-width="564" max-width="564" min-height="317"
                                    max-height="317"></v-img>
                                <v-card-item :title="gpu.MachineName" min-width="500" max-width="500">
                                    <template v-slot:subtitle>
                                        <div style="display: flex; align-items: center;">
                                            <v-img src="/img/nvidia.png" alt="NVIDIA" width="16" height="16"
                                                contain></v-img>
                                            <span style="margin-left: 4px;">{{ gpu.GPUName }}</span>
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
                                                <v-row justify="end">
                                                    <v-menu min-width="200px" rounded>
                                                        <template v-slot:activator="{ props }">
                                                            <div style="display: flex; justify-content: flex-end;">
                                                                <v-card-actions class="d-flex justify-end"
                                                                    style="position: absolute; top: 230px; right: 10px;">
                                                                    <v-btn icon v-bind="props"
                                                                        v-for="login_user in gpu.UserNames"
                                                                        :key="login_user" style="margin: 7px;">
                                                                        <v-avatar :color="getUserColor(login_user)"
                                                                            size="x-large">
                                                                            <span class="text-sm">{{ login_user }}</span>
                                                                        </v-avatar>
                                                                    </v-btn>
                                                                </v-card-actions>
                                                            </div>
                                                        </template>
                                                        <v-card>
                                                            <v-card-text>
                                                                <div class="mx-auto text-center">
                                                                    <p v-for="user in gpu.DetailUser" :key="user"
                                                                        class="text-caption mt-1">
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
                                    <div v-if="gpuInfo.isExpanded">
                                        <v-list class="bg-transparent">
                                            <v-list-item v-for="gpu in gpuInfo" :key="gpu.GPU">
                                                <template v-slot:default>
                                                    <v-list-item-content>
                                                        <v-list-item-title class="text-h10">Machine Name: {{ gpu.MachineName
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">GPU Name: {{ gpu.GPUName
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">Login User: {{
                                                            String(gpu.UserNames).replace(',', ', ')
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">Utilization: {{ gpu.Utilization
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">Temperature: {{ gpu.Temperature
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">Fan Speed: {{ gpu.FanSpeed
                                                        }}</v-list-item-title>
                                                        <v-list-item-title class="text-h10">Memory: {{ gpu.UsedMemory
                                                        }}</v-list-item-title>
                                                    </v-list-item-content>
                                                </template>
                                            </v-list-item>
                                        </v-list>
                                    </div>
                                </v-expand-transition>

                                <v-divider></v-divider>

                                <v-card-actions>
                                    <v-btn @click="fullReportClik(gpuInfo)">
                                        {{ !gpuInfo.isExpanded ? 'Full Report' : 'Hide Report' }}
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>
                    </v-sheet>
                    <div class="space"></div>
                </v-col>
            </v-row>
        </v-layout>
    </v-card>
</template>

<script setup>

</script>

<script>
export default {
    name: "my-cool-component",
    props: {
        gpuInfo_dic: {
            type: Array,
            required: true
        },
        apiUrl: {
            type: String,
            required: true
        },
        imgUrl: {
            type: String,
            required: true
        },
        requireData: {
            type: String,
            required: true
        },
    },
    components: {
    },
    data: () => ({
        expand: false,
        color_dic: {
            "yama": "red-lighten-1",
            'chi': 'yellow-darken-2',
            'sen': 'light-green-lighten-1',
            'ryo': 'orange-lighten-1',
            'riku': 'deep-purple-lighten-1',
            'tomo': 'teal-darken-1',
            'kai': 'blue-darken-3',
            'other': ''
        },
    }),
    mounted() {
    },
    methods: {
        fullReportClik(gpuInfo) {
            gpuInfo.isExpanded = !gpuInfo.isExpanded;
        },
        getUserColor(login_user) {
            if (login_user in this.color_dic) {
                return this.color_dic[login_user];
            } else {
                // If login_user is not in color_dic, assign a random color
                if (!this.color_dic['other']) {
                    this.color_dic['other'] = this.colors[
                        Math.floor(Math.random() * this.colors.length)
                    ];
                }
                return this.color_dic['other'];
            }
        },
    },
    computed: {
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
}
</style>