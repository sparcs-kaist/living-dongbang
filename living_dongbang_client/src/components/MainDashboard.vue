<template>
    <div>
        <TimeSlider />
        <CurrentClock />
        <WikiQuotes />
    </div>
</template>

<script>
import CurrentClock from './CurrentClock.vue'
import TimeSlider from './TimeSlider.vue';
import WikiQuotes from './WikiQuotes.vue';
export default {
    components: {
        CurrentClock,
        TimeSlider,
        WikiQuotes
    },
    data() {
        return {
            logoImg: require("../assets/SPARCS.png")
        };
    }
}
</script>