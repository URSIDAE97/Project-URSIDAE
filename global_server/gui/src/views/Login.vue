<template>
  <div class="login-panel">
    <div style="display: inline-flex; margin: auto;">
      <img alt="URSIDAE logo" src="../assets/img/logo_title_transparent_white.png">
      <div class="uk-margin-medium-left uk-margin-medium-top">
        <text-input
          label="Username"
          icon="user"
          :error="loginError"
          :value="tmp_user.username"
          :maxlength="20"
          name="username"
          @input="tmp_user.username = $event; loginError = false"
          @enter="login()"
        />
        <text-input
          label="Password"
          icon="lock"
          :error="loginError"
          :value="tmp_user.password"
          type="password"
          :maxlength="20"
          name="password"
          @input="tmp_user.password = $event; loginError = false"
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
</template>

<script>
import TextInput from '@/components/form_inputs/TextInput.vue'
import { authenticateUser } from '@/services/authentication_service.js'
import { setAuthToken } from '@/services/local_storage_service.js'
import { mapActions, mapMutations, mapState } from 'vuex'
import notificationService from '@/services/notification_service'
import { uppercase } from '@/library/filters'

export default {
  name: 'Login',

  components: {
    TextInput
  },

  data () {
    return {
      tmp_user: {
        username: '',
        password: ''
      },
      loginError: false
    }
  },

  computed: {
    ...mapState([
      'user'
    ])
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
      authenticateUser(self.tmp_user)
        .then(data => {
          if (data) {
            setAuthToken(data.access_token)
            self.setUserInfo()
            self.$router.push({ name: 'dashboard' })
            self.setGlobalLoading(false)
            notificationService.success(`Welcome back ${ uppercase(self.user.username) }`, 5000)
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
</style>