<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">

       <!-- TOP BANNER-->
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">

                    <div class="col-8 title" tabindex="0">
                        <div>Classes</div>
                    </div>

                    <div class="col-4" tabindex="0">

                    </div>
                </div>
            </q-banner>
        </div>


        <!-- CARDS-->
        <div style="width: 100%">
            <div v-if="class_list.length > 0">

                <masonry :cols="4" :gutter="20">

                    <!-- CREATE CLASS BUTTON-->
                    <div class="bottom-padding">
                        <q-card
                                class="cardHandle addLesson row justify-center items-center"
                                bordered
                                @click="newClassDialogPopup">
                            <q-card-section>
                                <q-icon class="plusIcon" name="fas fa-plus"></q-icon>
                            </q-card-section>
                        </q-card>
                        <q-tooltip anchor="top middle" self="center middle">Create Class</q-tooltip>
                    </div>

                   <!-- CLASS CARDS-->
                    <div v-for="classed in class_list" :key="classed.id" class="bottom-padding">
                        <q-card
                                class="cardHandle addLesson"
                                bordered>
                            <q-card-section>
                                <div>Class Name: {{classed.class_name}}</div>
                                <div>Class Grade: {{classed.grade_level}}</div>
                            </q-card-section>

                            <q-card-actions>
                                <q-btn @click="deleteConfirmation(classed)" color="primary" label="Delete"/>
                            </q-card-actions>

                        </q-card>
                    </div>

                </masonry>

                <!-- CREATE NEW CLASS DIALOG -->
                <CreateClassDialog ref="newClassDialog"
                                   :grade_options=grade_options
                                   @classNameEvent="class_name = $event"
                                   @classDescriptionEvent="class_description = $event"
                                   @gradeLevelEvent="grade_level = $event"
                                   :createClassHandler="createClass"/>

            </div>

            <div v-else>No Lesson Available</div>
        </div>
    </div>
</template>

<script>
    import CreateClassDialog from "../components/lessons/CreateClassDialog";


    export default {

        components: {
            CreateClassDialog
        },
        data() {
            return {
                create_class_dialog: false,
                class_name: '',
                grade_level: null,
                class_description: '',
                grade_options: [
                    6, 7, 8, 9, 10, 11, 12
                ],
                class_selection: null
            };
        },

        methods: {

            // calls popup for create class
            newClassDialogPopup() {
                this.$refs.newClassDialog.popupContent();
            },

            // CONFIRMATION DELETE DIALOG
            deleteConfirmation(classed) {

                this.$q.dialog({
                    title: 'Confirm Delete',
                    message: classed.class_name,
                    cancel: true,
                    persistent: true,
                    ok: {
                        label: 'Delete',
                        flat: true,
                        textColor: 'red'
                    }
                }).onOk(() => {
                    console.log('CLASSED', classed.id);
                    this.deleteClass(classed.id)
                }).onCancel(() => {
                })
            },

            deleteClass(id) {
                this.$store.dispatch('deleteUserClass', id)
            },

            createClass() {

                let data = {
                    "class_name": this.class_name,
                    "grade_level": this.grade_level,
                    "class_description": this.class_description
                };

                // POST TO DB
                this.$store.dispatch('postNewClass', data);

                // CLEAR CLASS LIST
                this.class_name = '';
                this.grade_level = null;
                this.class_description = '';

            },

        },

        created() {

        },

        computed: {
            class_list() {
                return this.$store.getters['getUserClasses'];
            }
        }
    };
</script>

<style lang="scss">
</style>

