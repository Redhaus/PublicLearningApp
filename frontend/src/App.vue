<template>
    <q-layout view="hHh lpR fFf" class="bg-grey-2">
        <q-header bordered class="bg-white text-grey-8 q-py-xs" height-hint="58">
            <q-toolbar>

                <q-btn
                        flat
                        dense
                        round
                        @click="drawer = !drawer"
                        aria-label="Menu"
                        icon="menu"
                />

                <q-btn flat no-caps no-wrap class="q-ml-xs" v-if="$q.screen.gt.xs">
                    <q-icon :name="fabYoutube" color="red" size="28px"/>
                    <q-toolbar-title shrink class="text-weight-bold">
                        IdealEdu
                    </q-toolbar-title>
                </q-btn>

                <q-space/>
                <q-space/>

                <TopRightNav/>

            </q-toolbar>
        </q-header>

        <q-drawer
                v-model="drawer"
                show-if-above
                bordered
                :mini="!drawer || miniState"
                content-class="bg-grey-2"
                :width="240">
              <q-scroll-area class="fill-window" >
                <SideNav @miniToggle="miniState = $event"/>
            </q-scroll-area>

        </q-drawer>

        <q-page-container>

<!--             <div class="col q-ma-md">-->
<!--          <div class="column full-height">-->
<!--            <q-scroll-area class="col q-pa-sm" visible>-->

<!--              <router-view />-->

<!--            </q-scroll-area>-->
<!--          </div>-->
<!--        </div>-->


  <q-scroll-area class="fill-window" :visible="false" >

          <transition name="slide" mode="out-in">
            <router-view/>
                  </transition>

       </q-scroll-area>
        </q-page-container>

    </q-layout>
</template>


<script>

    import SideNav from "@/components/SideNav.vue";
    import TopRightNav from "@/components/TopRightNav.vue";
    import {fabYoutube} from '@quasar/extras/fontawesome-v5';

    export default {
        name: 'MyLayout',
        data() {
            return {
                // leftDrawerOpen: false,
                search: '',
                miniState: false,
                drawer: false,

            }
        },
        created() {
            this.fabYoutube = fabYoutube;
            this.$store.dispatch("fetchCategories");
            this.$store.dispatch("fetchLessons");
            this.$store.dispatch("fetchLexis");



        },

        methods: {
            miniToggle() {
                // console.log('CLICKED')
                this.miniState = !this.miniState;
            }
        },
        components: {
            SideNav,
            TopRightNav
        },


    }
</script>


<style lang="scss">

      /*css animation*/


    .slide-enter {
         opacity: 0;
    }

    /*slide in in second, set ease, set forwards so it stays there*/
    .slide-enter-active {
        animation: slide-in .3s ease-out forwards;
        transition: opacity .3s;

    }

    .slide-leave {
    }

    .slide-leave-active {
        animation: slide-out .3s ease-out forwards;
        transition: opacity .3s;
        opacity: 0;
    }

    @keyframes slide-in {
        from {
            transform: translateY(20px);

        }
        to {
            transform: translateY(0);

        }
    }

    @keyframes slide-out {
        from {
            transform: translateY(0);
        }
        to {
            transform: translateY(20px);
        }
    }

    /*endTransition*/



    .fill-window{
        height: calc(100vh + 20px);
        /*height: 5500px*/
      }

    .YL{
        &__toolbar-input-container{
            min-width: 100px;
            width: 55%;
}
        &__toolbar-input-btn {
            border-radius: 0;
            border-style: solid;
            border-width: 1px 1px 1px 0;
            border-color: rgba(0, 0, 0, .24);
            max-width: 60px;
            width: 100%;
        }

        &__drawer-footer-link {
            color: inherit;
            text-decoration: none;
            font-weight: 500;
            font-size: .75rem;

            &:hover {
                color: #000;
            }
        }

    }
</style>

