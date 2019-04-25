import Axios from 'axios'

const BudgetManagerAPI = `http://${window.location.hostname}:3001`

const instance = Axios.create({
  baseURL: `${BudgetManagerAPI}/api/v1/`
})

export default instance
