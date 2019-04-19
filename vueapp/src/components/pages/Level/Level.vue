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
        <b-nav-item-dropdown class="Switch-stap">
          <template slot="button-content"><span style="color:#33678f"><b>Типы и модель данных</b></span></template>
          <b-dropdown-item href="#1"><span style="color:#33678f">1.Типы данных в Python</span></b-dropdown-item>
          <b-dropdown-item href="#2"><span style="color:#33678f">2.Модель данных</span></b-dropdown-item>
          <b-dropdown-item href="#3"><span style="color:#33678f">3.Изменяемые и неизменяемые типы данных</span></b-dropdown-item>
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
             <h4 class="theory-title">Типы данных в Python</h4>
             <div class="texting">
             <p>В Python типы данных можно разделить на встроенные в интерпретатор (built-in) и не встроенные, которые можно использовать при импортировании соответствующих модулей.</p>

             <h6>К основным встроенным типам относятся:</h6>
             <ul>
               <li>None (неопределенное значение переменной)</li>
               <li>Логические переменные (Boolean Type)</li>
               <li>Числа (Numeric Type)
                 <ul>
                  <li>int – целое число</li>
                  <li>float – число с плавающей точкой</li>
                  <li>complex – комплексное число</li>
                 </ul>
               </li>
               <li>Списки (Sequence Type)
                 <ul>
                   <li>list – список</li>
                   <li>tuple – кортеж</li>
                   <li>range – диапазон</li>
                 </ul>
               </li>
               <li>Строки (Text Sequence Type )
                 <ul>
                   <li>str</li>
                 </ul>
               </li>
               <li>Бинарные списки (Binary Sequence Types)
               <ul>
                 <li>bytes – байты</li>
                 <li>memoryview – специальные объекты для доступа к внутренним данным объекта через protocol buffer</li>
                 <li>bytearray – массивы байт</li>
               </ul>
             </li>
               <li> Множества (Set Types)
                 <ul>
                   <li> set – множество</li>
                   <li>frozenset – неизменяемое множество</li>
                 </ul>
               </li>
               <li> Словари (Mapping Types)
                 <ul>
                   <li> dict – словарь</li>
                 </ul>
               </li>
             </ul>
             </div>
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
  .texting{
    margin-left: 5%;
    margin-right: 5%;
    text-align: left;
  }
  .Switch-stap{

    text-align: center;
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
