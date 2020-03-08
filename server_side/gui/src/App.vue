<template>
  <div id="app">
    <div v-show="!global_loading">
      <div id="app-border-top" uk-sticky></div>
      <navigation-bar v-if="user" />
      <div id="content">
        <router-view />
      </div>
      <footer-bar v-if="user" />
    </div>
    <div v-show="global_loading" style="display: flex; height: calc(100vh - 1px)">
      <div style="margin: auto;">
        <breeding-rhombus-spinner
          :animation-duration="2000"
          :size="80"
          color="#f0f0f0"
        />
        <div class="uk-margin-xmedium-top">Loading ...</div>
      </div>
    </div>
  </div>
</template>

<script>
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons'
import { mapState, mapActions } from 'vuex'
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import { BreedingRhombusSpinner } from 'epic-spinners'

// use uikit icons
UIkit.use(Icons)

export default {
  name: 'app',

  components: {
    NavigationBar,
    FooterBar,
    BreedingRhombusSpinner
  },

  created () {
    this.setUserInfo()
  },

  computed: {
    ...mapState([
      'user',
      'global_loading'
    ])
  },

  methods: {
    ...mapActions([
      'setUserInfo'
    ])
  }
}
</script>

<style>
/* import uikit and custom styles */
@import '../node_modules/uikit/dist/css/uikit.min.css';
@import './assets/css/uikit-customs.css';
@import './assets/css/vue-materials-customs.css';
@import './assets/css/customs.css';
/* custom scrollbar styles */
@import './assets/css/scrollbar.css';

body {
  margin: 0 !important;
  padding: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  background: rgb(25, 25, 25) !important;
  color: rgb(240, 240, 240) !important;
}
body * {
  font-family: 'Comic Sans MS' !important;
}
#app-border-top {
  height: 0px;
  width: 100vw;
  z-index: 1000;
  border-bottom: 1px solid rgb(25, 25, 25);
}
#content {
  padding: 0px 15px 0px 15px;
  height: 100%;
  min-height: calc(100vh - 116px);
}
</style>
