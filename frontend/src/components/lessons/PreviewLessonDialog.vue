<template>

    <!--        xxx lesson_title-->
    <!--        xxx lesson_description-->
    <!--        xxx class_link ""-->
    <!--        xxx selected_event: '', id-->
    <!--        xxx selected_reading: '',-->
    <!--        xxx selected_related_events: [],-->
    <!--        xxx selected_exploration: [],-->
    <!--        xxx selected_lexis: [],-->
    <!--        xxx selected_questions: [],-->
    <!--        xxx selected_performances: [],-->
    <!--        xxx selected_extensions: [],-->
    <!--        xxx selected_goals: [],-->
    <!--        xxx user_questions: []-->


    <q-dialog v-model="preview_lesson_dialog">
        <q-card class="lex-card">

            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{lesson.lesson_title}}

                </div>
                <q-space/>
                <span> <q-btn @click="duplicateLesson(lesson)" flat round color="gray" icon="o_file_copy"/>
                           <q-btn @click="editLesson(lesson)" flat round color="gray" icon="o_edit"/>
                    </span>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">
                <q-card-section class="col-3 ">

                    <div class="subtitle subtitle-line">Lesson Description:</div>
                    <div>{{lesson.lesson_description}}</div>

                    <div class="subtitle dialog-top subtitle-line">Class Name:</div>
                    <div>{{class_card_name(lesson.class_link)}}</div>

                    <div class="subtitle dialog-top subtitle-line">Grade:</div>
                    <div>{{class_card_grade(lesson.class_link)}}</div>

                    <div>
                        <div class="subtitle dialog-top subtitle-line">Goals:</div>
                        <ol class="ol_padding">
                            <li v-for="goal in lesson.goals" :key="goal+'goal'">
                                {{getGoals(goal)}}
                            </li>
                        </ol>
                    </div>

                    <q-separator/>


                    <q-separator vertical/>

                </q-card-section>
                <q-card-section class="col-9 ">
                    <div class="row">

                        <div class="col-6">

                            <div class="subtitle subtitle-line">Event:</div>
                            <div class="dialog-top">{{eventFetch(lesson.event)}}</div>
                        </div>

                        <div class="col-6">

                            <div class="subtitle subtitle-line-full">Reading:</div>
                            <div class="text-italic dialog-top">{{readingFetch(lesson.event)}}</div>
                        </div>


                    </div>


                    <!-- sets selected_lexis for lex computations-->
                    {{setLex(lesson.lexis)}}

                    <div class="subtitle dialog-top">Lexis:</div>
                    <div class="container">
                        <div class="col" v-for="(column, index) in columns" :key="index">
                            <div class="item-container" v-for="lex in column" :key="lex">{{getLexis(lex)}}</div>
                        </div>
                    </div>

                    <div class="subtitle dialog-top subtitle-line-full">Further Explorations:</div>
                    <ol class="ol_padding">
                        <li v-for="ex in lesson.explorations" :key="ex+'exploration'">
                            <span class="text-italic">{{getExplorations(ex)}}</span>
                        </li>
                    </ol>

                    <div class="subtitle subtitle-line-full">Performances:</div>
                    <ol class="ol_padding">
                        <li v-for="perform in lesson.performances" :key="perform+'performances'">
                            {{getPerformances(perform)}}
                        </li>
                    </ol>


                    <div class="row">
                        <div class="col-6">
                            <div class="subtitle subtitle-line ">Questions:</div>
                            <ol class="ol_padding">
                                <li v-for="question in lesson.questions" :key="question+'question'">
                                    {{getQuestions(question)}}
                                </li>
                            </ol>
                        </div>

                        <div class="col-6">
                            <div class="subtitle subtitle-line-full col-6">Teacher Questions:</div>
                            <ol class="ol_padding">
                                <li v-for="question in lesson.user_questions" :key="question.id">
                                    {{question.user_question}}
                                </li>
                            </ol>
                        </div>

                        <div class="col-12">
                            <div class="subtitle subtitle-line-full col-6">Extensions:</div>
                            <ol class="ol_padding">
                                <li v-for="ext in lesson.extensions" :key="ext+'extensions'">
                                    {{getExtensions(ext)}}
                                </li>
                            </ol>
                        </div>


                    </div>


                    <!--                                    <div class="subtitle dialog-top">Quote:</div>-->

                    <!--                                    <div>"{{dialog.quotation}}"</div>-->
                    <!--                                    <div class="dialog-top">{{dialog.quote_source}}</div>-->
                    <!--                                    <div>{{dialog.quotation_author}}</div>-->


                </q-card-section>

                <!--                                <q-card-section class="col-5 ">-->
                <!--                                    <div class="subtitle">Applications:</div>-->
                <!--                                    <ul class="indent">-->
                <!--                                        <li v-for="application in dialog.application" :key="application.id">-->
                <!--                                            {{application.value}}-->
                <!--                                        </li>-->
                <!--                                    </ul>-->
                <!--                                    <q-separator vertical/>-->

                <!--                                    <div class="subtitle dialog-top">Exploration:</div>-->
                <!--                                    <ol class="indent">-->
                <!--                                        <li v-for="exploration in dialog.exploration" :key="exploration.id">-->
                <!--                                            {{exploration.value}}-->
                <!--                                        </li>-->
                <!--                                    </ol>-->

                <!--                                </q-card-section>-->

            </div>
        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        // props: ['dialog', 'iconState'],
        name: "LexisDialog.vue",

        data() {
            return {
                preview_lesson_dialog: false,
                lesson: {},
                cols: 5,
                selected_lexis: [],

                lesson_description: ''
            }
        },

        created() {
            // this.$store.dispatch("fetchEvents");
        },

        computed: {

            // this dynamically sets the columns by computing selected lexis array in computations to
            // cut array and add new columns dynamically
            columns() {
                let columns = [];
                if (this.selected_lexis) {
                    let mid = Math.ceil(this.selected_lexis.length / this.cols);
                    for (let col = 0; col < this.cols; col++) {
                        columns.push(this.selected_lexis.slice(col * mid, col * mid + mid))
                    }
                }
                return columns
            }
        },

        methods: {

            editLesson(lesson) {

                // console.log('LESSON', lesson);
                // this.$store.dispatch('editLesson', lesson);
                // this.$router.push({name: 'Lesson'});

                this.$store.dispatch('editLesson', lesson);
                this.$router.push({name: 'Lesson'});

            },

            duplicateLesson(lesson){

                console.log('LESSON', lesson);

                lesson.lesson_title = lesson.lesson_title + " NEW";
                this.$store.dispatch('duplicateLesson', lesson);
                this.$router.push({name: 'Lesson'});


            },

            setLex(data) {
                this.selected_lexis = data
            },

            eventFetch(id) {
                let events = this.$store.getters['getEvents'];
                let eventObj = events.find(element => element.id === id);
                if (eventObj) {
                    return eventObj.event_title
                }

            },
            readingFetch(id) {
                let readings = this.$store.getters['getReadings'];
                let book = readings.find(element => element.id === id);
                if (book) {
                    return book.title_major
                }

            },

            popupContent(lesson) {
                this.preview_lesson_dialog = true;
                this.lesson = lesson
            },

            class_card_grade(id) {
                let classes = this.$store.getters['getUserClasses'];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.grade_level
                } else {
                    return
                }
            },

            class_card_name(id) {
                let classes = this.$store.getters['getUserClasses'];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.class_name
                } else {
                    return
                }
            },

            getLexis(id) {

                console.log('GETLEXIS', id);
                // loop through items and return the item with the matching id
                let lexis = this.$store.getters['getLexis'];
                // console.log('LEX', lex);

                let lex = lexis.find(element => element.id === id);
                if (lex) {
                    return lex.term
                } else {
                    return
                }
            },

            getExplorations(id) {

                console.log('GETEX', id);
                // loop through items and return the item with the matching id
                let explorations = this.$store.getters['getExplorations'];
                // console.log('LEX', lex);

                let ex = explorations.find(element => element.id === id);
                if (ex) {
                    return ex.title_minor
                } else {
                    return
                }
            },

            getQuestions(id) {

                console.log('GETQUESTION', id);
                // loop through items and return the item with the matching id
                let questions = this.$store.getters['getQuestions'];
                // console.log('LEX', lex);

                let question = questions.find(element => element.id === id);
                if (question) {
                    return question.question
                } else {
                    return
                }
            },

            getPerformances(id) {

                console.log('GETPERF', id);
                // loop through items and return the item with the matching id
                let performances = this.$store.getters['getPerformances'];
                console.log('PERFORMANCES', performances);

                // console.log('LEX', lex);

                let perf = performances.find(element => element.id === id);
                if (perf) {
                    return perf.performance_title
                } else {
                    return
                }
            },

            getExtensions(id) {

                console.log('GETPERF', id);
                // loop through items and return the item with the matching id
                let extensions = this.$store.getters['getExtensions'];
                // console.log('PERFORMANCES', extensions);

                // console.log('LEX', lex);

                let ext = extensions.find(element => element.id === id);
                if (ext) {
                    return ext.action
                } else {
                    return
                }
            },


            getGoals(id) {

                // console.log('GETPERF', id);
                // loop through items and return the item with the matching id
                let goals = this.$store.getters['getGoals'];
                // console.log('PERFORMANCES', extensions);

                // console.log('LEX', lex);

                let goal = goals.find(element => element.id === id);
                if (goal) {
                    return goal.goal
                } else {
                    return
                }
            },


        },


    }
</script>

<style scoped>

    .container {
        display: flex;
        /*border: 1px solid;*/
    }

    .col {
        margin: 5px 0 10px 0;
        /*border: 1px solid;*/
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

    .item-container {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
        padding: 0px;
        margin: 1px 8px 1px 0;

    }

    .lex-card {
        min-width: 80%;
    }

    .ol_padding {
        padding-inline-start: 20px;

    }

    .subtitle {
        /*border-bottom: 1px solid gray;*/
    }

    .subtitle-line {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
        margin-right: 20px;
    }

    .subtitle-line-full {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
        /*margin-right: 20px;*/
    }

    .text-italic {
        font-style: italic;
    }


</style>