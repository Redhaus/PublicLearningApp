import Vue from "vue";

import "./styles/quasar.scss";
import "quasar/dist/quasar.ie.polyfills";
import "@quasar/extras/roboto-font/roboto-font.css";
import "@quasar/extras/material-icons/material-icons.css";
import "@quasar/extras/material-icons-outlined/material-icons-outlined.css";
import "@quasar/extras/fontawesome-v5/fontawesome-v5.css";
import { Quasar, Loading } from "quasar";

Vue.use(Quasar, {
  config: {
    Loading
  },
  components: {
    /* not needed if importStrategy is not 'manual' */
  },
  directives: {
    /* not needed if importStrategy is not 'manual' */
  },
  plugins: {
    Loading
  }
});
