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
  font-family: Inter var,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
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
