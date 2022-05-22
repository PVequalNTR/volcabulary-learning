<template>
  <Navbar></Navbar>
  <router-view/>
</template>

<script>
import Navbar from './components/Navbar.vue';
export default {
  name: 'root',
  components: {
    Navbar,
  } 
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}
</style>
