import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// import clip from "text-clipper";


import VueMasonry from 'vue-masonry-css'
import VTooltip from 'v-tooltip'

import "./quasar";
import {
  Quasar,
  Cookies
} from 'quasar'

Vue.config.productionTip = false;
Vue.use(VueMasonry);
Vue.use(VTooltip);


Vue.use(Quasar, {
  plugins: {
    Cookies
  }
});


// new Vue({
//   store,
//   el: '#app',
//
// });

new Vue({
  router,
  store,
    created () {
    console.log('STATE STORE: ', this.$store.state);
  },
  render: h => h(App)
}).$mount("#app");
