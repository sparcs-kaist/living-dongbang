<template>
    <div>
        <TimeSlider />
        <CurrentClock />
    </div>
</template>

<script>
import CurrentClock from './CurrentClock.vue'
import TimeSlider from './TimeSlider.vue';
export default {
    components: {
        CurrentClock,
        TimeSlider
    },
    data() {
        return {
            logoImg: require("../assets/SPARCS.png")
        };
    }
}
</script>