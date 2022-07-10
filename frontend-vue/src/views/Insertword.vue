<template>
  <div id="formbox" class="absolute" >
    <div style="height:100%;width: 100%;display: flex;flex-direction: column;align-items: center;justify-content: space-around;">
      <div id="BuildTitle">插入單字</div>
      <div class= "select" style="height:30%">
        <div id="SelectTitle" >選擇題庫</div>
        <select id="in">
            <option>first_ca</option>
            <option>second_ca</option>
        </select> 
      </div>
      <div class= "input" style="height:30%">
        <div id="InputTitle" >輸入單字</div>
        <input id="in" :value="wordinput" @input="wordinput=$event.target.value"> 
      </div>
      <button type="submit" :disabled="ifbtndisable" id="BuildSendBtn">送出</button>
    </div>
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
      wordinput: "",
      ifbtndisable: true,
    }
  },
  mounted() {
    //alert("輸入單字時，請使用小寫，有多個單字請以,隔開，否則將無法送出");
    /*axios
      .get('api/v1/sentence/worthwhile/')
      .then(res => {
        this.sentences = res.data
      })
      .catch(err => {
        console.log(err)
      })*/
  },
  methods:{
    FormatJudge(){
      console.log(this.wordinput);
      return true;
    }
  },
  watch:{
    wordinput: function(){
      var str = this.wordinput
      console.log(str)
      for(var i=0;i<str.length;i++ ){
        if(str[i]==',' || (str[i].charCodeAt()>=97 && str[i].charCodeAt()<=122)){
          console.log("able");
          this.ifbtndisable = false;
        }
        else{
          console.log("disable");
          this.ifbtndisable = true;          
        }
      }

    }
  }
}
</script>
<style>
    #formbox{
        background-color: #a0d5f4;
        left: 50%;
        transform: translateX(-50%);
        top: 20vh;
        width: 70vh;
        height: 60vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        border-radius: 15px;
        border-width: 3px;
        border-color: rgb(26, 118, 60);
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
    .input{
        /* background-color: red; */
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 100%;
        height: 15%;
    }
    #in{
        height: 50%;
        width: 60%;
        border-width: 2px;
        border-color: black;
    }
    #ErrorIn{
        height: 50%;
        width: 60%;
        border-width: 2px;
        border-color: red;
    }
    #InputTitle{
        border-radius: 15px;
        height: 50%;
        width: 20%;
        background-color: #4CAF50;
        font-size: 20px;
        font-weight: 600;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;;
    }
    .select{
        /* background-color: red; */
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 100%;
        height: 15%;
    }
    #in{
        height: 50%;
        width: 60%;
    }
    #SelectTitle{
        border-radius: 15px;
        height: 50%;
        width: 20%;
        background-color: #4CAF50;
        font-size: 20px;
        font-weight: 600;
        display: flex;
        justify-content: center;
        align-items: center;
        color: black;
    }

</style>>