<template>
  <div class="home">
    {{ sentences }}
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import { onMounted } from 'vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data() {
    return {
      sentences: [],
    }
  },
  mounted() {
    /*axios
      .get('api/v1/sentence/worthwhile/')
      .then(res => {
        this.sentences = res.data
      })
      .catch(err => {
        console.log(err)
      })*/
  }
}
</script>
