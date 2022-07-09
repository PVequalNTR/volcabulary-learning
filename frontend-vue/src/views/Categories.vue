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
        page: 1,
    }
  },
  mounted() {
    axios
      .get('api/v1/all_categories/')
      .then(res => {
        this.categories_list = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    change(pk) {
      this.page += pk
      axios
        .get('api/v1/latest_categories/' + this.page + '/')
        .then(response => {
          this.categories_list.splice(1, this.categories_list.length)
          for(var i = 0; i < res.data.length; i++) {
            this.categories_list.push(res.data[i])
          }
          console.log(response)
        })
        .catch(err => {
          console.log(err)
          this.page -= pk
        })
      }
    }
  }
</script>
