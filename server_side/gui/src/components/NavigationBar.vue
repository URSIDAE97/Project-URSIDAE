<template>
  <div id="nav-bar" class="uk-margin-bottom">
    <div id="nav-logo" class="uk-padding-xxsmall uk-padding-xsmall-bottom">
      <router-link :to="{ name: 'dashboard' }">
        <img
          src="../assets/img/logo_horizontal_title_transparent_white.png"
          alt="logo_project_ursidae"
          style="height: 30px;"
        >
      </router-link>
    </div>
    <div id="nav-links" class="uk-padding-xxsmall" uk-sticky="offset: 1px">
      <ul class="uk-subnav uk-subnav-divider links-list">
        <li>
          <router-link
            :to="{ name: 'dashboard' }"
            tag="button"
            class="uk-button uk-button-text"
          >DASHBOARD</router-link>
          <span uk-icon="icon: thumbnails; ratio: 0.9;" class="uk-margin-xsmall-left"></span>
        </li>
        <li>
          <router-link
            :to="{ name: 'settings' }"
            tag="button"
            class="uk-button uk-button-text"
          >SETTINGS</router-link>
          <span uk-icon="icon: settings; ratio: 0.9;" class="uk-margin-xsmall-left"></span>
        </li>
        <li>
          <button
            class="uk-button uk-button-text"
            @click="logout()"
          >LOG OUT</button>
          <span uk-icon="icon: sign-out; ratio: 0.9;" class="uk-margin-xsmall-left"></span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { clearAuthToken } from '@/services/local_storage_service'
import { mapActions } from 'vuex'

export default {
  name: 'navigation-bar',

  methods: {
    ...mapActions([
      'setUserInfo'
    ]),
    logout () {
      clearAuthToken()
      this.setUserInfo(null)
      this.$router.push({ name: 'login' })
    }
  }
}
</script>

<style scoped>
#nav-bar {
  background-color: black;
  color: rgb(240, 240, 240);
  display: grid;
  width: 100vw;
}
#nav-logo {
  margin: 0 auto;
}
#nav-links {
  width: auto;
  background-color: black;
  color: rgb(240, 240, 240);
  z-index: 1000;
  /* Shadow border bottom */
  -webkit-box-shadow: 0px 2px 10px 0px black;
  -moz-box-shadow: 0px 2px 10px 0px black;
  box-shadow: 0px 2px 10px 0px black;
}
.links-list {
  width: fit-content;
  margin: 0 auto;
}
</style>