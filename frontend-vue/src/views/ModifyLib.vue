<template>
  <div id="formbox" class="absolute" >
    <form style="height:100%;width: 100%;display: flex;flex-direction: column;align-items: center;justify-content: space-around;">
      <div id="BuildTitle" >修改單字</div>
      <div class= "select" style="height:30%">
        <div id="SelectTitle" >選擇題庫</div>
        <select id="select">
            <option >first_ca</option>
            <option >second_ca</option>
        </select> 
      </div>
      <div class= "input" style="height:30%">
        <div id="InputTitle" >修改單字</div>
        <input :id="wordInputId" :value="wordinput" @input="wordinput=$event.target.value"> 
      </div>
      <div v-if="notFormat" style="color:red;">輸入格式錯誤</div>
      <button type="button" :disabled="ifbtndisable" id="BuildSendBtn" @click="sent">送出</button>
    </form>
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
      wordinput: "", // 從後端抓單字
      descriptnput:"",
      ifbtndisable: true,
      notFormat:false,
      wordInputId: "in",
      categoryList: [],
    }
  },
  mounted() {
    alert("修改單字時，請使用小寫，有多個單字請以,隔開，否則將無法送出");
    axios.get("api/v1/all_categories/")
    .then( (res) => {
      console.log(res);
      this.categoryList = res.data
      console.log(res.data)
      console.log(this.categoryList)
    } )
    .catch( (err) => { console.log(err)} )
    console.log(this.categoryList,"Q")
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
    },
    sent(){
      var list = this.wordinput.split(",")
      var name = document.getElementById("select").value
      console.log(name)
      axios.post("api/v1/edit_category/"+name,{
          "name": name,
          "description": this.descriptnput,
          "vol_list": list,
        }
      )
      .then((res)=>{
        console.log(res);
        this.libname="";
        this.descriptnput="";
        this.wordinput="";
      })
      .catch((err) => {
        console.log(err);
        alert(err.response.data.info);
      })
    }
  },
  watch:{
    wordinput: function(){
      var str = this.wordinput
      console.log("~"+str)
      if(str==""){
        this.notFormat=false; 
        this.wordInputId = "in"
        console.log("empty")         
      }
      for(var i=0;i<str.length;i++ ){
        if(str[i]==',' || (str[i].charCodeAt()>=97 && str[i].charCodeAt()<=122)){
          console.log("able");
          this.ifbtndisable = false;
          this.notFormat=false;
          this.wordInputId = "in"
        }
        else{
          console.log("disable");
          this.ifbtndisable = true; 
          this.notFormat=true;
          this.wordInputId = "ErrorIn"
        }
      }
    }
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
        text-align: center;
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
    #select{
        height: 50%;
        width: 60%; 
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