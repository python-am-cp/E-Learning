<template>
  <div class="Level-container">
    <b-navbar class="NB" fixed = top toggleable="sm">
      <b-navbar-brand class="NB-brand" href=""><span style="color:#FFFFFF">E-Learning</span></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav role="navigation" class="ml-auto">
          <b-nav-item class="nav-item" href="/"><span style="color:#E0FFFF">ELP</span></b-nav-item>
          <b-nav-item class="nav-item" href=""><span style="color:#E0FFFF">О ПРОЕКТЕ</span></b-nav-item>
          <b-nav-item class="nav-item" href="login"><span style="color:#E0FFFF">ВХОД</span></b-nav-item>
          <b-nav-item class="nav-item" href="level"><span style="color:#E0FFFF">НАЧАТЬ ОБУЧЕНИЕ</span></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
  export default {}
</script>
<style  lang="scss" scoped>
  body {
    //  background: url('./img/im1.jpg');
    width: 100%;
    height: 100%;
  }
  .NB {
    background-color: #09151A;
    height: 9%;
    //position: fixed = top;
  }
  .NB-brand{
    color: #FFFFFF;
    margin: 0 0 0 20px;
  }
  .ml-auto{

    margin:  0 20px 0 0;
  }
  .nav-item{
    margin:  0 10px 0 10px;
  }
  .promo-block {
    position: relative;
    z-index: 1;
    background-size: cover;
    padding: 320px 200px 230px 5%;
  }
  .promo-block-title{
    color:#E0FFFF;
  }
  .promo-block-text{
    color:#E0FFFF;
  }
</style>
