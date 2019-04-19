import Authentication from '@/components/pages/Authentication'
import axios from '@/utils/http'

export const getUsers = async ({ commit }) => {
  const { data } = axios.get('users', {
    headers: {
      'Authorization': Authentication.getAuthenticationHeader(this)
    }
  })
  commit('addUsers', data)
}

