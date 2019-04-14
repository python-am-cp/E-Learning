import Vue from 'vue'
import Vuex from 'vuex'

import UserStore from './users/'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {},
  modules: {
    users: UserStore
  }
})
