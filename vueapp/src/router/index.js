import Vue from 'vue'
import Router from 'vue-router'
import * as Auth from '@/components/pages/Authentication'
// Pages
import Home from '@/components/pages/Home/Home'
import Authentication from '@/components/pages/Authentication/Authentication'
import First from '@/components/pages/Level/Level'
Vue.use(Router)
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        requiredAuth: true
      }
    },
    {
      path: '/level',
      name: 'Level',
      component: First,
      meta: {
        requiredAuth: true
      }
    },
    {
      path: '/login',
      name: 'Authentication',
      component: Authentication
    }
  ]
})
/*router.beforeEach((to, from, next) => {
  if (to.meta.requiredAuth) {
    if (Auth.default.user.authenticated) {
      next()
    } else {
      router.push('/login')
    }
  } else {
    next()
  }
})

 */
export default router
