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
    redirect: '/login', // / にアクセスした場合は /login にリダイレクトする
  },
  {
    path: '/home',
    name: 'home',
    component: HelloWorld,
    // meta: { requiresAuth: false },
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// router.beforeEach((to, from, next) => {
//   console.log(to.matched[0].meta["requiresAuth"])
//   // console.log(from)
//   console.log(['from',from.fullPath])
//   console.log(['to',to.fullPath])
//   console.log(to.matched[0].meta["requiresAuth"])
//   // console.log(!store.getToken())
//   if (to.matched[0].meta["requiresAuth"]) { 
//     //next('/home');
//     next();
//     console.log('/home')
//   } else {
//     next('/login');
//     console.log('/next')
//   }
// });

export default router
