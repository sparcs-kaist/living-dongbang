<template>
  <div class="left-panel"><LoginForm /></div>
  <DongbangMap :reserveStatus="reserveStatus" />
</template>

<script>
import DongbangMap from "../components/DongbangMap.vue";
import LoginForm from "../components/LoginForm.vue";

import reserveStatus from "../data/reserveStatus";

export default {
  name: "LoginPage",
  components: {
    DongbangMap,
    LoginForm,
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
