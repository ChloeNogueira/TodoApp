import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Todos from '../views/Todos.vue'
import axios from 'axios'

axios.defaults.headers.common['x-access-tokens'] =  localStorage.getItem('token')

Vue.use(VueRouter)

const routes = [
  {
    path:'/register',
    name: 'Register',
    component: Register
  },
  {
    path:'/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/:id',
    name: 'Todos',
    props: true,
    component: Todos
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
