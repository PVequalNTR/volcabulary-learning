<script setup>
import {gsap} from "gsap"
import icon from "./Icon.vue";
import btn from "./btn.vue"
</script>

<template>
    <div id="box" class="absolute" @click="into()" >
        <icon ref="imag"></icon>
        <btn msg="教學" ></btn>
        <btn ref="btn"></btn>
        <btn></btn>
    </div>
</template>

<script>
export default {
    name: "Comopnent",
    components: {
        icon,
        btn,
    },
    methods:{
        into(){
            console.log(this)
            const imag = this.$refs.imag;
            const btn = this.$refs.btn;
            // const timeline = gsap.timeline({defaults:{duration:1}});
            gsap.from(imag,{duration:1,y:"-100vh",ease:"bounce"})
            gsap.from(btn,{delay:1, duration:1, opacity:0,})
        }
    }
}
</script>

<style>

    #box{

        
        left: 50%;
        transform: translateX(-50%);
        top: 20vh;
        width: 70vh;
        height: 70vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        
    }

</style>