<template>
    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">

        <div class="col-12">
            <LessonSearchHeader
                    :class_options_filter=class_options_filter
                    @searchTerm="search = $event"
                    @classFilter="class_selection_filter = $event"/>
        </div>

        <div style="width: 100%">
            <div v-if="lesson_list.length > 0">

                <masonry :cols="4" :gutter="20">
                    <!--  Add Card Button-->
                    <div class="bottom-padding">
                        <q-card
                                class="cardHandle addLesson row justify-center items-center"
                                bordered
                                @click="newLessonDialogPopup">
                            <q-card-section>
                                <q-icon class="plusIcon" name="fas fa-plus"></q-icon>
                            </q-card-section>
                        </q-card>
                    </div>

                    <!-- Lesson Cards-->
                    <div v-for="lesson in lesson_list" :key="lesson.id" class="bottom-padding">


                        <q-card
                                class="cardHandle addLesson"
                                :class="{ active: lesson_id_list === lesson.id }"
                                bordered
                                >


                            <q-item>
                                <q-item-section avatar>
                                    <q-avatar>
                                        <q-icon color="gray" name="o_description" size="40px"/>
                                    </q-avatar>
                                </q-item-section>
                                <q-item-section class="grade-class">
                                    <q-item-label caption>Grade {{class_card_grade(lesson.class_link)}}</q-item-label>

                                </q-item-section>
                            </q-item>

                            <q-item>

                                <q-item-section>

                                    <q-item-label caption>Lesson Title</q-item-label>
                                    <q-item-label>{{lesson.lesson_title}}</q-item-label>
                                </q-item-section>
                            </q-item>

                            <q-item>

                                <q-item-section>
                                    <q-item-label caption>Class</q-item-label>
                                    <q-item-label>{{class_card_name(lesson.class_link)}}</q-item-label>
                                </q-item-section>
                            </q-item>

<!--                            <q-item>-->

<!--                                <q-item-section>-->
<!--                                    <q-item-label caption>Description</q-item-label>-->
<!--                                    <q-item-label>{{lesson.lesson_description}}</q-item-label>-->
<!--                                </q-item-section>-->
<!--                            </q-item>-->


                            <q-separator class="separator-bottom"  />


                            <q-card-actions class="items-bottom" align="right">
                                <q-btn @click="previewLessonDialogPopup(lesson)" flat round color="gray" icon="o_open_in_new"/>
                                <q-btn flat round color="gray" icon="o_file_copy"/>
                                <q-btn flat round color="gray" icon="o_edit"/>
                                <q-btn @click="deleteConfirmation(lesson)" flat round color="gray" icon="o_delete"/>
                            </q-card-actions>


                        </q-card>
                    </div>

                </masonry>

                <q-separator/>

                <div>
                    <q-btn @click="newClassDialogPopup" color="primary" label="Create Class"/>
                </div>


                <!-- CREATE NEW LESSON DIALOG -->
                <CreateLessonDialog :class_options=class_options ref="newLessonDialog" />

                <!-- CREATE NEW CLASS DIALOG -->
                <CreateClassDialog ref="newClassDialog"/>

                <PreviewLessonDialog ref="previewLessonDialog" />

            </div>


            <div v-else>No Lesson Available</div>

        </div>


    </div>
</template>
<script>
    import LessonSearchHeader from "../components/lessons/LessonSearchHeader";
    import CreateClassDialog from "../components/lessons/CreateClassDialog";
    import CreateLessonDialog from "../components/lessons/CreateLessonDialog";
    import PreviewLessonDialog from "../components/lessons/PreviewLessonDialog";


    export default {

        components: {
            LessonSearchHeader,
            CreateClassDialog,
            CreateLessonDialog,
            PreviewLessonDialog
        },
        data() {
            return {

                // Filters
                class_selection_filter: {
                    label: 'All',
                    value: 'all'
                },
                search: '',
                filter: '',

                // LESSON CONTENT
                // new_lesson_title: '',
                // class_selection: null,
                // lesson_description: '',

                // CONTENT DISPLAY
                lesson_id_list: '',
                lexis: [],
                selections: {},

            };
        },

        methods: {


             // CONFIRMATION DELETE DIALOG
            deleteConfirmation(lesson) {

                this.$q.dialog({
                    title: 'Confirm Delete',
                    message: lesson.lesson_title,
                    cancel: true,
                    persistent: true,
                    ok: {
                        label: 'Delete',
                        flat: true,
                        textColor: 'red'
                    }
                }).onOk(() => {
                    console.log('CLASSED', lesson.id);
                    this.deleteLesson(lesson.id)
                }).onCancel(() => {
                })
            },

            deleteLesson(id) {
                this.$store.dispatch('deleteUserLesson', id)
            },



            class_card_grade(id) {
                // console.log('IDIDID', id);
                let classes = this.$store.getters['getUserClasses'];
                // console.log('CLASSES', classes);
                let classObj = classes.find(element => element.id === id);
                // console.log('CLASSOBJ', classObj);
                if (classObj) {
                    return classObj.grade_level
                } else {
                    return
                }
            },

            class_card_name(id) {
                // console.log('IDIDID', id);
                let classes = this.$store.getters['getUserClasses'];
                // console.log('CLASSES', classes);
                let classObj = classes.find(element => element.id === id);
                // console.log('CLASSOBJ', classObj);
                if (classObj) {
                    return classObj.class_name
                } else {
                    return
                }
            },


            newLessonDialogPopup() {
                this.$refs.newLessonDialog.popupContent();
            },

            // calls popup for create class
            newClassDialogPopup() {
                this.$refs.newClassDialog.popupAdd();
            },

            // calls popup for create class
            previewLessonDialogPopup(lesson) {
                this.$refs.previewLessonDialog.popupContent(lesson);
            },

            //
            // createNewLesson() {
            //
            //     let lessonData = {
            //         title: this.new_lesson_title,
            //         description: this.lesson_description,
            //         class_id: this.class_selection.value
            //     };
            //
            //     this.$store.dispatch("postLessonTitle", lessonData);
            //
            //     // FORWARD TO EVENTS SECTION
            //     this.$router.push({name: 'Events'});
            //
            //
            // },


            addLesson() {
                // console.log('Add Lesson');
                this.create_new_lesson = true;
            },

            // lexList(data){
            //     // var obj = JSON.parse(data);
            //     // console.log(obj);
            //     // return obj
            //
            //      return  data.selected_lexis.forEach(element => {
            //         console.log('RETURN', this.getLexis(element));
            //         return this.getLexis(element);
            //     });
            //
            //      // console.log('TERM', term)
            //
            //     // console.log('LEXLIST', data.selected_lexis);
            //     // this.getLexis(data.selected_lexis);
            //
            // },

            saveLesson() {

                // console.log('SAVE LESSON CALLED');
                // console.log('GET RETURN OF SELECTIONS', this.$store.getters["getSelections"]);

                // bypass getters
                // console.log('DATA SELECTIONS', this.$store.state.lesson_store.lesson);


                // let payload = ;
                this.$store.dispatch("postLesson", this.selections);

            },

            // this fetches the words based on id passed
            getLexis(id) {

                // console.log('GETLEXIS', id);

                // console.log('ID', id);
                // loop through items and return the item with the matching id
                // let lex = this.$store.state.lexis_store.lexis.find(item => item.id === id);
                let lex = this.$store.getters['getLexis'].find(item => item.id === id);
                // console.log('LEX', lex.term);

                // return lex.term;
                if (lex) {
                    // console.log('LEX', lex.term);
                    return lex.term
                }

            },

            // sets lexis filter data var
            filterEvent(_filter) {
                this.filter = _filter;
            },

            clearSearch() {
                this.search = "";
            },

            eventAction(event) {


                if (this.lesson_id_list === event) {
                    // this.$store.dispatch("setSelectedEvent", event);
                    this.lesson_id_list = '';
                } else {
                    // this.$store.dispatch("setSelectedEvent", event);
                    this.lesson_id_list = event;
                }
                // if (this.event_id_list === event) {
                //     this.event_id_list = this.event_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.event_id_list.push(event);
                // }


                // if (this.event_id_list.includes(event)) {
                //     this.event_id_list = this.event_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.event_id_list.push(event);
                // }
            },


        },

        created() {

            // console.log('CREATED CALLED');
            // fetchLessons from server once created
            let id = window.localStorage.getItem('instructor_id');
            this.$store.dispatch("fetchLessons", id);


            // fetchClasses(){
            //
            // },


            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch("fetchEvents");
            // this.lexis_id_list = this.$store.getters["getSelectedEvent"];
            // this.$store.dispatch("fetchLexis");
            this.lexis = this.$store.getters["getLexis"];

            // console.log('LEXIS CREATED', this.lexis);

            // console.log('SELECTIONS', this.selections);

            // console.log('GET RETURN OF SELECTIONS',this.$store.getters["getSelections"] );
            // console.log('GET RETURN OF CURRENTLESSON',this.$store.getters["getCurrentLesson"] );

            //
            //
            // console.log('CREATED LESSON CALLED LESSONS DASHBOARD');
            this.selections = this.$store.getters["getSelections"];
            //             console.log('AFTER GET SELECTIONS', this.selections);

        },

        // if (this.class_selection_filter.value === 'all') {
        //     this.class_selection_filter = null;
        //     return
        // }

        // watch: {
        //     class_selection_filter: {
        //         handler: function (val, oldVal) {
        //             if(val && val.value === 'all')
        //             console.log('ALL', val.value);
        //             // this.class_selection_filter = [];
        //         },
        //         // deep: true
        //     }
        // },


        computed: {


            // class options for filtered lessons by class with added 'all'
            class_options_filter() {

                let class_list = [];
                let classes = this.$store.getters['getUserClasses'];
                classes.forEach(element => {

                    let data = {
                        label: element.class_name,
                        value: element.id
                    };

                    class_list.push(data)

                });

                // adding all filter
                let clear = {
                    label: 'All',
                    value: 'all'
                };
                class_list.unshift(clear);

                return class_list
            },


            // class options for creating lesson

            class_options() {

                let class_list = [];
                let classes = this.$store.getters['getUserClasses'];
                classes.forEach(element => {

                    let data = {
                        label: element.class_name,
                        value: element.id
                    };

                    class_list.push(data)

                });

                return class_list
            },


            lesson_list() {

                let lessons = this.$store.getters["getLessons"];
                // console.log(this.search);


                // if all is selected and sets .value to null make class_selection_filter null


                if (this.class_selection_filter.value !== 'all') {


                    // console.log('FILTER VALUE', this.class_selection_filter.value);

                    // create empty array to hold filtered values
                    let filteredList = [];


                    lessons.forEach((item) => {

                        // console.log('ITEM', item.class_link);


                        // if (this.class_selection_filter.value === 'all') {
                        //     this.class_selection_filter = null;
                        //     return
                        // }


                        // if there is no class link id on lesson do nothing
                        if (item.class_link === null) {
                            return
                        }

                        // if lesson item class link id = selected id add to array
                        if (item.class_link === this.class_selection_filter.value) {
                            filteredList.push(item)
                        }


                    });

                    // if there is also a search value and filter value check search against filteredList array
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    if (this.search.length > 0) {

                        // check if items term include search values
                        return filteredList.filter(obj => {
                            return obj.lesson_title.toLowerCase().includes(this.search.toLowerCase());
                        });
                        // return filterSearch;
                    }

                    // return filteredList if no search value
                    return filteredList


                }


                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = lessons.filter(obj => {
                        // return obj.term === this.search
                        return obj.lesson_title.toLowerCase().includes(this.search.toLowerCase());
                    });

                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }

                return lessons


            }
        }
    };
</script>

<style lang="scss">

    .dialog_container {
        width: 70% !important;
    }

    .text-title {
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.0125em;
    }

    .addLesson {
        min-height: 250px;
    }

    .plusIcon {
        font-size: 34px !important;
        color: #cccccc;
    }

    .items-bottom {

        position: absolute;
        bottom: 0;
        right: 0;

    }

      .separator-bottom {

        position: absolute;
        bottom: 60px;


    }


    .grade-class{
        text-align: right;
    }


</style>
