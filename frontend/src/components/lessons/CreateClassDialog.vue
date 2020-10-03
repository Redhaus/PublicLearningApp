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
                                     @input="classNameEvent"
                                     autofocus
                                     :rules="[ val => !!val || '* Required',
                                               val => val.length >= 3 || 'Please use minimum 3 characters']"
                                     lazy-rules
                            />
                        </q-card-section>

                        <q-card-section class="q-pt-none">
                            <q-select  v-model="grade_level"
                                       @input="gradeLevelEvent"
                                       :options="grade_options" label="Select Grade Level"/>
                        </q-card-section>

                        <q-card-section class="q-pt-none">
                            <q-input dense type="textarea"
                                     @input="classDescriptionEvent"
                                     label="Class Description" v-model="class_description"/>
                        </q-card-section>

                        <q-card-actions align="right" class="text-primary">
                            <q-btn flat label="Cancel" v-close-popup/>
                            <q-btn v-if="class_name.length < 3" disable flat label="Create Class" v-close-popup/>
                            <q-btn v-if="class_name.length >= 3" @click="createClass" flat label="Create Class"
                                   v-close-popup/>

                        </q-card-actions>
                    </q-card>
                </q-dialog>

</template>

<script>
    export default {
        // createClassHandler is function passed
        // options are grades array being passed
        props: ['createClassHandler', 'grade_options'],
        name: "CreateClassDialog.vue",
        data(){
            return{
               create_class_dialog: false,
                class_name: '',
                grade_level: null,
                class_description: ''
            }
        },

        methods:{
            createClass(){
                this.createClassHandler();
            },

            classNameEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('classNameEvent', this.class_name);
            },

            gradeLevelEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('gradeLevelEvent', this.grade_level);
            },

            classDescriptionEvent() {
                // pass emit event to parent component and pass data changed
                this.$emit('classDescriptionEvent', this.class_description);
            },

            popupContent() {
                this.create_class_dialog = true;
            },

        }

    }
</script>

<style scoped>

</style>