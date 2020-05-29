import Vue from 'vue'
import Vuex from 'vuex'
import { jwtDecode } from 'jwt-js-decode'
import { getAuthToken } from '@/services/local_storage_service'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    global_loading: false
  },
  mutations: {
    SET_USER_INFO (state, user) {
      state.user = user
    },
    SET_GLOBAL_LOADING (state, loading) {
      state.global_loading = loading
    }
  },
  actions: {
    setUserInfo ({ commit }) {
      var user = null
      var auth_token = getAuthToken()
      if (auth_token) {
        var jwt = jwtDecode(auth_token)
        user = jwt.payload.identity
      }
      commit('SET_USER_INFO', user)
    }
  },
  modules: {
  }
})
