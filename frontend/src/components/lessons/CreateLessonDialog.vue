<template>


    <q-dialog v-model="create_new_lesson" persistent>
                    <q-card style="min-width: 350px">
                        <q-card-section>


                            <div v-if="!edit_lesson" class="text-h6">Create a new lesson</div>
                            <div v-if="edit_lesson" class="text-h6">Update title, class & description </div>

                        </q-card-section>

                        <!-- ADD TITLE WITH VALIDATION -->
                        <q-card-section class="q-pt-none">
                            <q-input
                                    dense
                                    ref="class_title"
                                    v-model="new_lesson_title"
                                    label="Lesson Title"
                                    @input="lessonTitleEvent"
                                    :rules="[ val => !!val || '* Required',
                                              val => val.length >= 3 || 'Please use minimum 3 characters']"
                                    lazy-rules/>


                        </q-card-section>

                          <!-- SELECT CLASS -->
                        <q-card-section class="q-pt-none">
                            <q-select  ref="class_name" v-model="class_selection"
                                      @input="classSelectionEvent"
                                       dense
                                      :options="class_options" label="Select Class"/>



                        </q-card-section>

                        <!-- DESCRIPTION -->
                        <q-card-section class="q-pt-none">
                            <q-input ref="class_description"
                                        autogrow
                                     dense
                                     @input="lessonDescriptionEvent"
                                     label="Lesson Description"
                                     v-model="lesson_description"/>
                        </q-card-section>
                        <!-- CONDITIONAL BUTTONS-->
                        <q-card-actions align="right" class="text-primary">
                            <q-btn flat label="Cancel" v-close-popup/>

                            <!-- SWITCH BETWEEN UPDATE AND CREATE BTNS-->
                <q-btn :disable="!testBtn" v-if="!edit_lesson" @click="createNewLesson" flat label="Create New Lesson"
                       v-close-popup/>
                <q-btn :disable="!testEditBtn" v-if="edit_lesson" @click="updateLesson" flat label="Continue"
                       v-close-popup/>


<!--                            <q-btn v-if="new_lesson_title.length < 3" disabled flat label="Create New Lesson"-->
<!--                                   v-close-popup/>-->
<!--                            <q-btn v-if="new_lesson_title.length >= 3" @click="createNewLesson" flat-->
<!--                                   label="Create New Lesson" v-close-popup/>-->
                        </q-card-actions>

                    </q-card>
                </q-dialog>


</template>

<script>

        import DOMPurify from 'dompurify';


    export default {
        props: ['class_options', 'createNewLessonHandler'],
        name: "CreateLessonDialog.vue",
        data(){
            return{
                create_new_lesson: false,
                class_selection: null,
                new_lesson_title: '',
                lesson_description: '',
                edit_lesson: false,
                edit_lesson_data: ''

            }
        },

        computed: {
            testBtn() {
                if (this.new_lesson_title && this.new_lesson_title.length >= 3 && this.edit_lesson === false) {
                    return true
                } else {
                    return false
                }
            },

            testEditBtn() {
                if (this.new_lesson_title && this.new_lesson_title.length >= 3 && this.edit_lesson === true) {
                    return true
                } else {
                    return false
                }
            }

        },

        methods:{


            // this edit from card editIcon
            editLesson(lesson) {

                // let data = {
                //     "id": this.edit_id,
                //     "class_name": this.class_name,
                //     "grade_level": this.grade_level,
                //     "class_description": this.class_description
                // };
                //
                // // POST TO DB
                // this.$store.dispatch('updateClass', data);


                console.log('LESSON', lesson);
                this.$store.dispatch('editLesson', lesson);
                this.$router.push({name: 'Lesson'});

            },


            //   class_options() {
            //
            //     let class_list = [];
            //     let classes = this.$store.getters['getUserClasses'];
            //     classes.forEach(element => {
            //         let data = {
            //             label: element.class_name,
            //             value: element.id
            //         };
            //         class_list.push(data)
            //
            //     });
            //
            //     return class_list
            // },

            // this edit update icon card
            updateLesson(){

            // checks if class, description or title change and loads lesson for edit




                if (this.lesson_description){
                    var cleanDescription = DOMPurify.sanitize(this.lesson_description);

                   this.edit_lesson_data.lesson_description = cleanDescription;
                }

                if(this.class_selection.value){
                    this.edit_lesson_data.class_link = this.class_selection.value;
                }

                if(this.new_lesson_title){

                    var cleanTitle = DOMPurify.sanitize(this.new_lesson_title);
                    this.edit_lesson_data.lesson_title = cleanTitle;
                }

                this.$store.dispatch('editLesson', this.edit_lesson_data);
                this.$router.push({name: 'Lesson'});

            },



            createNewLesson() {

                var cleanTitle = DOMPurify.sanitize(this.new_lesson_title);
                var cleanDescription = DOMPurify.sanitize(this.lesson_description);



                let lessonData = {
                    title: cleanTitle,
                    description: cleanDescription,
                    class_id: this.class_selection.value
                };

                this.$store.dispatch("postLessonTitle", lessonData);

                // FORWARD TO EVENTS SECTION
                this.$router.push({name: 'Events'});

            },
            // createNewLesson(){
            //     this.createNewLessonHandler();
            // },

            lessonTitleEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('lessonTitleEvent', this.new_lesson_title);
            },

            classSelectionEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('classSelectionEvent', this.class_selection);
            },

            lessonDescriptionEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('lessonDescriptionEvent', this.lesson_description);
            },

            popupContent() {
                this.create_new_lesson = true;
            },

            popupEdit(lessonData) {
                this.create_new_lesson = true;
                this.edit_lesson = true;
                this.edit_lesson_data = lessonData;

                console.log('LESSON DATA', lessonData);
                // SET POPUP DATA

                 // let class_list = [];
                let classes = this.$store.getters['getUserClasses'];

                // find class of lesson and add it to selected class
                let selectedClass = classes.find(element => {
                    return element.id === lessonData.class_link;
                });

                // filters out deleted classes if deleted selected class doesn't exist so sets class selection ''
                if(selectedClass) {
                    this.class_selection = selectedClass.class_name;
                    }else{
                    this.class_selection = ''
                }

                 // console.log('selectedClass', selectedClass);
                // return class_list

                this.new_lesson_title = lessonData.lesson_title;
                this.lesson_description = lessonData.lesson_description;


            },


        }
    }
</script>

<style scoped>

</style>