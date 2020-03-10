import Vue from 'vue'
import Vuex from 'vuex'

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
    setUserInfo ({ commit }, user) {
      commit('SET_USER_INFO', user)
    }
  },
  modules: {
  }
})
