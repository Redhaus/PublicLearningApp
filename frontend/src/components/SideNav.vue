<template>
  <q-list padding>


    <q-item
      v-ripple clickable
      :active="$route.path === '/dashboard'"
      active-class="my-menu-link"
      @click="navSwitch('/dashboard', 'dashboard')"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_create_new_folder" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Dashboard</q-item-label>
      </q-item-section>
    </q-item>


<!--    <q-item-->
<!--      v-ripple clickable-->
<!--      :active="$route.path === '/classes'"-->
<!--      active-class="my-menu-link"-->
<!--      @click="navSwitch('/classes', 'classes')"-->
<!--    >-->
<!--      <q-item-section avatar>-->
<!--        <q-icon color="grey" name="o_group_add" />-->
<!--      </q-item-section>-->

<!--      <q-item-section>-->
<!--        <q-item-label>Classes</q-item-label>-->
<!--      </q-item-section>-->
<!--    </q-item>-->

        <q-separator dense class="q-mt-md q-mb-md" />


<!-- <q-expansion-item-->
<!--        expand-separator-->

<!--        v-model="expanded"-->
<!--      >-->

<!--        <template v-slot:header>-->
<!--          <q-item-section avatar>-->
<!--            <q-icon color="grey" name="o_collections_bookmark" />-->
<!--          </q-item-section>-->

<!--          <q-item-section>-->
<!--           Lesson Creator-->
<!--          </q-item-section>-->
<!--        </template>-->


<!--    <div v-if="showNav">-->

    <q-item
      v-ripple clickable
      :active="$route.path === '/events'"
      active-class="my-menu-link"
      @click="navSwitch('/events', 'events')"
      :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_library_books" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Events</q-item-label>
      </q-item-section>
    </q-item>




    <q-item
      v-ripple clickable
      :active="$route.path === '/readings'"
      active-class="my-menu-link"
      @click="navSwitch('/readings', 'readings')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_book" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Primary Readings</q-item-label>
      </q-item-section>
    </q-item>




    <q-item
      v-ripple clickable
      :active="$route.path === '/explorations'"
      active-class="my-menu-link"
      @click="navSwitch('/explorations', 'explorations')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_explore" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Further Exploration</q-item-label>
      </q-item-section>
    </q-item>




    <q-item
      v-ripple clickable
      :active="$route.path === '/lexis'"
      active-class="my-menu-link"
      @click="navSwitch('/lexis', 'lexis')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_text_snippet" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Lexis</q-item-label>
      </q-item-section>
    </q-item>



    <q-item
      v-ripple clickable
      :active="$route.path === '/questions'"
      active-class="my-menu-link"
      @click="navSwitch('/questions', 'questions')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_live_help" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Key Questions</q-item-label>
      </q-item-section>
    </q-item>





    <q-item
      v-ripple clickable
      :active="$route.path === '/performances'"
      active-class="my-menu-link"
      @click="navSwitch('/performances', 'performances')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_school" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Performances</q-item-label>
      </q-item-section>
    </q-item>



    <q-item
      v-ripple clickable
      :active="$route.path === '/extensions'"
      active-class="my-menu-link"
      @click="navSwitch('/extensions', 'extensions')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_extension" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Extensions</q-item-label>
      </q-item-section>
    </q-item>




    <q-item
      v-ripple clickable
      :active="$route.path === '/goals'"
      active-class="my-menu-link"
      @click="navSwitch('/goals', 'goals')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_emoji_events" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Continual Goals</q-item-label>
      </q-item-section>
    </q-item>



    <q-item
      v-ripple clickable
      :active="$route.path === '/review'"
      active-class="my-menu-link"
      @click="navSwitch('/review', 'lessons')"
       :disable="!showNav"
    >
      <q-item-section avatar>
        <q-icon color="grey" name="o_grading" />
      </q-item-section>

      <q-item-section>
        <q-item-label>Review Lesson</q-item-label>
      </q-item-section>
    </q-item>


<!--      </div>-->

<!-- </q-expansion-item>-->


    <q-separator class="q-mt-md q-mb-md" />

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

  computed:{

    showNav(){

      if(this.$store.getters['getIsEditing'] || this.$store.getters['getIsNew'] || this.$store.getters['getIsDuplicate']){
        return true
      }

      return false

    }

  },

  methods: {

      expandedFunction(){

          if(this.showNav){
              return true
          }else{
                return false
          }


      },

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
       expanded: false,
      links1: [
        // { icon: "o_create_new_folder", text: "Dashboard", link: "/", style: "dashboard" },
                      // { icon: "o_home", text: "Dashboard", link: "/", style: "dashboard" },

        // { icon: "o_group_add", text: "Classes", link: "/classes", style: "classes" },







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
