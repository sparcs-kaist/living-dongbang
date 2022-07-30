<template>
  <div class="left-panel"><LoginForm /></div>
  <DongbangMap />
</template>

<script>
import DongbangMap from "../components/DongbangMap.vue";
import LoginForm from "../components/LoginForm.vue";

export default {
  name: "LoginPage",
  components: {
    DongbangMap,
    LoginForm,
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
