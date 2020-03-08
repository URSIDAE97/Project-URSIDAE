import axios from 'axios'

const server_api = axios.create({
  baseURL: 'http://localhost:6969/api'
})

export default server_api
