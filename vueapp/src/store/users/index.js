import * as getters from './getters'
import * as mutations from './mutations'
import * as actions from './actions'

const state = {
  current: {},
  collection: []
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
