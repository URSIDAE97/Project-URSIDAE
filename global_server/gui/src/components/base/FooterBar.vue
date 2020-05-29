<template>
  <div
    id="footer"
    :class="[{ 'shadow-border': !!user }]"
    class="uk-padding-xxsmall-bottom"
    :style="{ height: height - 1 + 'px', 'background-color': !!user ? 'black' : 'unset' }"
  >
    <div class="uk-margin-xmedium-left footer-elem uk-text-xsmall">
      <div v-if="!!user" class="uk-margin-xsmall-bottom">
        <span>version: {{ version }}</span>
      </div>
      <div v-else class="uk-margin-bottom">
        <p class="uk-margin-small-bottom">version: {{ version }}</p>
        <p class="uk-margin-remove">by URSIDAE @{{ currentYear }}</p>
      </div>
    </div>
    <div class="footer-elem uk-text-xsmall">
      <div v-if="!!user" class="uk-margin-xsmall-bottom">
        <span>by URSIDAE @{{ currentYear }}</span>
      </div>
    </div>
    <div class="uk-margin-xmedium-right footer-elem uk-text-xsmall">
      <div :class="[ !!user ? 'uk-margin-remove' : 'uk-margin-bottom']">
        <a href="" :uk-icon="'icon: github; ratio: ' + (!!user ? '1;' : '1.5;')"></a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'footer-bar',

  props: {
    height: {
      type: Number,
      required: true
    }
  },

  data () {
    return {
      currentYear: new Date().getFullYear(),
      version: '0.0.2'
    }
  },

  computed: {
    ...mapState([
      'user'
    ])
  }
}
</script>

<style scoped>
#footer {
  background-color: black;
  color: rgb(240, 240, 240);
  border-bottom: 1px solid rgb(25, 25, 25);
  width: 100vw;
  z-index: 100;
  display: flex;
  justify-content: space-between;
}
.footer-elem {
  margin-top: auto;
}
.shadow-border {
  /* Shadow border top */
  -webkit-box-shadow: 0px -2px 10px 0px black;
  -moz-box-shadow: 0px -2px 10px 0px black;
  box-shadow: 0px -2px 10px 0px black;
}
</style>