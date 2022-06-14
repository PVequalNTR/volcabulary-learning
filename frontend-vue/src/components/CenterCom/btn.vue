<script setup>
    import {gsap} from 'gsap';
</script>


<template>
  <button id="btn" ref="btn" @click="into()">{{ msg }}</button>
</template>

<script>
export default {
    props:{
        msg:{
            type:String,
            default:"功能施工中",
        }
    },
    methods:{
        into(){
            console.log("!@#")
            const btn = this.$refs.btn;
            gsap.from(btn,{duration:1,opacity:0})
        }
    }
}
</script>

<style>

    #btn{
        height: 10%;
        width: 90%;
        margin: 5px;
        border-radius: 15px;
        background-color: #4CAF50;
        color: black;
        text-align: center;
        font-size: 180%;
        font-weight:600;
    }
    #btn:hover{
        border:3px solid;
        border-color: #4CAF50;
        background-color: white;
    }

</style>