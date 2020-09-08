<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Questions</div>
                    </div>

                    <div class="col-4" tabindex="0">
                        <q-input v-model="search" label="Search Questions" class="q-ml-md">
                            <template v-slot:append>
                                <q-icon v-if="search === ''" name="search"/>
                                <q-icon
                                        v-else
                                        name="clear"
                                        class="cursor-pointer"
                                        @click="clearSearch"
                                />
                            </template>
                        </q-input>
                        <!--                        <q-input filled bottom-slots v-model="search"  label="Search Lexis"  class="q-ml-md">-->
                        <!--                            <template v-slot:append>-->
                        <!--                                <q-icon v-if="search === ''" name="search"/>-->
                        <!--                                <q-icon v-else name="clear" class="cursor-pointer" @click="clearSearch"/>-->
                        <!--                            </template>-->
                        <!--                        </q-input>-->
                    </div>
                </div>
            </q-banner>
        </div>

        <div style="width: 100%">

           <div v-if="selected_event">
               <div v-if="questions_list.length > 0">
            <masonry :cols="4" :gutter="20">
                <div v-for="question in questions_list" :key="question.id" class="bottom-padding">
                    <q-card
                            :class="{ active: question_id_list.includes(question.id) }"
                            bordered
                            @click="eventAction(question.id)"
                    >
                        <q-card-section>
                            <div v-html="question.question"></div>
                        </q-card-section>
                    </q-card>
                </div>
            </masonry>
                     </div>
                    <div v-else>No Questions Available</div>


              </div>

        <div v-else>Please select an Event</div>

        </div>


        <div style="height: 50px"/>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                question_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchQuestions");
            this.question_id_list = this.$store.getters["getSelectedQuestions"];
        },

        computed: {

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },

            questions_list() {
                let questions = this.$store.getters["getQuestions"];

                console.log(this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = questions.filter(obj => {
                        // return obj.term === this.search
                        return obj.question.toLowerCase().includes(this.search.toLowerCase());
                    });
                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }
                //
                // if(this.search.length > 0){
                //       newLex  = lexis.filter(function (item) {
                //         return item === this.search;
                //     });
                //     return newLex
                // }

                return questions;
            }
        },

        methods: {


            clearSearch() {
                this.search = "";
            },

            eventAction(event) {
                if (this.question_id_list.includes(event)) {
                    this.$store.dispatch("setSelectedQuestions", event);

                    this.question_id_list = this.question_id_list.filter(function (item) {
                        return item !== event;
                    });
                } else {
                    this.$store.dispatch("setSelectedQuestions", event);
                    this.question_id_list.push(event);
                }
            }
        }
    };
</script>

<style lang="scss" scoped>


    .active {
        background-color: #cccccc;
    }

/*    .bottom-padding*/
/*        padding-bottom: 20px*/

/*    .flex-break*/
/*        flex: 1 0 100% !important*/
/*        width: 0 !important*/

/*    .active*/
/*        background-color: #cccccc*/

/*    .test*/
/*        padding-top: 20px*/
/*        padding-left: 20px*/

/*    .page-bar*/
/*        background-color: #ffffff*/

/*    .title*/
/*        font-size: 1.15rem !important*/
/*        margin: auto*/

/*        &:focus*/
/*            outline: none*/

/*    .full-width-banner*/
/*        width: 100%*/
/*        padding-bottom: 20px*/

/*    .text-white*/
/*        min-height: 320px*/

/*    .banner-margin*/
/*        margin-left: 15px*/
    /*.my-card*/
        /*width: 48%*/
</style>
