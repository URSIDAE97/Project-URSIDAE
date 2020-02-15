<template>
  <div id="footer" class="uk-padding-xxsmall-bottom uk-margin-small-top">
    <span class="uk-text-xsmall">by URSIDAE @{{ currentYear }}</span>
  </div>
</template>

<script>
export default {
  name: 'footer-bar',

  data () {
    return {
      currentYear: new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
#footer {
  background-color: black;
  text-align: center;
  color: rgb(240, 240, 240);
  border-bottom: 1px solid rgb(25, 25, 25);
  /* Shadow border top */
  -webkit-box-shadow: 0px -2px 10px 0px black;
  -moz-box-shadow: 0px -2px 10px 0px black;
  box-shadow: 0px -2px 10px 0px black;
}
</style>