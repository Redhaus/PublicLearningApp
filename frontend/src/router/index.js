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
import Classes from "../views/Classes";
import MainLayout from "../views/MainLayout";
import Home_Page from "../views/Home_Page";
import Registration from "../views/Registration";
import InstructorProfile from "../views/InstructorProfile";


Vue.use(VueRouter);

const routes = [

    {
        path: "/dashboard",
        // name: "Dashboard",
        component: MainLayout,
        children: [
            {
                // UserProfile will be rendered inside User's <router-view>
                // when /user/:id/profile is matched
                path: '/dashboard',
                name: "Dashboard",
                component: Home
            },
            {
                // UserPosts will be rendered inside User's <router-view>
                // when /user/:id/posts is matched
                path: "/events",
                name: "Events",
                component: Events,
            },

            {
                path: "/classes",
                name: "Classes",
                component: Classes
            },

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
                path: "/profile",
                name: "Profile",
                component: InstructorProfile
            },

        ]
    },

    //   {
    //   path: "/",
    //   name: "Dashboard",
    //   component: Home,
    //     meta: {
    //       layout: true,
    //     },
    // },

    // {
    //     path: "/classes",
    //     name: "Classes",
    //     component: Classes
    // },


    // {
    //   path: "/events",
    //   name: "Events",
    //   component: Events,
    //     meta: {
    //       MainLayout: true,
    //     },
    // },
    // {
    //   path: "/events",
    //   name: "Events",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "../views/Events.vue")
    // },
    // {
    //     path: "/readings",
    //     name: "Readings",
    //     component: Readings
    // },
    //
    // {
    //     path: "/explorations",
    //     name: "Explorations",
    //     component: Explorations
    // },
    // {
    //     path: "/lexis",
    //     name: "Lexis",
    //     component: Lexis
    // },
    //
    // {
    //     path: "/questions",
    //     name: "Questions",
    //     component: Questions
    // },
    //
    // {
    //     path: "/performances",
    //     name: "Performances",
    //     component: Performances
    // },
    //
    // {
    //     path: "/extensions",
    //     name: "Extensions",
    //     component: Extensions
    // },
    //
    // {
    //     path: "/goals",
    //     name: "Goals",
    //     component: Goals
    // },
    //
    // {
    //     path: "/review",
    //     name: "Lesson",
    //     component: Lessons
    // },

    {
        path: "/register",
        name: "Register",
        component: Registration
    },

    //  {
    //     path: "/pricing",
    //     name: "Pricing",
    //     component: Price_Page
    // },

    {
        path: "/",
        name: "Home",
        component: Home_Page
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
