<template>
  <nav class="bg-white h-20 px-4 py-2 flex flex-row">
    <router-link to="/" class="h-full flex items-center basis-1/2 hover:text-sky-700 hover:border-b-green-400">
      <img :src="'/mdcpp_icon.png'" alt="mdcpp_icon" class="h-full mx-4"/>
      <span class="text-2xl font-semibold hover:text-sky-700">文意字彙線上平台</span>
    </router-link>
    <ul class="h-full flex items-center text-lg flex-row-reverse basis-1/2">
      <!--<li class="basis-1/6">
        <router-link to="" v-if="login === true" class="rounded bg-blue-600 text-white px-6 py-3">帳號</router-link>
        <router-link to="" v-else class="rounded bg-blue-600 text-white px-6 py-3">登入</router-link>
      </li>-->
      <li class="basis-1/6 ">
        <router-link to="/about" class="rounded bg-blue-600 text-white px-6 py-3">介紹</router-link>
      </li>
      <li class="basis-1/6">
        <router-link to="/Categories" class="hover:text-sky-700 p-2 hover:border-b-green-400 hover:border-b-2">開始</router-link>
      </li>
      <li class="basis-1/6">
        <router-link to="/build" class="hover:text-sky-700 p-2 hover:border-b-green-400 hover:border-b-2">建立</router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    login: Boolean
  }
}
</script>
