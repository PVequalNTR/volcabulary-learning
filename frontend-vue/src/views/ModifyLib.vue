<template>
  <div id="formbox" class="absolute" >
    <div style="height:100%;width: 100%;display: flex;flex-direction: column;align-items: center;justify-content: space-around;">
      <div id="BuildTitle" >修改單字</div>
      <div class= "select" style="height:30%">
        <div id="SelectTitle" >選擇題庫</div>
        <select id="select" @change="SelectCategory">
            <option></option>
            <option v-for="(item,index) in categoryList" :key="index" :value="item.id" >{{ item.name }}</option>
        </select> 
      </div>
      <div class= "input" style="height:30%">
        <div id="InputTitle" >修改名稱</div>
        <input id="in" :value="libname" @input="libname=$event.target.value"> 
      </div>
      <div class= "input" style="height:30%">
        <div id="InputTitle" >修改敘述</div>
        <input id="in" :value="descriptinput" @input="descriptinput=$event.target.value"> 
      </div>
      <div class= "input" style="height:30%">
        <div id="InputTitle" >修改單字</div>
        <input :id="wordInputId" :value="wordinput" @input="wordinput=$event.target.value"> 
      </div>
      <div v-if="notFormat" style="color:red;">輸入格式錯誤</div>
      <button type="button" :disabled="ifbtndisable" id="BuildSendBtn" @click="sent">送出</button>
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
      libname:"",
      wordinput: "",
      descriptinput: "",
      ifbtndisable: true,
      notFormat:false,
      wordInputId: "in",
      categoryList: [],
    }
  },
  mounted() {
    //alert("修改單字時，請使用小寫，有多個單字請以,隔開，否則將無法送出");
    axios.get("api/v1/all_categories/")
    .then( (res) => {
      this.categoryList = res.data
    } )
    .catch( (err) => { console.log(err)} )
  },
  methods:{
    FormatJudge(){
      console.log(this.wordinput);
      return true;
    },
    sent(){
      var list = this.wordinput.split(",")
      var id = document.getElementById("select").value
      console.log(this.libname,this.descriptinput,typeof(this.libname),typeof(this.descriptinput))
      for(var i=0;i<this.categoryList.length;i++){
        if(this.categoryList[i].id==parseInt(id)) name = this.categoryList[i].name
      }
      axios.post("api/v1/edit_category/"+id,{
          "name": this.libname,
          "description": this.descriptinput,
          "vol_list": list,
        }
      )
      .then((res)=>{
        console.log(res);
        this.libname="";
        this.descriptinput="";
        this.wordinput="";
      })
      .catch((err) => {
        console.log(err);
        var errorword = err.response.data.info.split(" ")[2]
        alert("找不到單字"+errorword);
      })
    },
    SelectCategory(){
      console.log("selected")
      axios.get("api/v1/get_category/"+document.getElementById("select").value)
      .then( (res) => {
        this.wordinput = res.data.vol_list.join(",")
        this.descriptinput =  res.data.description;
        this.libname = res.data.name
      } )
      .catch( (err) => console.log(err) )
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
          break;
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
        border-width: 2px;
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
        border-width: 2px;
        border-color: black;
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