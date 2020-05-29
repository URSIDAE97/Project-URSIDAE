<template>
  <div id="nav-bar" v-if="user" class="uk-padding-xxsmall" :style="{ height: height + 'px' }">
    <ul class="uk-subnav uk-subnav-divider uk-margin-remove">
      <li>
        <router-link :to="{ name: 'dashboard' }">
          <img
            src="../../assets/img/logo_horizontal_title_transparent_white.png"
            alt="logo_project_ursidae"
            style="height: 30px;"
          >
        </router-link>
      </li>
      <li>
        <span uk-icon="icon: thumbnails; ratio: 0.9;" class="uk-margin-xsmall-right urs-text"></span>
        <router-link
          :to="{ name: 'dashboard' }"
          tag="button"
          class="uk-button uk-button-text urs-text"
        >DASHBOARD</router-link>
      </li>
      <li>
        <span uk-icon="icon: settings; ratio: 0.9;" class="uk-margin-xsmall-right urs-text"></span>
        <router-link
          :to="{ name: 'settings' }"
          tag="button"
          class="uk-button uk-button-text urs-text"
        >SETTINGS</router-link>
      </li>
    </ul>
    <ul class="uk-subnav uk-subnav-divider uk-margin-remove">
      <li class="uk-margin-right">
        <span uk-icon="icon: sign-out; ratio: 0.9;" class="uk-margin-xsmall-right urs-text"></span>
        <button
          class="uk-button uk-button-text urs-text"
          @click="logout()"
        >LOG OUT</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { clearAuthToken } from '@/services/local_storage_service'
import { mapActions, mapState } from 'vuex'

export default {
  name: 'navigation-bar',

  props: {
    height: {
      type: Number,
      required: true
    }
  },

  computed: {
    ...mapState([
      'user'
    ])
  },

  methods: {
    ...mapActions([
      'setUserInfo'
    ]),
    logout () {
      clearAuthToken()
      this.setUserInfo()
      this.$router.push({ name: 'login' })
    }
  }
}
</script>

<style scoped>
#nav-bar {
  background-color: black;
  width: 100vw;
  z-index: 100;
  display: flex;
  justify-content: space-between;
  border-top: 1px solid rgb(25, 25, 25);
  /* Shadow border bottom */
  -webkit-box-shadow: 0px 2px 10px 0px black;
  -moz-box-shadow: 0px 2px 10px 0px black;
  box-shadow: 0px 2px 10px 0px black;
}
</style>