// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueCookie from 'vue-cookie'
import Vuetify from 'vuetify'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store from '@/store'
import Authentication from '@/components/pages/Authentication'
//import First from '@/components/pages/Authentication'
import 'vuetify/dist/vuetify.css'
Vue.use(BootstrapVue)
Vue.use(VueCookie)
Vue.use(Vuetify)
Vue.use(store)
Vue.config.productionTip = false
Authentication.checkAuthentication()
/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
