<template>
    <div id="current-clock">
        <div class="date-text">{{ date }}</div>
        <div class="time-text">{{ time }}</div>
    </div>
</template>

<script>
import currentTime from "../helpers/time"

export default {
    data() {
        return {
            timer: null,
            date: "0000.00.00",
            time: "00:00"
        }
    },
    methods: {
        updateTime() {
            const today = new Date()
            const { date, time } = currentTime(today)
            this.date = date
            this.time = time
        }
    },
    mounted() {
        this.timer = setInterval(() => {
            this.updateTime()
        }, 1000)
    },
    beforeUnmount() {
        clearInterval(this.timer)
    }
}
</script>

<style>
#current-clock {
    position: relative;
    padding: 30px;
    padding-top: 20px;
    text-align: center;
    align-items: center;
    background-color: var(--orange);
    border-radius: 10px;
    color: var(--white);
}
.date-text {
    padding-bottom: 10px;
    font-weight: bold;
    font-size: var(--font-middle);
}
.time-text {
    font-weight: bolder;
    font-size: 30px;
}
</style>