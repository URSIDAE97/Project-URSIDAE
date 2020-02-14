<template>
  <div id="nav" class="uk-padding-xsmall uk-margin-bottom">
    <router-link to="/">
      <img
        src="../assets/logo/logo_transparent_white.png"
        alt="logo_project_ursidae"
        id="nav-logo"
        class="uk-margin-left uk-margin-right"
      >
    </router-link>
    <ul class="uk-subnav uk-subnav-divider uk-margin-remove">
      <li>
        <router-link to="/">DASHBOARD</router-link>
        <span uk-icon="icon: thumbnails; ratio: 0.9" class="uk-margin-xsmall-left"></span>
      </li>
      <li>
        <router-link to="/about">ABOUT</router-link>
        <span uk-icon="icon: question; ratio: 0.9" class="uk-margin-xsmall-left"></span>
      </li>
      <li>
        <router-link to="/about">SETTINGS</router-link>
        <span uk-icon="icon: settings; ratio: 0.9" class="uk-margin-xsmall-left"></span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'navigation-bar'
}
</script>

<style scoped>
#nav {
  background-color: black;
  color: rgb(240, 240, 240);
  display: flex;
  border-top: 1px solid rgb(25, 25, 25);
  /* Shadow border bottom */
  -webkit-box-shadow: 0px 2px 10px 0px black;
  -moz-box-shadow: 0px 2px 10px 0px black;
  box-shadow: 0px 2px 10px 0px black;
}
#nav-logo {
  height: 30px;
}
</style>