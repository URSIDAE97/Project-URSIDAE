<template>
  <div style="height: calc(100vh - 1px); width: calc(100vw - 30px);">
    <!-- login panel -->
    <div class="login-panel">
      <div style="display: inline-flex; margin: auto;">
        <img alt="URSIDAE logo" src="../assets/img/logo_title_transparent_white.png">
        <div class="uk-margin-medium-left uk-margin-medium-top">
          <text-input
            label="Username"
            icon="user"
            :error="loginError"
            :value="user.username"
            :maxlength="20"
            @input="user.username = $event; loginError = false"
            @enter="login()"
          />
          <text-input
            label="Password"
            icon="lock"
            :error="loginError"
            :value="user.password"
            type="password"
            :maxlength="20"
            @input="user.password = $event; loginError = false"
            @enter="login()"
          />
          <span uk-icon="icon: sign-in; ratio: 0.9;" class="uk-margin-small-right uk-margin-xxmedium-top"></span>
          <button
            class="uk-button uk-button-text"
            style="color: rgb(240, 240, 240)"
            @click="login()"
          >LOG IN</button>
        </div>
      </div>
    </div>

    <!-- info panel -->
    <div class="uk-text-xsmall corner">
      <p class="uk-margin-small-bottom">version: {{ version }}</p>
      <p class="uk-margin-remove">by URSIDAE @{{ currentYear }}</p>
    </div>
  </div>
</template>

<script>
import TextInput from '@/components/form_inputs/TextInput.vue'
import { authenticateUser } from '@/services/authentication_service.js'
import { setAuthToken } from '@/services/local_storage_service.js'
import { mapActions, mapMutations } from 'vuex'
import notificationService from '@/services/notification_service'

export default {
  name: 'Login',

  components: {
    TextInput
  },

  data () {
    return {
      user: {
        username: '',
        password: ''
      },
      loginError: false,
      version: '0.0.2',
      currentYear: new Date().getFullYear()
    }
  },

  methods: {
    ...mapMutations({
      setGlobalLoading: 'SET_GLOBAL_LOADING'
    }),
    ...mapActions([
      'setUserInfo'
    ]),
    login () {
      let self = this
      self.setGlobalLoading(true)
      authenticateUser(self.user)
        .then(data => {
          if (data) {
            setAuthToken(data.username + data.password)
            self.setUserInfo(data)
            self.$router.push({ name: 'dashboard' })
            self.setGlobalLoading(false)
          } else {
            self.setGlobalLoading(false)
            self.loginError = true
            notificationService.error('Bad credentials', 5000)
          }
        })
    }
  }
}
</script>

<style scoped>
.login-panel {
  height: 100%;
  width: 100%;
  display: flex;
}
img {
  height: 40vh !important;
}
.corner {
  position: absolute;
  bottom: 3vh;
  left: 3vh;
}
</style>