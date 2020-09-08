<template>
  <q-list padding>
    <!--        <router-link v-for="link in links1"-->
    <!--                     :key="link.text"-->
    <!--                     :to="link.link"-->
    <!--        >-->

    <q-item
      v-for="link in links1"
      :key="link.text"
      v-ripple
      clickable
      :active="links === link.style"
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
      <q-item-section avatar>
        <q-icon name="chevron_left" />
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
        { icon: "home", text: "Dashboard", link: "/", style: "dashboard" },
        { icon: "whatshot", text: "Events", link: "/events", style: "events" },
        {
          icon: "subscriptions",
          text: "Primary Readings",
          link: "/readings",
          style: "readings"
        },
        {
          icon: "subscriptions",
          text: "Further Exploration",
          link: "/explorations",
          style: "explorations"
        },
        { icon: "restore", text: "Lexis", link: "/lexis", style: "lexis" },
        {
          icon: "thumb_up_alt",
          text: "Key Questions",
          link: "/questions",
          style: "questions"
        },
        {
          icon: "thumb_up_alt",
          text: "Performances",
          link: "/performances",
          style: "performances"
        },
        {
          icon: "folder",
          text: "Extensions",
          link: "/extensions",
          style: "extensions"
        },
        {
          icon: fabYoutube,
          text: "Continual Goals",
          link: "/goals",
          style: "goals"
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
  background-color: #cacaca;
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
