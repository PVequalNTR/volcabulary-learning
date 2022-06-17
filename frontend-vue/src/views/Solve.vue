<template>
  <div class="justify-center flex">
    <div class="w-2/3 my-16">
        <h1 class="font-bold text-4xl mb-10">{{ $route.query.name }}</h1>
        <div class="border-2 rounded shadow-xl border-green-400">
            <div v-for="(sentence, index) in sentences" class="flex my-4">
                <input v-model="input[index]" class="p-2 ml-5 mr-20 border-2 rounded"/><span class="leadint-none relative font-semibold">{{sentence.name}}</span>
            </div>
            <button @click="submit" type="submit" class="text-white ml-5 p-2 rounded-md mb-4 border-2 border-blue-500 bg-blue-500">提交</button>
        </div>
    </div>
    <ViewResult v-if="submitted === true" :score="score" :name="$route.query.name"></ViewResult>
    
  </div>

</template>

<script>
// @ is an alias to /src
import ViewResult from '@/components/ViewResult.vue'
import axios from 'axios'
import { onMounted } from 'vue'

export default {
  name: 'Solve',
  components: {
    ViewResult
  },
  data() {
    return {
        sentences: [{
      	    'id': null, 'name': null
        }],
        max: 0,
        input: [],
        answer: [],
        score: 0,
        submitted: false,
    }
  },
  mounted() {
    axios
      .get('api/v1/get_sentences/' + this.$route.query.id)
      .then(res => {
        this.sentences = res.data
        this.max = Object.keys(res.data).length
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
      submit() {
          for(var i = 0; i < this.max; i++) {
              this.answer.push({
                  id: this.sentences[i].id,
                  word: this.input[i]
              })
          }
          axios.post('/api/v1/check/' + this.$route.query.name, this.answer)
          .then(response => {
              this.score = Math.round(JSON.parse(response.data).score / this.max * 1000) / 10
              this.submitted = true
          })
          .catch(err => {
            console.log(err)
          })
      },
  }
}
</script>
