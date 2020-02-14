<template>
  <div id="app">
    <navigation-bar/>
    <div id="content">
      <router-view/>
    </div>
    <footer/>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'app',

  components: {
    NavigationBar,
    Footer
  }
}
</script>

<style>
body {
  margin: 0;
  width: 100%;
  height: 100%;
  background: rgb(25, 25, 25);
  color: rgb(240, 240, 240);
}
body * {
  font-family: 'Comic Sans MS' !important;
}
#content {
  padding: 0px 15px 0px 15px;
}
</style>
