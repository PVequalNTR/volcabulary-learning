<template>
    <div class="justify-center flex">
        <div class="w-3/5 mt-6">
            <h1 class="text-3xl font-bold text-left">題庫列表</h1>
            <div class="grid grid-cols-5 gap-4 mt-8">
                <router-link v-for="item of categories_list" :to="{ path:'/categories/view', query:{id:item.id}}" class="p-4 rounded-lg shadow-lg bg-indigo-400 text-white text-center font-bold" >
                {{ item.name }}
                </router-link>
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import { onMounted } from 'vue'

export default {
  name: 'Categories',
  components: {
},
  data() {
    return {
        categories_list: [],
        modalopen: false,
        name: '',
        vol_list: [],
        description: '',
    }
  },
  mounted() {
    axios
      .get('api/v1/latest_categories/1/')
      .then(res => {
        this.categories_list = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>
