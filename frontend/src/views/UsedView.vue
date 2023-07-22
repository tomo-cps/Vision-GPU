<template>
    UsedView.vue
    <UsedGPU />
</template>
  
<script>
import { defineComponent } from 'vue';

// Components
import UsedGPU from '../components/UsedGPU.vue';

export default defineComponent({
    name: 'UsedView',
    components: {
        UsedGPU,
    },
});
</script>