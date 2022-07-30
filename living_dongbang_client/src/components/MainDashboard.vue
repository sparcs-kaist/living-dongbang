<template>
    <div id="main-dashboard">
        <CurrentClock />
    </div>
</template>

<script>
import CurrentClock from './CurrentClock.vue'
export default {
    components: { 
        CurrentClock 
    },
    data() {
        return {
            logoImg: require("../assets/SPARCS.png")
        };
    }
}
</script>