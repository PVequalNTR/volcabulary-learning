<template>
  <div class="justify-center flex">
    <div class="w-2/3 my-16">
        <div v-if="submitted === true"></div>
        <div class="grid grid-cols-2">
          <h1 class="font-bold text-4xl mb-10 ">{{ name }}</h1>
          <h3 v-if="submitted" class="font-bold text-4xl mb-10 text-right" :class="{'text-red-600': score != 100 ,'text-green-400': score == 100}">Point : {{ score }}</h3>
        </div>
        <div class="border-2 rounded shadow-xl border-green-400">
            <div v-for="(sentence, index) in sentences" class="flex my-4">
                <input :disabled="submitted" :class="{'line-through': submitted && !correct[index], 'text-red-600': submitted && !correct[index], 'text-green-500': submitted && correct[index]}" v-model="input[index]" class="p-2 ml-5 mr-5 border-2 rounded"/>
                <button v-if="submitted" class="hover:text-blue-400 mr-5 border-slate-200 border-2 rounded bg-slate-200" @click="open(index)">翻譯</button>
                <span class="leadint-none relative font-semibold items-center block">{{ index + 1 }}.&nbsp{{sentence.name}}</span>
            </div>
            <button :disabled="submitted" @click="submit" type="submit" class="text-white ml-5 p-2 rounded-md mb-4 border-2 border-blue-500 bg-blue-500" :class="{'bg-blue-400': submitted, 'border-blue-400': submitted}">提交</button>
        </div>
    </div>
    <ViewChinese v-if="view != -1" :sentence="sentences[view].name" :chinese="chinese[view]" v-on:close="view = -1"></ViewChinese>
    
  </div>

</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import { onMounted } from 'vue'
import ViewChinese from '@/components/ViewChinese.vue'
export default {
  name: 'Solve',
  components: {
    ViewChinese,
  },
  data() {
    return {
        sentences: [{
      	    'id': null, 'name': null
        }],
        max: 0,
        input: [],
        score: 0,
        submitted: false,
        chinese: [],
        name: '',
        correct: [],
        answer: [],
        view: -1,
    }
  },
  mounted() {
    axios.get('api/v1/get_category/' + this.$route.query.id)
      .then(res => {
        this.name = res.data.name
      }),
    axios
      .get('api/v1/get_sentences/' + this.$route.query.id)
      .then(res => {
        this.sentences = res.data
        this.max = Object.keys(res.data).length
        for(var i = 0; i < this.max; i++) {
          this.input.push('')
        }
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
      submit() {
          if(this.submitted) return
          for(var i = 0; i < this.max; i++) {
              this.answer.push({
                  id: this.sentences[i].id,
                  word: this.input[i],
              })
              console.log(this.answer)
          }
          axios.post("api/v1/check/", this.answer)
          .then(response => {
              this.score = (Math.round(response.data.score / this.max * 1000) / 10),
              this.submitted = true
              this.chinese = response.data.chinese
              this.correct = response.data.correct
          })
          .catch(err => {
            console.log(err)
          })
      },
      open(index) {
        this.view = index
      },
  }
}
</script>
