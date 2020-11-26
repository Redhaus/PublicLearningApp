<template>
    <q-layout view="hHh lpR lFf" class="bg-grey-2">

<!--        view="hHh lpR lFf">-->
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

<!--                    Ideal Icon-->
<!--                    <q-icon dense>-->

<!--                        <svg version="1.1" baseProfile="basic" id="Layer_1"-->
<!--                             xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"-->
<!--                             y="0px" viewBox="0 0 136.75 156.28"-->
<!--                             xml:space="preserve">-->
<!--                            <g>-->
<!--                                <g>-->
<!--                                    <path class="st0"-->
<!--                                          d="M84.73,70.65h50.15c-0.67,46.28-38.36,83.75-84.72,84.05v-50.15C68.87,104.26,84.08,89.28,84.73,70.65z"/>-->
<!--                                    <path class="st0"-->
<!--                                          d="M56.31,40.18V1.42c36.18,0.48,65.65,29.27,67.19,65.19l-38.84,0C83.2,52.08,71.11,40.64,56.31,40.18z"/>-->
<!--                                    <path class="st0" d="M38.1,46.55c-3.77,3.77-6.02,8.65-6.46,13.9H1.78c0.47-13.22,5.83-25.58,15.24-34.98-->
<!--                                        c9.47-9.46,21.92-14.83,35.23-15.24v29.85C46.91,40.46,41.93,42.72,38.1,46.55z"/>-->
<!--                                    <path class="st0"-->
<!--                                          d="M46.11,76.83v21.96C26.85,98.63,11.09,83.53,9.79,64.51h22.08C33.05,71.4,38.96,76.68,46.11,76.83z"/>-->
<!--                                    <path class="st0" d="M56.82,70.65h11.14c-0.47,4.41-2.42,8.5-5.61,11.68c-3.31,3.29-7.59,5.25-12.19,5.62V76.9-->
<!--                                        c1.65-0.31,3.22-1.13,4.45-2.35C55.71,73.46,56.45,72.11,56.82,70.65z"/>-->
<!--                                    <path class="st0" d="M50.97,61.96c-0.31-0.01-0.62,0.02-0.93,0.07v-7.87c0.31-0.02,0.62-0.05,0.93-0.05-->
<!--                                        c3.71,0,7.22,1.46,9.85,4.09c2.28,2.29,3.67,5.23,3.99,8.41h-7.95c-0.26-1.07-0.81-2.07-1.61-2.87-->
<!--                                        C54.11,62.59,52.58,61.96,50.97,61.96z"/>-->
<!--                                </g>-->
<!--                            </g>-->
<!--                            </svg>-->


<!--                    </q-icon>-->

                    <q-toolbar-title shrink class="text-weight-bold">

                    <LogoTemplate/>

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
                :width="280">
            <q-scroll-area class="fill-window">
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


            <q-scroll-area class="fill-window" :visible="false">

                <!--                <div class="stepper">-->


                <!--                    <q-stepper-->
                <!--                            v-model="step"-->
                <!--                            ref="stepper"-->
                <!--                            color="primary"-->
                <!--                            alternative-labels-->
                <!--                            >-->
                <!--                        <q-step-->
                <!--                                :name="1"-->
                <!--                                title="Select Events"-->
                <!--                                icon="settings"-->
                <!--                                :done="step > 1" />-->

                <!--                        <q-step-->
                <!--                                :name="2"-->
                <!--                                title="Select Reading"-->
                <!--                                icon="create_new_folder"-->
                <!--                                :done="step > 2" />-->

                <!--                        <q-step-->
                <!--                                :name="3"-->
                <!--                                title="Further Explorations"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 3" />-->

                <!--                        <q-step-->
                <!--                                :name="4"-->
                <!--                                title="Select Lexis"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 4" />-->

                <!--                        <q-step-->
                <!--                                :name="5"-->
                <!--                                title="Select Questions"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 5" />-->

                <!--                        <q-step-->
                <!--                                :name="6"-->
                <!--                                title="Select Performances"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 6" />-->

                <!--                        <q-step-->
                <!--                                :name="7"-->
                <!--                                title="Select Extensions"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 7" />-->

                <!--                        <q-step-->
                <!--                                :name="8"-->
                <!--                                title="Select Goals"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 8" />-->

                <!--                        <q-step-->
                <!--                                :name="9"-->
                <!--                                title="Review Lesson"-->
                <!--                                icon="add_comment"-->
                <!--                                  :done="step > 9" />-->

                <!--                        <template v-slot:navigation>-->
                <!--                            <q-stepper-navigation>-->
                <!--                                <q-btn @click="$refs.stepper.next()" color="primary"-->
                <!--                                       :label="step === 3 ? 'Finish' : 'Continue'"/>-->
                <!--                                <q-btn v-if="step > 1" flat color="primary" @click="$refs.stepper.previous()"-->
                <!--                                       label="Back" class="q-ml-sm"/>-->
                <!--                            </q-stepper-navigation>-->
                <!--                        </template>-->
                <!--                    </q-stepper>-->


                <!--                </div>-->

                <transition name="slide" mode="out-in">
                    <router-view/>

                    <!--                    <slot/>-->
                </transition>

            </q-scroll-area>
        </q-page-container>

    </q-layout>
</template>


<script>

    import SideNav from "@/components/SideNav.vue";
    import TopRightNav from "@/components/TopRightNav.vue";
    import {fabYoutube} from '@quasar/extras/fontawesome-v5';
    import LogoTemplate from "../components/LogoTemplate";

    export default {
        name: 'MyLayout',
        data() {
            return {
                // leftDrawerOpen: false,
                search: '',
                miniState: false,
                drawer: false,
                step: 1,
            }
        },
        created() {
            let id = window.localStorage.getItem('instructor_id');
            console.log('ID', id);

            this.fabYoutube = fabYoutube;
            this.$store.dispatch("fetchLessons", id);
            this.$store.dispatch("fetchClasses", id);
            this.$store.dispatch("fetchEvents");
            this.$store.dispatch("fetchCategories");
            this.$store.dispatch("fetchLexis");
            this.$store.dispatch("fetchReadings");
            this.$store.dispatch("fetchExplorations");
            this.$store.dispatch("fetchQuestions");
            this.$store.dispatch("fetchPerformances");
            this.$store.dispatch("fetchExtensions");
            this.$store.dispatch("fetchGoals");
            this.$store.dispatch("fetchInstructor");

        },

        methods: {
            miniToggle() {
                // console.log('CLICKED')
                this.miniState = !this.miniState;
            }
        },
        components: {
            SideNav,
            TopRightNav,
            LogoTemplate
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


    .fill-window {
        height: calc(100vh + 20px);
        /*height: 5500px*/
    }

    .YL {
        &__toolbar-input-container {
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


    /* LEXIS STYLES */


    .indent {
        padding-left: 20px;
    }

    .cardHandle {
        transition: all .15s ease-in-out;

        &:hover {
            background-color: #EEEEEE;
            /*transform: scale(.96);*/
        }
    }

    .q-tab--active {
        color: #000000 !important;
        /*border-top: 1px solid #666;*/
    }

    .bottom-padding {
        padding-bottom: 20px;
    }

    .flex-break {
        flex: 1 0 100% !important;
        width: 0 !important;
    }

    .active {
        background-color: #000 !important;
        color: white;
        transform: scale(.96);
    }

    .subtitle {
        font-size: .8rem !important;
        font-weight: bold;
    }

    .subtitleEtymology {
        padding-top: 10px;
        font-size: .8rem !important;
        font-weight: bold;
    }

    .test {
        padding-top: 20px;
        padding-left: 20px;
    }

    .page-bar {
        background-color: #ffffff;
    }

    .title {
        font-size: 1.15rem !important;
        margin: auto;

        &:focus {
            outline: none;
        }
    }

    .full-width-banner {
        width: 100%;
        padding-bottom: 20px;
    }

    .banner-margin {
        margin-left: 15px;
    }

    .pos {
        float: right;
        font-weight: normal;
    }

    .q-dialog__inner--minimized > div {
        /*max-width: none !important;*/
    }

    .dialog-top {
        padding-top: 10px;
    }

    .lex-card {
        min-width: 70% !important;
        padding: 20px;
    }


    .q-stepper__tab {
        padding: 0 !important;
    }

    .marginNegThirty {
        margin-top: -34px;
    }

    .q-card{
    box-shadow: none !important;
    }

    .page-bar{
        border: 1px solid rgba(0, 0, 0, 0.12);
    }

   /*body.desktop .q-hoverable:hover > .q-focus-helper {*/
   /*     background-color: #ffffff !important;*/
   /*    opacity: 1 !important;*/
   /* }*/

    body.desktop .q-focus-helper {
    position: absolute;
    top: 0;
    left: 0 /* rtl:ignore */;
    width: 100%;
    height: 100%;
    pointer-events: none;
    border-radius: inherit;
    opacity: 0;
    transition: background-color 1s cubic-bezier(0.25, 0.8, 0.5, 1), opacity 1s cubic-bezier(0.25, 0.8, 0.5, 1);
}

        .selectEventNotification {
    color: grey;
    font-size: 2rem;
    text-align: center;
    padding-top: 20%;
}




        /*TOOLTIPS*/


    .tooltip {
  display: block !important;
  z-index: 10000;
        font-size: 12px;
        line-height: 14px;

  .tooltip-inner {
    background: black;
    color: white;
    border-radius: 4px;
    padding: 10px 10px 10px 12px;
      max-width: 250px;
  }

  .tooltip-arrow {
    width: 0;
    height: 0;
    border-style: solid;
    position: absolute;
    margin: 5px;
    border-color: black;
    z-index: 1;
  }

  &[x-placement^="top"] {
    margin-bottom: 5px;

    .tooltip-arrow {
      border-width: 5px 5px 0 5px;
      border-left-color: transparent !important;
      border-right-color: transparent !important;
      border-bottom-color: transparent !important;
      bottom: -5px;
      left: calc(50% - 5px);
      margin-top: 0;
      margin-bottom: 0;
    }
  }

  &[x-placement^="bottom"] {
    margin-top: 5px;

    .tooltip-arrow {
      border-width: 0 5px 5px 5px;
      border-left-color: transparent !important;
      border-right-color: transparent !important;
      border-top-color: transparent !important;
      top: -5px;
      left: calc(50% - 5px);
      margin-top: 0;
      margin-bottom: 0;
    }
  }

  &[x-placement^="right"] {
    margin-left: 5px;

    .tooltip-arrow {
      border-width: 5px 5px 5px 0;
      border-left-color: transparent !important;
      border-top-color: transparent !important;
      border-bottom-color: transparent !important;
      left: -5px;
      top: calc(50% - 5px);
      margin-left: 0;
      margin-right: 0;
    }
  }

  &[x-placement^="left"] {
    margin-right: 5px;

    .tooltip-arrow {
      border-width: 5px 0 5px 5px;
      border-top-color: transparent !important;
      border-right-color: transparent !important;
      border-bottom-color: transparent !important;
      right: -5px;
      top: calc(50% - 5px);
      margin-left: 0;
      margin-right: 0;
    }
  }

  &[aria-hidden='true'] {
    visibility: hidden;
    opacity: 0;
    transition: opacity .15s, visibility .15s;
  }

  &[aria-hidden='false'] {
    visibility: visible;
    opacity: 1;
    transition: opacity .15s;
  }


}



    /*.st0 {*/
    /*    fill: #CC212A;*/
    /*}*/

    /*.st1 {*/
    /*    fill: #DA8367;*/
    /*}*/

    /*.st2 {*/
    /*    fill: #EABDA6;*/
    /*}*/

    /*.st3 {*/
    /*    fill: #9FC54C;*/
    /*}*/

    /*.st4 {*/
    /*    fill: #C2D88E;*/
    /*}*/

    /*.st5 {*/
    /*    fill: #DDE9C2;*/
    /*}*/

    /*.st6 {*/
    /*    fill: #EEBF2F;*/
    /*}*/

    /*.st7 {*/
    /*    fill: #F5D781;*/
    /*}*/

    /*.st8 {*/
    /*    fill: #F9E7BC;*/
    /*}*/

    /*.st9 {*/
    /*    fill: #1EA69B;*/
    /*}*/

    /*.st10 {*/
    /*    fill: #84C2BD;*/
    /*}*/

    /*.st11 {*/
    /*    fill: #BFDEDB;*/
    /*}*/

    /*.st12 {*/
    /*    fill: #25AAE2;*/
    /*}*/

    /*.st13 {*/
    /*    fill: #80C5ED;*/
    /*}*/

    /*.st14 {*/
    /*    fill: #BDE0F6;*/
    /*}*/

    /*.st15 {*/
    /*    fill: #7D2C8A;*/
    /*}*/

    /*.st16 {*/
    /*    fill: #A479B1;*/
    /*}*/

    /*.st17 {*/
    /*    fill: #C9B4D4;*/
    /*}*/

    /*.st18 {*/
    /*    fill: #2D55A3;*/
    /*}*/

    /*.st19 {*/
    /*    fill: #7584BF;*/
    /*}*/

    /*.st20 {*/
    /*    fill: #B0B5DC;*/
    /*}*/

    /*.st21 {*/
    /*    fill: #CB1B71;*/
    /*}*/

    /*.st22 {*/
    /*    fill: #DA859D;*/
    /*}*/

    /*.st23 {*/
    /*    fill: #EABFC7;*/
    /*}*/


</style>

