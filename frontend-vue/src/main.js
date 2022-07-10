import { createApp } from 'vue'
import { createPinia } from 'pinia'

import './index.css'

import axios from 'axios'
import App from './App.vue'
import router from './router'

const app = createApp(App)

axios.defaults.baseURL = 'https://vocabulary-learn-api.herokuapp.com/'

app.use(createPinia())
app.use(router)

app.mount('#app')
