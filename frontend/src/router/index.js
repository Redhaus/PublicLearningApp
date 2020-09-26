import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Lexis from "../views/Lexis.vue";
import Events from "../views/Events.vue";
import Readings from "../views/Readings.vue";
import Explorations from "../views/Explorations";
import Extensions from "../views/Extensions";
import Performances from "../views/Performances";
import Questions from "../views/Questions";
import Goals from "../views/Goals";
import Lessons from "../views/Lesson";
import Signin from "../views/Signin";




Vue.use(VueRouter);

const routes = [
    {
    path: "/",
    name: "Dashboard",
    component: Home
  },



  {
    path: "/events",
    name: "Events",
    component: Events
  },
  // {
  //   path: "/events",
  //   name: "Events",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/Events.vue")
  // },
  {
    path: "/readings",
    name: "Readings",
    component: Readings
  },

  {
    path: "/explorations",
    name: "Explorations",
    component: Explorations
  },
  {
    path: "/lexis",
    name: "Lexis",
    component: Lexis
  },

  {
    path: "/questions",
    name: "Questions",
    component: Questions
  },

  {
    path: "/performances",
    name: "Performances",
    component: Performances
  },

  {
    path: "/extensions",
    name: "Extensions",
    component: Extensions
  },

  {
    path: "/goals",
    name: "Goals",
    component: Goals
  },

      {
    path: "/review",
    name: "Lesson",
    component: Lessons
  },


      {
    path: "/signin",
    name: "Signin",
    component: Signin
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
