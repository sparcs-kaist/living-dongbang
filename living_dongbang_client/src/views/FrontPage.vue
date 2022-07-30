<template>
  <div class="left-panel"><MainDashboard /></div>
  <DongbangMap />
</template>

<script>
import DongbangMap from "../components/DongbangMap.vue";
import MainDashboard from "../components/MainDashboard.vue";

export default {
  name: "FrontPage",
  components: {
    DongbangMap,
    MainDashboard,
  },
  data() {
    return {
      user: "null",
    };
  },
};
</script>

<style>
.left-panel {
  display: inline-block;
  position: relative;
  width: 300px;
  vertical-align: top;
  padding: 50px;
}
</style>
