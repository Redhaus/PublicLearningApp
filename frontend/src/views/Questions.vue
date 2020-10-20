<template>
    <!--<q-scroll-area >-->

    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">
        <div class="col-12">
            <SearchHeader name="Questions" @searchTerm="search = $event"/>
        </div>

        <div style="width: 100%">

            <div v-if="selected_event">
                <div v-if="questions_list.length > 0">
                    <masonry :cols="4" :gutter="20">
                        <div v-for="question in questions_list" :key="question.id" class="bottom-padding">
                            <q-card
                                    :class="{ active: selected_list.includes(question.id) }"
                                    bordered
                                    @click="eventAction(question.id)"
                                    class="cardHandle"
                            >
                                <q-card-section>
                                    <div v-html="question.question"></div>
                                </q-card-section>
                            </q-card>
                        </div>

                    </masonry>


                    <!-- separate user questions-->


                    <div v-if="user_question_list.length > 0">
                        <q-separator/>

                        <!--                        <masonry :cols="4" :gutter="20">-->
                        <div style="padding-top: 15px">
                            <div v-for="user_question in user_question_list" :key="user_question.id"
                                 class="bottom-padding row" style="width: 100%">
                                <q-card

                                        bordered
                                        class="cardHandle active-user-question col-12"
                                >
                                    <q-card-section class="bottom-padding row items-center">
                                        <div class="col-10">{{user_question.user_question}}


                                        </div>
                                        <div class="col-2">

                                            <q-btn @click="deleteConfirmation(user_question)" class="deleteBtn" flat
                                                   round icon="close"/>
                                            <q-btn @click="editQuestion(user_question)" class="deleteBtn" flat
                                                   round icon="edit"/>
                                        </div>
                                    </q-card-section>


                                </q-card>

                            </div>
                        </div>
                        <!--                        </masonry>-->


                        <div style="height: 100px"></div>
                    </div>


                    <!--                    <q-page-container>-->
                    <!--                        <q-page padding>-->

<!--                    <div class="qfoot">-->

                                                    <q-page-sticky class="slideUp" expand position="bottom">
                        <div class="col-12">
                            <q-banner elevated rounded inline-actions class="page-bar shadow-3">

                                <q-input v-on:keyup.enter="save_user_question" bottom-slots
                                         v-model="user_question_input" label="Add Additional Question">
                                    <!--        <template v-slot:before>-->
                                    <!--          <q-icon name="event" />-->
                                    <!--        </template>-->

                                    <template v-slot:hint>
                                        Add any additional question you would like associated with this lesson.
                                    </template>

                                    <template v-slot:append>
                                        <q-btn @click="save_user_question" round dense flat icon="add"/>
                                    </template>
                                </q-input>


                                <!--                                <q-toolbar class="">-->
                                <!--&lt;!&ndash;                                    <q-avatar>&ndash;&gt;-->
                                <!--&lt;!&ndash;                                    </q-avatar>&ndash;&gt;-->
                                <!--                                    <q-toolbar-title>-->
                                <!--                                        <q-input v-model="user_question_input" label="Additional Question"/>-->

                                <!--                                    </q-toolbar-title>-->
                                <!--                                </q-toolbar>-->
                            </q-banner>
                        </div>
<!--                    </div>-->
                                                </q-page-sticky>
                    <!--                        </q-page>-->


                    <!--                    </q-page-container>-->


                    <!--                         <q-footer reveal elevated>-->
                    <!--        <q-toolbar>-->
                    <!--&lt;!&ndash;          <q-btn flat round dense icon="menu" @click="drawerLeft = !drawerLeft" />&ndash;&gt;-->

                    <!--          <q-toolbar-title>-->
                    <!--            <strong>Question</strong>-->
                    <!--          </q-toolbar-title>-->

                    <!--&lt;!&ndash;          <q-btn flat round dense icon="menu" @click="drawerRight = !drawerRight" />&ndash;&gt;-->
                    <!--        </q-toolbar>-->
                    <!--      </q-footer>-->


                </div>
                <div v-else>No Questions Available</div>


            </div>

            <div v-else>Please select an Event</div>

        </div>


        <div style="height: 50px"/>
    </div>
</template>
<script>
    import {v4 as uuidv4} from 'uuid';
    import SearchHeader from "../components/SearchHeader";

    export default {
        components: {
            SearchHeader,
        },
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                // question_id_list: [],
                search: "",
                user_question_input: '',
                // user_question: {}
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchQuestions");
            // this.question_id_list = this.$store.getters["getSelectedQuestions"];
        },

        computed: {

            selected_list() {
                return this.$store.getters["getSelectedQuestions"];
            },

            // this makes sure there is selected event before content is displayed
            selected_event() {
                return this.$store.getters["getSelectedEvent"];
            },

            questions_list() {
                let questions = this.$store.getters["getQuestions"];

                // console.log(this.search);

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
            },

            // displays list of user_questions if any
            user_question_list() {
                // fetches latest list from lesson store
                var array = this.$store.getters['getUserQuestions'];

                return array.reverse()
            }
        },

        methods: {

            set(question) {
                console.log('QUESTOPM', question)
            },

            editQuestion(question) {
                this.user_question_input = question.user_question;
                this.deleteQuestion(question.id)
            },

            deleteQuestion(id) {
                this.$store.dispatch('deleteUserQuestion', id)

            },

            // confirms delete of question
            deleteConfirmation(question) {

                this.$q.dialog({
                    title: 'Confirm Delete',
                    message: question.user_question,
                    cancel: true,
                    persistent: true,
                    ok: {
                        label: 'Delete',
                        flat: true,
                        textColor: 'red'
                    }
                }).onOk(() => {
                    console.log('QUESTIONID', question.id);
                    this.deleteQuestion(question.id)

                }).onOk(() => {
                    // console.log('>>>> second OK catcher')
                }).onCancel(() => {
                    // console.log('>>>> Cancel')
                }).onDismiss(() => {
                    // console.log('I am triggered on both OK and Cancel')
                })

            },

            save_user_question() {


                let data = {
                    'id': uuidv4(),
                    'user_question': this.user_question_input
                };
                this.$store.dispatch('setUserQuestions', data);
                this.user_question_input = '';


            },


            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                this.$store.dispatch("setSelectedQuestions", event);


                // if (this.question_id_list.includes(event)) {
                //     this.$store.dispatch("setSelectedQuestions", event);
                //
                //     this.question_id_list = this.question_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.$store.dispatch("setSelectedQuestions", event);
                //     this.question_id_list.push(event);
                // }
            }
        }
    };
</script>

<style lang="scss" scoped>

    .deleteBtn {
        float: right;
    }

    .active {
        background-color: #cccccc;
    }

    .active-user-question {

        background-color: #cccccc
    }

    /*.qfoot {*/
    /*    position: fixed;*/
    /*    width: 100%;*/
    /*    bottom: 0;*/
    /*}*/


    .slideUp {

          -webkit-animation: slideUp 1s ease-in-out 1s forwards;

            animation: slideUp 1s ease-in-out 1s forwards;

        /*animation-name: slideUp;*/
        /*-webkit-animation-name: slideUp;*/

        /*animation-duration: 1s;*/
        /*-webkit-animation-duration: 1s;*/

        /*animation-timing-function: ease-in-out;*/
        /*-webkit-animation-timing-function: ease-in-out;*/

        /*animation-delay: 1s;*/
        opacity: 0;

        /*visibility: hidden !important;*/
    }

    @keyframes slideUp {
        0% {
            transform: translateY(100%);
            opacity: 0;
            /*visibility: visible !important;*/

        }

        100% {
            transform: translateX(0%);
            opacity: 1;
                        /*visibility: visible !important;*/

        }
    }

    @-webkit-keyframes slideUp {
        0% {
            -webkit-transform: translateX(100%);
            opacity: 0;

        }

        100% {
            -webkit-transform: translateX(0%);
            opacity: 1;
        }
    }


</style>
