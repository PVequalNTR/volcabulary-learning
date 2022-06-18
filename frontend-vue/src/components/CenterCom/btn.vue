<script setup>
    import {gsap} from 'gsap';
</script>


<template>
  <button id="btn" ref="btn" @click="webJump()">{{ msg }}</button>
</template>

<script>
export default {
    props:{
        msg:{
            type:String,
            default:"功能施工中",
        }, 
        second:{
            type:String,
            default:"0",
        }, // btn time delat
        jump:{
            type:String,
            default:"None"
        } // web to go
        
    },
    methods:{
        webJump(){
            const herf = this.$props.jump
            if(herf != "None"){
                window.open(herf);
            }
        }
    },
    mounted(){
        const btn = this.$refs.btn
        console.log(this)
        const sec = Number(this.$props.second)
        console.log(sec,typeof(sec))
        console.log("btn mounted")
        gsap.from(btn,{delay:2+sec,duration:1,opacity:0,stagger:0.5})
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