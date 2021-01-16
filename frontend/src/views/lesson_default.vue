<template>
    <!--     <q-banner elevated rounded inline-actions class="page-bar shadow-3">-->
    <!--              <q-banner >-->

    <div>

        <transition
                appear
                enter-active-class="animated fadeIn"
                leave-active-class="animated fadeOut"
        >


            <div class="row" style="padding: 20px">
                <q-card class="col-12 borderIt">
                    <!--BANNER-->
                    <q-banner rounded inline-actions class="page-bar">
                        <div class="row">
                            <div class="col-8 title" tabindex="0">
                                <div>Review Lesson</div>
                            </div>

                            <div class="col-1 offset-md-3" tabindex="0">
                                <div>
                                </div>

                                <q-btn
                                        class="edit_btn"
                                        dense
                                        size="16px"
                                        flat
                                        round
                                        color="gray"
                                        icon="o_save_alt"
                                        @click="downloadLesson"

                                        v-tooltip.left="{
                                              content: 'Download Lesson',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"

                                >
                                    <!--                                    <q-tooltip anchor="center left" self="center right"-->
                                    <!--                                    >Download Lesson-->
                                    <!--                                    </q-tooltip>-->
                                </q-btn>
                            </div>

                        </div>
                    </q-banner>


                </q-card>

                <div class="col-3">
                    <!--TITLE LESSON DATA-->
                    <div class="row">
                        <div class="q-left-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="updateLessonDialogPopup"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Lesson Information',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"
                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Lesson Information-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle">Lesson Title:</div>
                                    <div>{{ lesson.lesson_title }}</div>

                                    <div class="subtitle dialog-top ">Lesson Description:</div>
                                    <div>{{ lesson.lesson_description }}</div>

                                    <div class="subtitle dialog-top ">Class Name:</div>
                                    <div>{{ class_card_name(lesson.class_link) }}</div>

                                    <div class="subtitle dialog-top ">Grade:</div>
                                    <div>{{ class_card_grade(lesson.class_link) }}</div>
                                </q-card-section>


                            </q-card>
                        </div>
                    </div>

                    <!-- GOALS               -->
                    <div class="row">
                        <div class="q-left-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Goals')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Goals Selections',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"
                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Goals Selections-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div>
                                        <div class="subtitle ">Goals:</div>
                                        <ol class="ol_padding">
                                            <li
                                                    v-for="goal in lesson.selections.selected_goals"
                                                    :key="goal + 'goal'"
                                            >
                                                {{ getGoals(goal) }}
                                            </li>
                                        </ol>
                                    </div>
                                </q-card-section>
                            </q-card>

                            <q-btn
                                    v-if="is_editing"
                                    style="width: 100%; margin-top: 16px;"
                                    @click="postLessonUpdate"
                                    label="Update Lesson"
                                    color="black"
                                    unelevated
                            />

                            <q-btn
                                    v-if="is_duplicate"
                                    style="width: 100%; margin-top: 16px;"
                                    @click="postDuplicateLesson"
                                    label="Save Duplicate Lesson"
                                    color="black"
                                    unelevated
                            />

                            <q-btn
                                    v-if="is_new"
                                    style="width: 100%; margin-top: 16px;"
                                    @click="saveLesson"
                                    label="Save Lesson"
                                    color="black"
                                    unelevated
                            />

                        </div>


                    </div>
                </div>

                <div class="col-9">
                    <!--EVENTS-->

                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-6 col-md-6 col-lg-6">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            flat
                                            round
                                            color="gray"
                                            icon="help_outline"


                                            v-tooltip.top="{
                                              content: 'Events are not able to be edited because our curriculum\n'+
'                                            content differs for each event. If you wish to select a new\n'+
'                                            event please create a new lesson.',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"

                                    >


                                        <!--                                        -->
                                        <!--                                        <q-tooltip-->
                                        <!--                                                max-width="250px"-->
                                        <!--                                                anchor="top middle"-->
                                        <!--                                                self="bottom middle"-->
                                        <!--                                        >Events are not able to be edited because our curriculum-->
                                        <!--                                            content differs for each event. If you wish to select a new-->
                                        <!--                                            event please create a new lesson.-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle ">Event:</div>
                                    <div class="dialog-top">
                                        {{ eventFetch(lesson.selections.selected_event) }}
                                    </div>
                                </q-card-section>
                            </q-card>
                        </div>

                        <!-- READINGS                   -->
                        <div class="q-pa-md col-xs-12 col-sm-6 col-md-6 col-lg-6">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Readings')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Primary Reading',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"


                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Primary Reading-->
                                        <!--                                        </q-tooltip-->
                                        <!--                                        >-->
                                    </q-btn>

                                    <div class="subtitle -full">Primary Readings:</div>
                                    <div class="text-italic dialog-top">
                                        {{ readingFetch(lesson.selections.selected_reading) }}
                                    </div>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>

                    <!--EXPLORATIONS-->
                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Explorations')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.top="{
                                              content: 'Edit Further Explorations',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"

                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Further Explorations-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle -full">Further Explorations:</div>
                                    <ol class="ol_padding">
                                        <li
                                                v-for="ex in lesson.selections.selected_exploration"
                                                :key="ex + 'exploration'"
                                        >
                                            <span class="text-italic">{{ getExplorations(ex) }}</span>
                                        </li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>

                    <!--  LEXIS              -->
                    <!-- sets selected_lexis for lex computations-->
                    {{ setLex(lesson.selections.selected_lexis) }}

                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Lexis')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Lexis Selections',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"


                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Lexis Selections-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle">Lexis:</div>
                                    <div class="container">
                                        <div
                                                class="col"
                                                v-for="(column, index) in columns"
                                                :key="index"
                                        >
                                            <div
                                                    class="item-container"
                                                    v-for="lex in column"
                                                    :key="lex"
                                            >
                                                {{ getLexis(lex).term }}
                                            </div>
                                        </div>
                                    </div>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>

                    <!--QUESTIONS-->
                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Questions')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Lesson Questions',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"


                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Lesson Questions-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="row">
                                        <div class="col-6">
                                            <div class="subtitle -right ">Questions:</div>
                                            <ol class="ol_padding">
                                                <li
                                                        v-for="question in lesson.selections.selected_questions"
                                                        :key="question + 'question'"
                                                >
                                                    {{ getQuestions(question) }}
                                                </li>
                                            </ol>
                                        </div>

                                        <div class="col-6">
                                            <div class="subtitle -full col-6">Teacher Questions:</div>
                                            <ol class="ol_padding">
                                                <li
                                                        v-for="question in lesson.selections.user_questions"
                                                        :key="question.id"
                                                >
                                                    {{ question.user_question }}
                                                </li>
                                            </ol>
                                        </div>
                                    </div>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>

                    <!--PERFORMANCES-->
                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Performances')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Performance Selections',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"

                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Performance Selections-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle -full">Performances:</div>
                                    <ol class="ol_padding">
                                        <li
                                                v-for="perform in lesson.selections.selected_performances"
                                                :key="perform + 'performances'"
                                        >
                                            {{ getPerformances(perform) }}
                                        </li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>

                    <!--EXTENSIONS-->
                    <div class="row">
                        <div class="q-pa-md col-xs-12 col-sm-12 col-md-12 col-lg-12">
                            <q-card class="borderIt">
                                <q-card-section>
                                    <q-btn
                                            class="edit_btn"
                                            dense
                                            size="12px"
                                            @click="editPath('Extensions')"
                                            flat
                                            round
                                            color="gray"
                                            icon="o_edit"

                                            v-tooltip.left="{
                                              content: 'Edit Extension Selections',
                                              classes: ['info'],
                                              targetClasses: ['it-has-a-tooltip'],
                                              offset: 5,
                                              delay: {
                                                show: 500,
                                                hide: 300,
                                              },
                                            }"
                                    >
                                        <!--                                        <q-tooltip anchor="center left" self="center right"-->
                                        <!--                                        >Edit Extension Selections-->
                                        <!--                                        </q-tooltip>-->
                                    </q-btn>

                                    <div class="subtitle -full col-6">Extensions:</div>
                                    <ol class="ol_padding">
                                        <li
                                                v-for="ext in lesson.selections.selected_extensions"
                                                :key="ext + 'extensions'"
                                        >
                                            {{ getExtensions(ext) }}
                                        </li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </div>
                    </div>
                </div>


            </div>
        </transition>


        <q-inner-loading :showing="visible" class="qspin">
            <q-spinner size="50px" color="black"/>
        </q-inner-loading>


        <!--                                    <div class="subtitle dialog-top">Quote:</div>-->

        <!--                                    <div>"{{dialog.quotation}}"</div>-->
        <!--                                    <div class="dialog-top">{{dialog.quote_source}}</div>-->
        <!--                                    <div>{{dialog.quotation_author}}</div>-->

        <!--        </q-card-section>-->

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

        <!--        <CreateLessonDialog :class_options=class_options ref="newLessonDialog"/>-->
        <UpdateLessonInfo :class_options="class_options" ref="newLessonDialog"/>


        <!--        save dialog-->
        <q-dialog v-model="seamlessSave" seamless position="bottom">
            <!--        <q-dialog v-model="seamless" seamless position="bottom">-->
            <q-card dark style="width: 350px">
                <q-card-section class="row items-center justify-center no-wrap">
                    <div>
                        <div class="text-weight-bold">Lesson Saved</div>
                    </div>
                </q-card-section>
            </q-card>
        </q-dialog>


    </div>

    <!-- CREATE NEW LESSON DIALOG -->
    <!--    <CreateLessonDialog :class_options=class_options ref="newLessonDialog"/>-->

    <!--    <q-btn label="Save" @click="saveLesson"/>-->

    <!--    </q-card>-->

    <!--    </div>-->
    <!--     </q-banner>-->

    <!--    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">-->

    <!--    </div>-->
</template>

<script>
    import UpdateLessonInfo from "../components/lessons/UpdateLessonInfo";


    export default {
        components: {
            UpdateLessonInfo
        },
        // props: ['dialog', 'iconState'],
        name: "LexisDialog.vue",

        data() {
            return {

                msg: 'This is a button.',

                // lesson saved popup
                seamless: true,

                showing: false,
                preview_lesson_dialog: false,
                // lesson: {},
                cols: 4,
                selected_lexis: [],

                lesson_title: "",
                lesson_description: "",
                lesson_class: "",
                lesson_id: "",
                // is_editing: "",
                // is_duplicate: ""


                // loadthing
                visible: false,
                showSimulatedReturnData: false


            };
        },

        created() {
            //
            // this.is_editing = this.$store.getters['getIsEditing'];
            // this.is_duplicate = this.$store.getters['getIsDuplicate'];

            // this.$store.dispatch("fetchEvents");
            // this.lesson = this.$store.getters['getLesson'];
            //
            // this.lesson = this.$store.getters['getSelections'];
            // this.lesson_title = this.$store.getters['getLessonTitle'];
            // this.lesson_description = this.$store.getters['getLessonDescription'];
            // this.lesson_class = this.$store.getters['getClassID'];
        },

        computed: {


            seamlessSave: {
                get() {
                    return this.$store.getters['getSeamlessSave']
                },
                set(val) {
                    this.seamlessSave = val
                }
            },



            is_duplicate() {
                return this.$store.getters['getIsDuplicate'];
            },

            is_editing() {
                return this.$store.getters['getIsEditing'];
            },

            is_new() {
                return this.$store.getters['getIsNew'];
            },


            lesson() {
                return this.$store.getters["getLesson"];
            },

            class_options() {
                let class_list = [];
                let classes = this.$store.getters["getUserClasses"];
                classes.forEach(element => {
                    let data = {
                        label: element.class_name,
                        value: element.id
                    };
                    class_list.push(data);
                });

                return class_list;
            },

            // this dynamically sets the columns by computing selected lexis array in computations to
            // cut array and add new columns dynamically
            columns() {
                let columns = [];
                if (this.selected_lexis) {
                    let mid = Math.ceil(this.selected_lexis.length / this.cols);
                    for (let col = 0; col < this.cols; col++) {
                        columns.push(this.selected_lexis.slice(col * mid, col * mid + mid));
                    }
                }
                return columns;
            }
        },

        methods: {

            downloadLesson(){
                console.log('DOWNLOAD CLICKED')
            },


            // loading on save
            showTextLoading() {
                this.visible = true
                this.showSimulatedReturnData = false
                setTimeout(() => {
                    this.visible = false
                    this.showSimulatedReturnData = true
                }, 3000)
            },


            // forwards page to editing section
            editPath(path) {
                this.$router.push({name: path});
            },

            // SAVES NEW LESSON
            saveLesson() {
                this.showTextLoading();
                // console.log("SAVE LESSON CALLED");
                // console.log(
                //     "GET RETURN OF SELECTIONS",
                //     this.$store.getters["getSelections"]
                // );

                // bypass getters
                // console.log("DATA SELECTIONS", this.$store.state.lesson_store.lesson);

                // let payload =
                this.$store.dispatch("postLesson");
            },

            postLessonUpdate() {

                this.showTextLoading();
                this.$store.dispatch("postLessonUpdate");
            },


            postDuplicateLesson() {
                this.showTextLoading();
                this.$store.dispatch("postLesson");
            },

            updateLessonDialogPopup() {
                //   return element.id === lessonData.class_link;
                // this.new_lesson_title = lessonData.lesson_title;
                // this.lesson_description = lessonData.lesson_description;
                //
                //

                // let lessonData = {
                //     "lesson_title": this.lesson_title,
                //     "lesson_description": this.lesson_description,
                //     "class_link": this.lesson_class,
                //
                // };

                this.$refs.newLessonDialog.popupEdit();
            },

            // editLessonDialogPopup(lesson) {
            //     this.$refs.newLessonDialog.popupEdit(lesson);
            // },

            popupContent(lesson) {
                this.preview_lesson_dialog = true;
                this.lesson = lesson;
            },

            editLesson(lesson) {
                // console.log("LESSON", lesson);
                this.$store.dispatch("editLesson", lesson);
            },

            // DISPLAY DATA FUNCTIONS

            setLex(data) {
                this.selected_lexis = data;
            },

            eventFetch(id) {
                let events = this.$store.getters["getEvents"];
                let eventObj = events.find(element => element.id === id);
                if (eventObj) {
                    return eventObj.event_title;
                }
            },
            readingFetch(id) {
                let readings = this.$store.getters["getReadings"];
                let book = readings.find(element => element.id === id);
                if (book) {
                    return book.title_major;
                }
            },

            class_card_grade(id) {
                let classes = this.$store.getters["getUserClasses"];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.grade_level;
                } else {
                    return;
                }
            },

            class_card_name(id) {
                let classes = this.$store.getters["getUserClasses"];
                let classObj = classes.find(element => element.id === id);
                if (classObj) {
                    return classObj.class_name;
                } else {
                    return;
                }
            },

            getLexis(id) {
                // console.log("GETLEXIS", id);
                // loop through items and return the item with the matching id
                let lexis = this.$store.getters["getLexis"];
                // console.log('LEX', lex);

                let lex = lexis.find(element => element.id === id);
                if (lex) {
                    return lex;
                    // return lex.term;

                } else {
                    return;
                }
            },

            getExplorations(id) {
                // console.log("GETEX", id);
                // loop through items and return the item with the matching id
                let explorations = this.$store.getters["getExplorations"];
                // console.log('LEX', lex);

                let ex = explorations.find(element => element.id === id);
                if (ex) {
                    return ex.title_minor + " (" + ex.reading_category.category_name + ")";
                } else {
                    return;
                }
            },

            getQuestions(id) {
                // console.log("GETQUESTION", id);
                // loop through items and return the item with the matching id
                let questions = this.$store.getters["getQuestions"];
                // console.log('LEX', lex);

                let question = questions.find(element => element.id === id);
                if (question) {
                    return question.question;
                } else {
                    return;
                }
            },

            getPerformances(id) {
                // console.log("GETPERF", id);
                // loop through items and return the item with the matching id
                let performances = this.$store.getters["getPerformances"];
                // console.log("PERFORMANCES", performances);

                // console.log('LEX', lex);

                let perf = performances.find(element => element.id === id);
                if (perf) {
                    return perf.performance_title;
                } else {
                    return;
                }
            },

            getExtensions(id) {
                // console.log("GETPERF", id);
                // loop through items and return the item with the matching id
                let extensions = this.$store.getters["getExtensions"];
                // console.log('PERFORMANCES', extensions);

                // console.log('LEX', lex);

                let ext = extensions.find(element => element.id === id);
                if (ext) {
                    return ext.action;
                } else {
                    return;
                }
            },

            getGoals(id) {
                // console.log('GETPERF', id);
                // loop through items and return the item with the matching id
                let goals = this.$store.getters["getGoals"];
                // console.log('PERFORMANCES', extensions);

                // console.log('LEX', lex);

                let goal = goals.find(element => element.id === id);
                if (goal) {
                    return goal.goal;
                } else {
                    return;
                }
            }
        }
    }
    ;
</script>

<style scoped>

    .qspin {
        margin-top: -300px;
    }

    .test {
        margin-top: 0 !important;
        margin-left: 0 !important;
    }

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
        /*border-bottom: 1px solid rgba(0, 0, 0, 0.12);*/
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
        color: gray;
        font-weight: normal;
        /*border-bottom: 1px solid gray;*/
    }

    .subtitle-line {
        border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    }

    .subtitle-line-right {
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

    .gutter {
        margin-top: 20px;
        margin-left: 20px;
    }

    .q-pa-md {
        padding: 16px 0 0 16px !important;
    }

    .q-left-pa-md {
        padding: 16px 0 0 0 !important;
    }

    .edit_btn {
        float: right;
        margin-top: -5px;
    }


    .borderIt {
        border: 1px solid rgba(0, 0, 0, 0.12);
    }


    text-weight-bold {
        text-align: center;
    }


</style>

<!--<template>-->

<!--&lt;!&ndash;     <q-banner elevated rounded inline-actions class="page-bar shadow-3">&ndash;&gt;-->
<!--&lt;!&ndash;              <q-banner >&ndash;&gt;-->

<!--                <div class="row" style="padding: 20px">-->

<!--                    <q-card class="col-12" >-->

<!--        <q-card-section class="row items-center q-pb-none">-->
<!--            <div class="text-h6">{{lesson_title}}-->

<!--            </div>-->
<!--            <q-space/>-->
<!--            <span> <q-btn flat round color="gray" icon="o_file_copy"/>-->
<!--                           <q-btn @click="editLesson(lesson)" flat round color="gray" icon="o_edit"/>-->
<!--                    </span>-->
<!--            <q-btn icon="close" flat round dense v-close-popup/>-->
<!--        </q-card-section>-->

<!--        <q-separator/>-->
<!--        <div class="row">-->
<!--            <q-card-section class="col-3 ">-->

<!--                <div class="subtitle subtitle-line">Lesson Description:-->
<!--                    <q-btn @click="updateLessonDialogPopup" flat round color="gray" icon="o_edit"/>-->
<!--                </div>-->
<!--                <div>{{lesson_description}}</div>-->

<!--                <div class="subtitle dialog-top subtitle-line">Class Name:</div>-->
<!--                <div>{{class_card_name(lesson_class)}}</div>-->

<!--                <div class="subtitle dialog-top subtitle-line">Grade:</div>-->
<!--                <div>{{class_card_grade(lesson_class)}}</div>-->

<!--                <div>-->
<!--                    <div class="subtitle dialog-top subtitle-line">Goals:</div>-->
<!--                    <ol class="ol_padding">-->
<!--                        <li v-for="goal in lesson.selected_goals" :key="goal+'goal'">-->
<!--                            {{getGoals(goal)}}-->
<!--                        </li>-->
<!--                    </ol>-->
<!--                </div>-->

<!--                <q-separator/>-->

<!--                <q-btn @click="postLessonUpdate" label="Update Lesson"  color="primary"/>-->

<!--                <q-separator vertical/>-->

<!--            </q-card-section>-->
<!--            <q-card-section class="col-9 ">-->
<!--                <div class="row">-->

<!--                    <div class="col-6">-->

<!--                        <div class="subtitle subtitle-line">Event:</div>-->
<!--                        <div class="dialog-top">{{eventFetch(lesson.selected_event)}}</div>-->
<!--                    </div>-->

<!--                    <div class="col-6">-->

<!--                        <div class="subtitle subtitle-line-full">Reading:</div>-->
<!--                        <div class="text-italic dialog-top">{{readingFetch(lesson.selected_reading)}}</div>-->
<!--                    </div>-->

<!--                </div>-->

<!--                &lt;!&ndash; sets selected_lexis for lex computations&ndash;&gt;-->
<!--                {{setLex(lesson.selected_lexis)}}-->

<!--                <div class="subtitle dialog-top">Lexis:</div>-->
<!--                <div class="container">-->
<!--                    <div class="col" v-for="(column, index) in columns" :key="index">-->
<!--                        <div class="item-container" v-for="lex in column" :key="lex">{{getLexis(lex)}}</div>-->
<!--                    </div>-->
<!--                </div>-->

<!--                <div class="subtitle dialog-top subtitle-line-full">Further Explorations:</div>-->
<!--                <ol class="ol_padding">-->
<!--                    <li v-for="ex in lesson.selected_exploration" :key="ex+'exploration'">-->
<!--                        <span class="text-italic">{{getExplorations(ex)}}</span>-->
<!--                    </li>-->
<!--                </ol>-->

<!--                <div class="subtitle subtitle-line-full">Performances:</div>-->
<!--                <ol class="ol_padding">-->
<!--                    <li v-for="perform in lesson.selected_performances" :key="perform+'performances'">-->
<!--                        {{getPerformances(perform)}}-->
<!--                    </li>-->
<!--                </ol>-->

<!--                <div class="row">-->
<!--                    <div class="col-6">-->
<!--                        <div class="subtitle subtitle-line ">Questions:</div>-->
<!--                        <ol class="ol_padding">-->
<!--                            <li v-for="question in lesson.selected_questions" :key="question+'question'">-->
<!--                                {{getQuestions(question)}}-->
<!--                            </li>-->
<!--                        </ol>-->
<!--                    </div>-->

<!--                    <div class="col-6">-->
<!--                        <div class="subtitle subtitle-line-full col-6">Teacher Questions:</div>-->
<!--                        <ol class="ol_padding">-->
<!--                            <li v-for="question in lesson.user_questions" :key="question.id">-->
<!--                                {{question.user_question}}-->
<!--                            </li>-->
<!--                        </ol>-->
<!--                    </div>-->

<!--                    <div class="col-12">-->
<!--                        <div class="subtitle subtitle-line-full col-6">Extensions:</div>-->
<!--                        <ol class="ol_padding">-->
<!--                            <li v-for="ext in lesson.selected_extensions" :key="ext+'extensions'">-->
<!--                                {{getExtensions(ext)}}-->
<!--                            </li>-->
<!--                        </ol>-->
<!--                    </div>-->

<!--                </div>-->

<!--                &lt;!&ndash;                                    <div class="subtitle dialog-top">Quote:</div>&ndash;&gt;-->

<!--                &lt;!&ndash;                                    <div>"{{dialog.quotation}}"</div>&ndash;&gt;-->
<!--                &lt;!&ndash;                                    <div class="dialog-top">{{dialog.quote_source}}</div>&ndash;&gt;-->
<!--                &lt;!&ndash;                                    <div>{{dialog.quotation_author}}</div>&ndash;&gt;-->

<!--            </q-card-section>-->

<!--            &lt;!&ndash;                                <q-card-section class="col-5 ">&ndash;&gt;-->
<!--            &lt;!&ndash;                                    <div class="subtitle">Applications:</div>&ndash;&gt;-->
<!--            &lt;!&ndash;                                    <ul class="indent">&ndash;&gt;-->
<!--            &lt;!&ndash;                                        <li v-for="application in dialog.application" :key="application.id">&ndash;&gt;-->
<!--            &lt;!&ndash;                                            {{application.value}}&ndash;&gt;-->
<!--            &lt;!&ndash;                                        </li>&ndash;&gt;-->
<!--            &lt;!&ndash;                                    </ul>&ndash;&gt;-->
<!--            &lt;!&ndash;                                    <q-separator vertical/>&ndash;&gt;-->

<!--            &lt;!&ndash;                                    <div class="subtitle dialog-top">Exploration:</div>&ndash;&gt;-->
<!--            &lt;!&ndash;                                    <ol class="indent">&ndash;&gt;-->
<!--            &lt;!&ndash;                                        <li v-for="exploration in dialog.exploration" :key="exploration.id">&ndash;&gt;-->
<!--            &lt;!&ndash;                                            {{exploration.value}}&ndash;&gt;-->
<!--            &lt;!&ndash;                                        </li>&ndash;&gt;-->
<!--            &lt;!&ndash;                                    </ol>&ndash;&gt;-->

<!--            &lt;!&ndash;                                </q-card-section>&ndash;&gt;-->

<!--        </div>-->

<!--        &lt;!&ndash; CREATE NEW LESSON DIALOG &ndash;&gt;-->
<!--        <CreateLessonDialog :class_options=class_options ref="newLessonDialog"/>-->

<!--         <q-btn label="Save" @click="saveLesson"/>-->

<!--    </q-card>-->

<!--                </div>-->
<!--&lt;!&ndash;     </q-banner>&ndash;&gt;-->

<!--&lt;!&ndash;    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">&ndash;&gt;-->

<!--&lt;!&ndash;    </div>&ndash;&gt;-->
<!--</template>-->
