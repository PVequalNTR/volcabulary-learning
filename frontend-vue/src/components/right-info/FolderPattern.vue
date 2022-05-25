<template>
  <div class="absolute w-56 right-5 ">
      <img :src="imgsrc" class="absolute w-full z-0">
      <div class="relative font-sans w-48 mt-14 text-gray-100 z-10 text-4xl" style="left:8%;">{{DataInfo}}</div>
      <div class="relative font-sans w-48 mt-3 text-gray-100 text-center text-6xl z-10" style=" left:8%;">{{DataNum}}</div>
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
    top:290px; /*+210*/
}
#folder3{
    top: 500px;
}

</style>