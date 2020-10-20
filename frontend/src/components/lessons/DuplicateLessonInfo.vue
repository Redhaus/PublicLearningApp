<template>


    <q-dialog v-model="create_new_lesson" persistent>
        <q-card style="min-width: 350px">
            <q-card-section>
                <!--<div v-if="!edit_lesson" class="text-h6">Duplicate lesson</div>-->
                <div class="text-h6">Duplicate lesson</div>
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
                <q-btn :disable="!testEditBtn" @click="duplicateLesson" flat label="Continue" v-close-popup/>
            </q-card-actions>
        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        props: ['class_options', 'createNewLessonHandler'],
        name: "CreateLessonDialog.vue",
        data() {
            return {
                create_new_lesson: false,
                class_selection: null,
                new_lesson_title: '',
                lesson_description: '',
                edit_lesson: false,
                edit_lesson_data: ''
            }
        },

        computed: {
            testEditBtn() {
                if (this.new_lesson_title && this.new_lesson_title.length >= 3) {
                    return true
                } else {
                    return false
                }
            }
        },

        methods: {

            // this edit from card editIcon
            // editLesson(lesson) {
            //     console.log('LESSON LESSON LESSON LESSON LESSON LESSON');
            //
            //     console.log('LESSON', lesson);
            //     this.$store.dispatch('editLesson', lesson);
            //     this.$router.push({name: 'Lesson'});
            // },

            // this edit update icon card
            duplicateLesson() {

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

                this.$store.dispatch('duplicateLesson', this.edit_lesson_data);
                this.$router.push({name: 'Lesson'});

            },


            createNewLesson() {

                let lessonData = {
                    title: this.new_lesson_title,
                    description: this.lesson_description,
                    class_id: this.class_selection.value
                };

                this.$store.dispatch("postLessonTitle", lessonData);

                // FORWARD TO EVENTS SECTION
                this.$router.push({name: 'Events'});

            },

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
                let selectedClass = classes.find(element => {

                    console.log('ELEMENTS', element);

                    return element.id === lessonData.class_link;

                });

                console.log('selectedClass', selectedClass);

                this.new_lesson_title = lessonData.lesson_title + " NEW";
                this.class_selection = selectedClass.class_name;
                this.lesson_description = lessonData.lesson_description;

            },

        }
    }
</script>

<style scoped>

</style>