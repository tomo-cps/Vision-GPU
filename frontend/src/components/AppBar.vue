<template>
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
                <v-list-item color="grey-darken-3" v-for="menu in menus" :key="menu.name" :to="menu.url">
                    <v-list-item-title><v-icon>{{ menu.icon }}</v-icon> {{ menu.name }}</v-list-item-title>
                </v-list-item>
            </v-list-item-group>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'AppBar',
    data: () => ({
        drawer: false,
        menus: [
            { name: '', icon: '', url: '' },
            { name: 'Home', icon: 'mdi-home', url: '/' },
            { name: 'Available', icon: 'mdi-map-marker', url: '/available' },
            { name: 'Used', icon: 'mdi-apple-safari', url: '/used' },
        ]
    }),
    components: {
    },
    methods: {
        reloadPage() {
            location.reload();
        }
    },
});
</script>

<style>
/* .text-right{
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    z-index: 1;
}

.sidebar_layer{
  top: 0;
  z-index: 800;
} */
</style>