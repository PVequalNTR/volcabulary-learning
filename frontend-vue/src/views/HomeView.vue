<template>
  <div class="home">
    <CenterCom></CenterCom>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import { onMounted } from 'vue'
import CenterCom from "../components/CenterCom/Component.vue"
export default {
  name: 'HomeView',
  components: {
      CenterCom,
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