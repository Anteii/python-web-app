import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';


axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; // the FastAPI backend

Vue.config.productionTip = false;

createApp(App).use(store).use(router).mount("#app");