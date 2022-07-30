<template>
  <div class="left-panel" v-if="user"><MainDashboard /></div>
  <div class="left-panel" v-else><LoginForm /></div>
  <DongbangMap />
</template>

<script>
import DongbangMap from './components/DongbangMap.vue'
import LoginForm from './components/LoginForm.vue'
import MainDashboard from './components/MainDashboard.vue'

export default {
  name: 'App',
  components: {
    DongbangMap,
    LoginForm,
    MainDashboard
  },
  data() {
    return {
      user: "null"
    }
  }
}
</script>

<style>
@import url('//fonts.googleapis.com/css?family=Raleway');
@import url('https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@1.0/nanumsquare.css');

:root {
  --orange: #EBA12A;
  --dark-orange: #EC8F26;
  --white: #FFFFFF;
  --light-gray: #BBBBBB;
  --gray: #777777;
  --dark-gray: #333333;
  --black: #000000;
  --green: #2AEBA1;
  --pink: #EB2A74;
  --blue: #2A74EB;
  --beige: #FEF8EF;
  --font-eng: Raleway;
  --font-kor: NanumSquare;
  --font-small: 12px;
  --font-middle: 14px;
  --font-large: 16px;
}
#app {
  font-family: NanumSquare, Raleway, Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: var(--dark-gray);
}
.left-panel {
    display: inline-block;
    position: relative;
    width: 300px;
    vertical-align: top;
    padding: 50px;
}
</style>
