<template>
  <div id="formbox" class="absolute" >
      <div id="BuildTitle">插入單字</div>
      <SelectData Msg="選擇題庫"></SelectData>
      <InputData Msg="單字名稱"></InputData>
      <button id="BuildSendBtn">送出</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import { onMounted } from 'vue'
import InputData from "../components/Create/InputData.vue"
import SelectData from "../components/Create/SelectData.vue"

export default {
  name: '',
  components: {
    InputData,
    SelectData,
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
<style>
    #formbox{
        background-color: #94D8FF;
        left: 50%;
        transform: translateX(-50%);
        top: 20vh;
        width: 70vh;
        height: 40vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        border-width: 2px;
        border-color: black;
    }
    #BuildTitle{
      height: 30px;
      font-size: 30px;
      font-weight: 600;
      color:black;
    }
    #BuildSendBtn{
        height: 8%;
        width: 20%;
        border-radius: 15px;
        background-color: #4CAF50;
        color: black;
        text-align: center;
        font-size: 20px;
        font-weight:600;
    }
    #BuildSendBtn:hover{
        border:3px solid;
        border-color: #4CAF50;
        background-color: white;
    }

</style>>