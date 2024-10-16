<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: "App",
  components: {},
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Creepster&family=Staatliches&display=swap");

:root {
  --color-red: #8a0303;
  --color-black: #000000;
  --color-dark-gray: #1e1e1e;
  --color-light-gray: #2e2e2e;
  --color-dark-green: #3e4c40;
  --color-light-green: #76993a;
  --color-white: #f5f5f5;
  --color-brown: #c8a165;
  --hover-btn: #860f0f;
  --font-creepster: "Creepster", system-ui;
  --font-staatliches: "Staatliches", sans-serif;
  --font-bebas: "Bebas Neue", sans-serif;
  --radious-defalt: 5px;
}

input {
  font-family: var(--font-staatliches);
}

h1 {
  font-family: var(--font-creepster);
}

p {
  font-family: var(--font-staatliches);
}

body,
html {
  background-color: var(--color-dark-gray);
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  min-height: 300vh;
  width: 100vw;
}

* {
  padding: 0;
  margin: 0;
}
</style>
