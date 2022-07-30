<template>
  <div class="left-panel"><MainDashboard /></div>
  <DongbangMap :reserveStatus="reserveStatus" />
</template>

<script>
import DongbangMap from "../components/DongbangMap.vue";
import MainDashboard from "../components/MainDashboard.vue";

import reserveStatus from "../data/reserveStatus";

export default {
  name: "FrontPage",
  components: {
    DongbangMap,
    MainDashboard,
  },
  data() {
    return {
      reserveStatus: reserveStatus
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
