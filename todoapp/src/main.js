import axios from 'axios'
import Vue from 'vue'
import App from './App.vue'
import router from './router'



axios.interceptors.request.use(req => {
  console.log(`${req.method} ${req.url}`);
  req.headers.common['x-access-tokens'] = localStorage.getItem('token')
  return req;
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
