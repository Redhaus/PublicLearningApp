<template>
  <q-list padding>


    <q-item
      v-for="link in links1"
      :key="link.text"

      v-ripple
      clickable
      :active="$route.path === link.link"
      active-class="my-menu-link"
      @click="navSwitch(link.link, link.style)"
    >
      <q-item-section avatar>
        <q-icon color="grey" :name="link.icon" />
      </q-item-section>

      <q-item-section>
        <q-item-label>{{ link.text }}</q-item-label>
      </q-item-section>
    </q-item>
    <!--        </router-link>-->

    <!--        <q-separator class="q-my-md"/>-->

    <!--        <q-item v-for="link in links2" :key="link.text" v-ripple clickable>-->
    <!--            <q-item-section avatar>-->
    <!--                <q-icon color="grey" :name="link.icon"/>-->
    <!--            </q-item-section>-->
    <!--            <q-item-section>-->
    <!--                <q-item-label>{{ link.text }}</q-item-label>-->
    <!--            </q-item-section>-->
    <!--        </q-item>-->

    <q-separator class="q-mt-md q-mb-lg" />

    <q-item clickable v-ripple @click="miniToggle">
      <q-item-section avatar v-if="!miniState">
        <q-icon name="chevron_left" />
      </q-item-section>

      <q-item-section avatar v-if="miniState">
        <q-icon name="chevron_right" />
      </q-item-section>

      <q-item-section>Minify</q-item-section>
    </q-item>

    <!--        <div class="q-px-md  text-grey-9">-->
    <!--            <div class="row items-center q-gutter-x-sm q-gutter-y-xs">-->
    <!--                <a-->
    <!--                  v-for="button in buttons2"-->
    <!--                  :key="button.text"-->
    <!--                  class="YL__drawer-footer-link"-->
    <!--                  href="javascript:void(0)">-->
    <!--                    {{ button.text }}-->
    <!--                </a>-->
    <!--            </div>-->
    <!--        </div>-->
  </q-list>
</template>

<script>
import { fabYoutube } from "@quasar/extras/fontawesome-v5";

export default {
  name: "SideNav",

  created() {
    this.links = this.$route.name.toLowerCase();
  },

  methods: {
    navSwitch(url, style) {
      const path = url;
      if (this.$route.path !== path) this.$router.push(path);

      this.links = style;

      if (this.miniState) {
        this.miniState = false;
        this.$emit("miniToggle", this.miniState);
      }
    },

    miniToggle() {
      // console.log('CLICKED')
      this.miniState = !this.miniState;

      // pass emit event to parent component and pass data changed
      this.$emit("miniToggle", this.miniState);
    },

    drawerClick(e, link) {
      console.log("LINK", link);
      this.link = link;
      // if in "mini" state and user
      // click on drawer, we switch it to "normal" mode
      // this.miniState = !this.miniState;
      //
      if (this.miniState) {
        this.miniState = false;
        //
        //   // notice we have registered an event with capture flag;
        //   // we need to stop further propagation as this click is
        //   // intended for switching drawer to "normal" mode only
        e.stopPropagation();
      }
      e.stopPropagation();
    }
  },
  data() {
    return {
      drawer: false,
      miniState: false,
      links: "inbox",
      links1: [
        { icon: "o_create_new_folder", text: "Dashboard", link: "/", style: "dashboard" },
                      // { icon: "o_home", text: "Dashboard", link: "/", style: "dashboard" },

        { icon: "o_group_add", text: "Classes", link: "/classes", style: "classes" },


        { icon: "o_library_books", text: "Events", link: "/events", style: "events" },
        {
          icon: "o_book",
          text: "Primary Readings",
          link: "/readings",
          style: "readings"
        },
        {
          icon: "o_explore",
          text: "Further Exploration",
          link: "/explorations",
          style: "explorations"
        },
        { icon: "o_text_snippet", text: "Lexis", link: "/lexis", style: "lexis" },
        {
          icon: "o_live_help",
          text: "Key Questions",
          link: "/questions",
          style: "questions"
        },
        {
          icon: "o_school",
          text: "Performances",
          link: "/performances",
          style: "performances"
        },
        {
          icon: "o_extension",
          text: "Extensions",
          link: "/extensions",
          style: "extensions"
        },
        {
          icon: "o_emoji_events",
          text: "Continual Goals",
          link: "/goals",
          style: "goals"
        },

         {
          icon: "o_grading",
          text: "Review Lesson",
          link: "/review",
          style: "lessons"
        }
      ]
      // links2: [
      //
      // ],
    };
  }
};
</script>

<style>
/*.router-link-exact-active{*/
/*   color: black;*/
/*}*/

.my-menu-link {
  color: black !important;
}

.my-menu-link {
  color: black;
  /*background-color: #cacaca;*/


    border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    border-top: 1px solid rgba(0, 0, 0, 0.12);
    background-color: #FFF;


}

/*.router-link-exact-active .text-grey {*/
/*    color: black !important;*/
/*}*/

/*.router-link-exact-active .q-item {*/
/*    color: black;*/
/*    background-color: #cacaca;*/
/*}*/

a {
  text-decoration: none;
  color: gray;
}
</style>
