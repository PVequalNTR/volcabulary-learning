<template>
  <div class="absolute w-56 right-5 px-5">
      <img :src="imgsrc" class="absolute w-56 m-0 z-0">
      <div class="relative w-48 h-9 mt-14 ml-5 mr-5 text-gray-100 z-10 text-4xl">{{DataInfo}}</div>
      <div class="relative font-sans w-48 mt-4 mx-5  text-gray-100 text-center text-6xl z-10">{{DataNum}}</div>
  </div>
</template>

<script>
export default {
    name:"folder",
    props:{
        DataInfo:{
            type:String,
            default:"default msg",
        },
        DataNum:{
            type:Number,
            default:0,
        }
    },
    data(){
        return{
        imgsrc: "src/assets/folder.png",
        }
    }



}
</script>

<style>

#folder1{
    top: 80px; 
}
#folder2{
    top:290px; /*+190*/
}

</style>