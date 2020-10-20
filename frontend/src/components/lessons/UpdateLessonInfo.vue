<template>


    <q-dialog v-model="create_new_lesson" persistent>
        <q-card style="min-width: 350px">
            <q-card-section>

                <div class="text-h6">Update title, class & description</div>

            </q-card-section>

            <!-- ADD TITLE WITH VALIDATION -->
            <q-card-section class="q-pt-none">
                <q-input
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
                <q-select ref="class_name" v-model="class_selection"
                          @input="classSelectionEvent"
                          :options="class_options" label="Select Class"/>
            </q-card-section>

            <!-- DESCRIPTION -->
            <q-card-section class="q-pt-none">
                <q-input ref="class_description"
                         dense type="textarea"
                         @input="lessonDescriptionEvent"
                         label="lesson Description"
                         v-model="lesson_description"/>
            </q-card-section>
            <!-- CONDITIONAL BUTTONS-->
            <q-card-actions align="right" class="text-primary">
                <q-btn flat label="Cancel" v-close-popup/>

                <!-- SWITCH BETWEEN UPDATE AND CREATE BTNS-->

                <q-btn :disable="!testEditBtn" @click="updateLesson" flat label="Continue"
                       v-close-popup/>


            </q-card-actions>

        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        props: ['class_options'],
        name: "UpdateLessonInfo.vue",
        data() {
            return {
                create_new_lesson: false,
                class_selection: null,
                new_lesson_title: '',
                lesson_description: '',
                edit_lesson_data: ''

            }
        },

        computed: {
            // testBtn() {
            //     if (this.new_lesson_title && this.new_lesson_title.length >= 3 && this.edit_lesson === false) {
            //         return true
            //     } else {
            //         return false
            //     }
            // },

            testEditBtn() {
                if (this.new_lesson_title && this.new_lesson_title.length >= 3 ) {
                    return true
                } else {
                    return false
                }
            }

        },

        methods: {

            popupEdit(lessonData) {
                this.create_new_lesson = true;
                this.edit_lesson_data = this.$store.getters['getLesson'];

                console.log('LESSON DATA BOOYA', this.edit_lesson_data);
                // SET POPUP DATA

                // let class_list = [];
                let classes = this.$store.getters['getUserClasses'];
                let selectedClass = classes.find(element => {
                    // console.log('ELEMENTS', element);
                    return element.id === this.edit_lesson_data.class_link;


                });

                console.log('selectedClass', selectedClass);


                // return class_list


                this.new_lesson_title = this.edit_lesson_data.lesson_title;
                this.class_selection = selectedClass.class_name;
                this.lesson_description = this.edit_lesson_data.lesson_description;

                // this.edit_id = classData.id;
                // this.edit_class = true;

            },

            // this edit update icon card
            updateLesson() {

                // checks if class, description or title change and loads lesson for edit
                if (this.lesson_description) {
                    this.edit_lesson_data.lesson_description = this.lesson_description;
                }

                if (this.class_selection.value) {
                    this.edit_lesson_data.class_link = this.class_selection.value;
                }

                if (this.new_lesson_title) {
                    this.edit_lesson_data.lesson_title = this.new_lesson_title;
                }

                this.$store.dispatch('editLessonData', this.edit_lesson_data);
                // this.$router.push({name: 'Lesson'});

            },

            // EVENT INPUT METHODS
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
            // },
            // createNewLesson(){
            //     this.createNewLessonHandler();
            // },



            //
            // popupContent() {
            //     this.create_new_lesson = true;
            // },


        }
    }
</script>

<style scoped>

</style>