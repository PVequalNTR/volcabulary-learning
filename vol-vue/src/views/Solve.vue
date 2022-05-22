<template>
  <div class="solve">
      <h1>{{}}</h1>
    <p>{{sentences[id].name}}</p>
    <input v-model="input" class="border-2">
    <button @click="next" class="w-10 h-10 bg-slate-400"></button>
    {{ answer }}
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import { onMounted } from 'vue'

export default {
  name: 'Solve',
  components: {
  },
  data() {
    return {
        sentences: [{
      	    'id': null, 'name': null
        }],
        answer: [],
        max: 0,
        id: 0,
        input: '',
    }
  },
  mounted() {
    axios
      .get('api/v1/get_sentences/1/')
      .then(res => {
        this.sentences = res.data
        this.max = Object.keys(res.data).length;
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
      submit() {
        /* axios submit */
      },
      next() {
          this.answer.push({
              'id': this.id,
              'input': this.input
          })
          this.id++
          this.input = ''
          if(this.id >= this.max) this.submit()
      }
  }
}
</script>
