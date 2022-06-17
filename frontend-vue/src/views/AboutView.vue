<template>
  <div id="box" class="absolute">
    <div id="AboutTitle">介紹</div>
    <p id="AboutContent">
      這個網站是為了讓大家練習英文段考的文意字彙而建立。
      <br><br>
      當初因為我們在英文考試中，常常因為文意字彙這種需要通
      靈的題目而掉分，因此想要來好好地練一下文意字彙。
      <br><br>
      不過能用的資源就只有習作跟一些考卷，這些題目對我們
      而言是不太足夠的，所以我們就想，既然題目不夠，那就
      自己抓吧!這個網站的構想也因此誕生。
      <br><br>
      在這個網站中，我們採用Vue作為前端的框架，以Django作
      為後端，以Postgresql作為資料庫
      <br><br>
      因為技術不足(對以上技術不算熟悉)，雖然現在這個網站還
      不成熟，但希望之後能繼續補足精進這個網站。
    </p>
    <div class="absolute font-semibold text-xl" style="right: 0%;bottom:0% ">網站開發者 : 楊翔宇、謝侑哲</div>
  </div>
</template>




<style>


  #AboutTitle{
    font-size: 30px;
    font-weight: 600;
  }
  #AboutContent{
    width: 100%;
    font-weight: 600;
    font-size: 20px;
  }

</style>