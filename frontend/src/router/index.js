import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import GoogleLogin from '../components/GoogleLogin.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: GoogleLogin,
  },
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/home',
    name: 'home',
    component: HelloWorld,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
