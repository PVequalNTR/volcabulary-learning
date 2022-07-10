<script setup>
    import {gsap} from 'gsap';
</script>

<template>
  <img :src="imgsrc" ref="imag" class="imag w-2/3 h-2/3 " @load="drop()" >
</template>

<script>
export default {

    name: "icon",
    data(){
        return{
            imgsrc: "/mdcpp_icon.png",
        }
    },
    methods:{
        drop(){
            const imag = this.$refs.imag;
            gsap.from(imag,{duration:2,y:"-100vh",ease:"bounce"})
        }
    }

}


</script>

<style>

</style>

