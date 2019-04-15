<template>
  <div class="Level-container" fixed = top>
    <b-navbar class="NB" fixed = top toggleable="sm">
      <b-navbar-brand class="NB-brand" href=""><span style="color:#FFFFFF">E-Learning</span></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <div class="course-nav main-nav__course-nav">
      </div>
      <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="switch-nav">
        <b-nav-form>

        </b-nav-form>
        <b-nav-item-dropdown text="Типы данных">
          <b-dropdown-item href="#"><span style="color:#E0FFFF">EN</span></b-dropdown-item>
          <b-dropdown-item href="#"><span style="color:#E0FFFF">ES</span></b-dropdown-item>
          <b-dropdown-item href="#"><span style="color:#E0FFFF">RU</span></b-dropdown-item>
          <b-dropdown-item href="#"><span style="color:#E0FFFF">FA</span></b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-form>

        </b-nav-form>
      </b-navbar-nav>

        <b-navbar-nav role="navigation" class="ml-auto">
          <b-nav-item class="nav-item" href="/"><span style="color:#E0FFFF">ELP</span></b-nav-item>
          <b-nav-item class="nav-item" href=""><span style="color:#E0FFFF">О ПРОЕКТЕ</span></b-nav-item>
          <b-nav-item class="nav-item" href="login"><span style="color:#E0FFFF">ВЫХОД</span></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
   <article class="course-layout" fixed = top data-taskid="1">
     <div class="theory" >
       <b-row class="text-center">
         <b-col >
           <div class="main-theory-title">
             <h1 class="theory-title">Типы данных</h1>
           </div>
         </b-col>
       </b-row>
       <b-row class="text-right">

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
  .Level-container{

  }
  .theory{
    text-align: start;
    width: 100%;
    margin: 0 auto;
    margin-left: 0%;
    margin-right: 0%;
  }
  .switch-nav{
    color: #FFFFFF;
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
    padding-bottom: 2%;
    border-bottom: 1px solid rgba(100,100,100,.3)
  }

</style>
