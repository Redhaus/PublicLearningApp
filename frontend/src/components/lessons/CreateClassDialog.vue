<template>

    <q-dialog v-model="create_class_dialog" persistent>



        <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6">Create Class</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
                <q-input dense
                         label="Class Name"
                         v-model="class_name"
                         autofocus
                         :rules="[ val => !!val || '* Required',
                                               val => val.length >= 3 || 'Please use minimum 3 characters']"
                         lazy-rules
                />
            </q-card-section>

            <q-card-section class="q-pt-none">
                <q-select v-model="grade_level"
                          :options="grade_options" label="Select Grade Level"/>
            </q-card-section>

            <q-card-section class="q-pt-none">
                <q-input dense type="textarea"
                         label="Class Description" v-model="class_description"/>
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
                <q-btn @click="cancelClass" flat label="Cancel" v-close-popup/>

                <!-- SWITCH BETWEEN UPDATE AND CREATE BTNS-->
                <q-btn :disable="!testBtn" v-if="!edit_class" @click="createClass" flat label="Create Class"
                       v-close-popup/>
                <q-btn :disable="!testEditBtn" v-if="edit_class" @click="updateClass" flat label="Update Class"
                       v-close-popup/>


                <!--                            :disabled="validated == 1"-->
            </q-card-actions>
        </q-card>
    </q-dialog>

</template>

<script>

    import DOMPurify from 'dompurify';

    export default {
        // createClassHandler is function passed
        // options are grades array being passed
        // props: ['createClassHandler', 'updateClassHandler', 'grade_options'],
        // props: ['grade_options'],

        name: "CreateClassDialog.vue",
        data() {
            return {
                create_class_dialog: false,
                class_name: '',
                grade_level: null,
                class_description: '',
                edit_class: false,
                edit_id: '',

                grade_options: [
                    6, 7, 8, 9, 10, 11, 12
                ],
            }
        },

        computed: {
            testBtn() {
                if (this.class_name && this.class_name.length >= 3 && this.edit_class === false) {
                    return true
                } else {
                    return false
                }
            },

            testEditBtn() {
                if (this.class_name && this.class_name.length >= 3 && this.edit_class === true) {
                    return true
                } else {
                    return false
                }
            }

        },

        methods: {

            clearData(){

                 setTimeout(() => {
                    this.class_name = '';
                    this.grade_level = null;
                    this.class_description = '';
                    this.edit_class = false;

                }, 300);

            },

            // CANCEL CLASS CREATION AND UDPATE
            cancelClass() {
                this.clearData();
            },

            createClass() {

                  // Run npm install -g npm

                var cleanName = DOMPurify.sanitize(this.class_name);
                var cleanDescription = DOMPurify.sanitize(this.class_description);


                let data = {
                    "class_name": cleanName,
                    "grade_level": this.grade_level,
                    "class_description": cleanDescription
                };

                // POST TO DB
                this.$store.dispatch('postNewClass', data);

                // CLEAR CLASS LIST
                this.clearData();

            },



            updateClass() {

                var cleanName = DOMPurify.sanitize(this.class_name);
                var cleanDescription = DOMPurify.sanitize(this.class_description);

                let data = {
                    "id": this.edit_id,
                    "class_name": cleanName,
                    "grade_level": this.grade_level,
                    "class_description": cleanDescription
                };

                // POST TO DB
                this.$store.dispatch('updateClass', data);

                // CLEAR CLASS LIST
                this.clearData();

            },


            popupAdd() {
                this.create_class_dialog = true;
            },

            popupEdit(classData) {
                // SET POPUP DATA
                this.class_name = classData.class_name;
                this.grade_level = classData.grade_level;
                this.class_description = classData.class_description;
                this.edit_id = classData.id;
                this.edit_class = true;

                this.create_class_dialog = true;
            },

        }

    }
</script>

<style scoped>

</style>