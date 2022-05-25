<template>
  <div class="home">
    {{ sentences }}
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import { onMounted } from 'vue'

export default {
  name: 'HomeView',
  components: {
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
