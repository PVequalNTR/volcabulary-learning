<template>
  <nav class="bg-white h-20 px-4 py-2 flex flex-row">
    <router-link to="/" class="h-full flex items-center basis-1/2 hover:text-sky-700">
      <img src="@/assets/mdcpp_icon.png" alt="mdcpp_icon" class="h-full mx-4"/>
      <span class="text-2xl font-semibold hover:text-sky-700">文意字彙線上平台</span>
    </router-link>
    <ul class="h-full flex items-center text-lg flex-row-reverse basis-1/2">
      <li class="basis-1/6 ">
        <router-link to="" class="hover:text-sky-700 border-2 rounded p-2">介紹</router-link>
      </li>
      <li class="basis-1/6">
        <router-link to="" v-if="login === true" class="hover:text-sky-700 border-2 rounded p-2">帳號</router-link>
        <router-link to="" v-else class="hover:text-sky-700 border-2 rounded p-2">登入</router-link>
      </li>
      <li class="basis-1/6">
        <router-link to="" class="hover:text-sky-700 border-2 rounded p-2">開始</router-link>
      </li>
    </ul>
  </nav>
  <hr>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    login: Boolean
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
