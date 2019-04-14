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
   <article class="course-layout" fixed = top data-taskid="1">
     <div class="theory" >
       <b-row>
         <b-col cols="8">
           <div class="main-theory-title">
             <h1 class="theory-title">Типы данных</h1>
           </div>
         </b-col>
         <b-col cols="4">

         </b-col>
       </b-row>
     </div>
   </article>
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
  .theory{
    text-align: start;
  }
  //text-align : center
  .course-layout {
    margin: 0 auto;
    padding-top: 7%;
    display: flex;
    flex-grow: 1;
    height: 1200px;
    width: 70%;
    font-size: 14px;
    background-color: #FFFFFF;
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
  .theory-title{
    color: black;
    font-size: x-large;
    text-align: center;
  }

</style>
