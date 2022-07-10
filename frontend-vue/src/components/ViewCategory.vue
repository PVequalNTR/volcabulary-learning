<template>
<div class="modal">
  <div class="rounded-lg w-1/2 h-2/3 px-16 py-8 overflow-scroll" >
    <div class="h-10">
      <button @click="$router.go(-1)" class="h-5 w-5 float-right">
          <i class="fa-solid fa-x float-right"></i>
      </button>
    </div>
    <p class="font-bold mb-6 text-4xl">{{ name }}</p>
    <p class="my-4 text-lg font-semibold">{{ description }}</p>
    <div class="flex flex-row">
      <button @click="viewlist = !viewlist" class="text-lg my-4 p-4 rounded shadow-lg bg-amber-400 text-white text-center font-semibold mr-2">單字列表</button>
      <router-link :to="{ path:'/solve', query:{id: id}}" class="text-lg my-4 p-4 rounded shadow-lg bg-green-400 text-white text-center font-semibold ml-2">開始測驗</router-link>
    </div>
    <div v-if="viewlist === true" class="my-4 rounded-lg shadow-lg p-4 border-blue-200 border-2 ">
      <p v-for="word of words">{{ word }}</p>
    </div>
    
  </div>
</div>
    
</template>
<script>
import axios from 'axios'

export default {
    name: 'ViewCategory',
    data() {
        return { 
            modalOpen: false,
            viewlist: false,
            id: 0,
            name: '',
            words: [],
            description: '',
        }
    },
    mounted() {
        this.id = axios
          .get('api/v1/get_category/' + this.$route.query.id)
          .then(response => {
            this.name = response.data.name
            this.words = response.data.vol_list
            this.description = response.data.description
            this.id = response.data.id
            console.log(response)
          })
          .catch(err => {
            console.log(err)
          })
    },
}
</script>
<style scoped>
.modal {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  background-color: rgba(0,0,0,.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal div {
  background-color: white;
}
</style>