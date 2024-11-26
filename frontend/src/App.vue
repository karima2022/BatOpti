<template>
  <NavBar/>

  <div id="app">
    <router-view />
  </div>
</template>

<script>

import NavBar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@media (prefers-color-scheme: light) {
    .logo {
        filter: invert(1) hue-rotate(180deg); /* Inverse les couleurs et ajuste les teintes */
    }
}


</style>
