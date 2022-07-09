<template>

<div id="InsertEntryBox" class="absolute ">
  <!-- <InsertEntry msg="插入單字" ToLocation="/insertword"></InsertEntry> -->
  <InsertEntry msg="新增單字庫" ToLocation="/insertlib"></InsertEntry>
  <InsertEntry msg="修改單字庫" ToLocation="/modifylib"></InsertEntry>
</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import { onMounted } from 'vue'
import InsertEntry from "../components/Create/InsertEntry.vue"

export default {
  name: '',
  components: {
    InsertEntry,
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
    #InsertEntryBox{
        left: 50%;
        transform: translateX(-50%);
        top: 20vh;
        width: 70vh;
        height: 70vh;
        display: flex;
        flex-direction: row;
        align-content: center;
        justify-content: flex-start;
        flex-wrap: wrap;
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