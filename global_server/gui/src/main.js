import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default-dark.css'
import { MdField, MdButton, MdIcon} from 'vue-material/dist/components'
import UIkit from 'uikit'
import Icons from 'uikit/dist/js/uikit-icons'

// use uikit icons
UIkit.use(Icons)

// vue materials components
Vue.use(MdField)
Vue.use(MdButton)
Vue.use(MdIcon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
