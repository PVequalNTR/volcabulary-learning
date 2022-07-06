<template>
<div class="result">
  <div class="rounded-lg w-1/2 h-2/3 px-16 py-12 border-4 border-blue-500">
      <button class="h-5 w-5 float-right" @click="close()">
          <i class="fa-solid fa-x float-right"></i>
      </button>
      <p class="font-bold text-2xl mb-10">原文 : {{ sentence }}</p>
      <span class="font-bold text-2xl">翻譯 : {{ chinese }}</span>
  </div>
</div>
    
</template>
<script>
export default {
    name: 'ViewChinese',
    props: {
      sentence: String,
      chinese: String,
    },
    methods: {
      close() {
        this.$emit('close'); 
      }
    }
}
</script>
<style scoped>
.result {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  background-color: rgba(0,0,0,.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.result div {
  background-color: white;
}
</style>