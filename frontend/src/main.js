import { createApp } from "vue";
import App from "./App.vue";
import router from "./router"; 

import '../src/assets/tailwind.css';
import axios from "axios";

const token = localStorage.getItem('access');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
} else {
  console.warn('Aucun token trouvé dans localStorage.');
}


createApp(App)
  .use(router) 
  .mount("#app");
