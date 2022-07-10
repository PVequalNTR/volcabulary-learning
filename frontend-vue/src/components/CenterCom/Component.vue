<script setup>
import {gsap} from "gsap"
import icon from "./Icon.vue";
import btn from "./btn.vue"
</script>

<template>
    <div id="box" class="absolute" >
        <icon ></icon>
        <btn msg="歡迎來到文意字彙解題網站 !"></btn>
        <btn msg="參閱教學" jump="https://hackmd.io/@MingdaoCP/SJXthxDF5"></btn>
        
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