import axios from 'axios'

const server_api = axios.create({
  baseURL: 'http://localhost:6969/api',
  headers: {
    'Content-Type': 'application/json'
  }
})

export default server_api
