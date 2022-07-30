<template>
  <router-view />
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
@import url("//fonts.googleapis.com/css?family=Raleway");
@import url("https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@1.0/nanumsquare.css");

:root {
  --orange: #eba12a;
  --dark-orange: #ec8f26;
  --white: #ffffff;
  --light-gray: #bbbbbb;
  --gray: #777777;
  --dark-gray: #333333;
  --black: #000000;
  --green: #2aeba1;
  --pink: #eb2a74;
  --blue: #2a74eb;
  --beige: #fef8ef;
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
</style>
