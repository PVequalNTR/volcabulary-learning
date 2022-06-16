<template>
    <div class= "input">
        <div id="InputTitle">{{Msg}}</div>
        <input id="in"> 
    </div>
</template>

<script>
import Default from '../../views/default.vue'
import btn from '../CenterCom/btn.vue'

export default {
  components: { btn, Default },

    props:{
        Msg:{
            type:String,
            default: "預設文字",
        },
    },
    data(){
        return{
        }
    }

}
</script>

<style>

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
    #InputTitle{
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


</style>