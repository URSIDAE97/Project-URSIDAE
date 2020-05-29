<template>
  <div id="app">
    <div v-show="!global_loading" class="fill-view">
      <navigation-bar :height="nav_bar_height" />
      <div
        id="content"
        :style="{ height: 'calc(100vh - ' + nav_bar_height + 'px - ' + footer_bar_height + 'px)' }"
      >
        <router-view />
      </div>
      <footer-bar :height="footer_bar_height" />
    </div>
    <div v-show="global_loading" class="fill-view">
      <loading />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import NavigationBar from '@/components/base/NavigationBar.vue'
import FooterBar from '@/components/base/FooterBar.vue'
import Loading from '@/components/base/Loading.vue'

const NAV_BAR_HEIGHT = 45
const FOOTER_BAR_HEIGHT = 30

export default {
  name: 'app',

  components: {
    NavigationBar,
    FooterBar,
    Loading
  },

  created () {
    this.setUserInfo()
    // if (this.user) {
    //   this.$router.push({ name: 'dashboard' })
    // }
  },

  computed: {
    ...mapState([
      'user',
      'global_loading'
    ]),
    nav_bar_height () {
      return this.user ? NAV_BAR_HEIGHT : 0
    },
    footer_bar_height () {
      return this.user ? FOOTER_BAR_HEIGHT : FOOTER_BAR_HEIGHT + NAV_BAR_HEIGHT
    }
  },

  methods: {
    ...mapActions([
      'setUserInfo'
    ])
  }
}
</script>

<style lang="scss">
/* uikit */
@import '../node_modules/uikit/dist/css/uikit.min.css';
/* customs */
@import './assets/scss/uikit-customs.scss';
@import './assets/css/vue-materials-customs.css';
@import './assets/scss/customs.scss';
/* scrollbars */
@import './assets/css/scrollbars.css';

#app {
  margin: 0 !important;
  padding: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  background: rgb(30, 30, 30) !important;
  color: rgb(240, 240, 240) !important;
}
#app * {
  font-family: 'Comic Sans MS' !important;
}
.fill-view {
  height: 100%;
  width: 100%;
}
#content {
  width: 100%;
  padding: 15px;
  overflow-x: auto;
  overflow-y: auto;
}
</style>
