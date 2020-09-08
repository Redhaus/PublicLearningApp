import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import VueMasonry from 'vue-masonry-css'

import "./quasar";
import {
  Quasar,
  Cookies
} from 'quasar'

Vue.config.productionTip = false;
Vue.use(VueMasonry);


Vue.use(Quasar, {
  plugins: {
    Cookies
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
