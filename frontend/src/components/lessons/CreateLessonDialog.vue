<template>


    <q-dialog v-model="create_new_lesson" persistent>
                    <q-card style="min-width: 350px">
                        <q-card-section>
                            <div class="text-h6">Create a new lesson</div>
                        </q-card-section>
                        <!-- SELECT CLASS -->
                        <q-card-section class="q-pt-none">
                            <q-select ref="class_name" v-model="class_selection"
                                      @input="classSelectionEvent"
                                      :options="class_options" label="Select Class"/>
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
                            <q-btn v-if="new_lesson_title.length < 3" disabled flat label="Create New Lesson"
                                   v-close-popup/>
                            <q-btn v-if="new_lesson_title.length >= 3" @click="createNewLesson" flat
                                   label="Create New Lesson" v-close-popup/>
                        </q-card-actions>

                    </q-card>
                </q-dialog>


</template>

<script>
    export default {
        props: ['class_options', 'createNewLessonHandler'],
        name: "CreateLessonDialog.vue",
        data(){
            return{
                create_new_lesson: false,
                class_selection: null,
                new_lesson_title: '',
                lesson_description: ''
            }
        },
        methods:{

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

        }
    }
</script>

<style scoped>

</style>