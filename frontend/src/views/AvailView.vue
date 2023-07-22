<template>
    AvailGPU.vue
    <AvailGPU />
</template>
  
<script>
import { defineComponent } from 'vue';

// Components
import AvailGPU from '../components/AvailGPU.vue';

export default defineComponent({
    name: 'HomeView',
    components: {
        AvailGPU,
    },
});
</script>