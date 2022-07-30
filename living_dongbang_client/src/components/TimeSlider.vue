<template>
    <div id="slider-container">
        <div class="hour-label left">+0h</div>
        <div class="hour-label middle">+12h</div>
        <div class="hour-label right">+24h</div>

        <div class="line-label left">|</div>
        <div class="line-label middle">|</div>
        <div class="line-label right">|</div>

        <input id="time-slider" type="range" min="0" max="24" step="0.5" v-model="addHours">
    </div>
</template>

<script>
export default {
    data() {
        return {
            addHours: 0
        };
    },
    watch: {
        addHours(hours) {
            console.log(hours)
        }
    }
}
</script>

<style>
#slider-container {
    position: relative;
    margin-top: 25px;
}
#time-slider {
    -webkit-appearance: none;
    appearance: none;
    height: 10px;
    background: var(--light-gray);
    padding: 0;
    border: none;
    margin-bottom: 20px;
}
#time-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%; 
  background: var(--dark-orange);
  cursor: pointer;
}
.hour-label {
    position: absolute;
    display: inline-block;
    margin-top: -25px;
}
.line-label {
    position: absolute;
    display: inline-block;
    margin-top: -5px;
    z-index: -1;
}
.left {
    left: 0;
    transform: translateX(calc(-50% + 22px));
}
.middle {
    left: 50%;
    transform: translateX(-50%);
}
.right {
    right: 0;
    transform: translateX(calc(50% - 22px));
}
</style>