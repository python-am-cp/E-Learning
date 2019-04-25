<template>
  <div id="app-2">
    <v-container>
      <router-view/>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="scss">
  @import "./assets/styles";
  body {
    background: url('./assets/images/im1.jpg') no-repeat center center fixed;
    &:after {
      content: '';
      position: fixed;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      opacity: .3;
      z-index: -1;
      color: powderblue;
    }
  }
</style>
