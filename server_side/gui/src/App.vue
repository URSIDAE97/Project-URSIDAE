<template>
  <div id="app">
    <div id="app-border-top" uk-sticky></div>
    <navigation-bar/>
    <div id="content">
      <router-view/>
    </div>
    <footer-bar/>
  </div>
</template>

<script>
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons'

import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'

// use uikit icons
UIkit.use(Icons)

export default {
  name: 'app',

  components: {
    NavigationBar,
    FooterBar
  }
}
</script>

<style>
/* import uikit and custom styles */
@import '../node_modules/uikit/dist/css/uikit.min.css';
@import './assets/css/uikit-customs.css';
@import './assets/css/customs.css';
/* custom scrollbar styles */
@import './assets/css/scrollbar.css';

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
#app-border-top {
  height: 0px;
  width: 100%;
  z-index: 1000;
  border-top: 1px solid rgb(25, 25, 25);
}
#content {
  padding: 0px 15px 0px 15px;
}
</style>
