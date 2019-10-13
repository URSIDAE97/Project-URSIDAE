<template>
  <div id="app">
    <TitleBar>URSIDAE</TitleBar>
    <router-view/>
  </div>
</template>


<script>
import TitleBar from '@/components/TitleBar.vue'

export default {
  components: {
    TitleBar
  }
}
</script>


<style>
body {
  margin: 0;
  width: 100%;
  height: 100%;
  font-family: 'Comic Sans MS';
  background: rgb(25, 25, 25);
  color: rgb(240, 240, 240);
}
</style>
