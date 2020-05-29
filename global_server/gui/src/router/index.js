import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index'

const Dashboard = () => import(/* webpackChunkName: "dashboard" */ '@/views/Dashboard.vue')
const Settings = () => import(/* webpackChunkName: "settings" */ '@/views/Settings.vue')
const Login = () => import(/* webpackChunkName: "login" */ '@/views/Login.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '*',
    redirect: { name: 'dashboard'}
  },
  {
    path: '/',
    name: 'dashboard',
    component: Dashboard
  },
  {
    path: '/settings',
    name: 'settings',
    component: Settings
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.state.global_loading = true
  if (to.name !== 'login' && !store.state.user) {
    next({ name: 'login' })
  } else if (to.name === 'login' && store.state.user) {
    next(from)
  } else {
    next()
  }
})

router.afterEach(() => {
  store.state.global_loading = false
})

export default router
