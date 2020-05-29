import server_api from './axios_config'

export function authenticateUser (user) {
  return server_api.post('/auth/login', user)
    .then(response => {
      return response.data
    })
    .catch(error => {
      console.log(error)
      return null
    })
}