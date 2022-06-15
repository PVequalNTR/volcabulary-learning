<template>
<div class="result">
  <div class="rounded-lg w-1/2 h-2/3 px-16 py-12 border-4 border-blue-500">
      <router-link to="/Categories" class="h-5 w-5 float-right">
          <i class="fa-solid fa-x float-right"></i>
      </router-link>
      <p class="font-bold text-2xl">{{ name }}</p>
      <span class="font-bold text-2xl">分數：</span>
      <span class="font-bold text-2xl">{{ score }}</span>
  </div>
</div>
    
</template>
<script>

export default {
    name: 'ViewResult',
    props: {
      name: String,
      score: Number
    },
    data() {
        return { 
        }
    },
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