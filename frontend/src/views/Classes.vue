<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">

       <!-- TOP BANNER-->
        <div class="col-12">
                     <SearchHeader name="Classes" @searchTerm="search = $event"/>

<!--            <q-banner elevated rounded inline-actions class="page-bar shadow-3">-->
<!--                <div class="row">-->

<!--                    <div class="col-8 title" tabindex="0">-->
<!--                        <div>Classes</div>-->
<!--                    </div>-->

<!--                    <div class="col-4" tabindex="0">-->

<!--                    </div>-->
<!--                </div>-->
<!--            </q-banner>-->
        </div>


        <!-- CARDS-->
        <div style="width: 100%">

                <masonry :cols="4" :gutter="20">

                    <!-- CREATE CLASS BUTTON-->
                    <div class="bottom-padding">
                        <q-card
                                class="cardHandle addLesson row justify-center items-center"
                                bordered
                                @click="newClassDialogPopup"

                                  v-tooltip.center="{
                                  content: 'Create New Class',
                                  classes: ['info'],
                                  targetClasses: ['it-has-a-tooltip'],
                                  offset: 5,
                                  delay: {
                                    show: 500,
                                    hide: 300,
                                  },
                                }"


                        >
                            <q-card-section>
                                <q-icon class="plusIcon" name="fas fa-plus"></q-icon>
                            </q-card-section>
                        </q-card>
<!--                        <q-tooltip anchor="top middle" self="center middle">Create Class</q-tooltip>-->
                    </div>


<!--                    <div v-if="class_list.length > 0">-->


                   <!-- CLASS CARDS-->
                    <div v-for="classed in class_list" :key="classed.id" class="bottom-padding">


                        <q-card
                            class="cardHandle addLesson"
                            bordered>

                            <q-item>
                                <q-item-section avatar>
                                    <q-avatar>
                                        <q-icon color="gray" name="o_groups" size="40px"/>
                                    </q-avatar>
                                </q-item-section>
<!--                                <q-item-section class="grade-class">-->
<!--                                    <q-item-label caption>Grade {{class_card_grade(lesson.class_link)}}</q-item-label>-->
<!--                                </q-item-section>-->
                            </q-item>

                            <q-item>
                                <q-item-section>
                                    <q-item-label caption>Class Name</q-item-label>
                                    <q-item-label>{{classed.class_name}}</q-item-label>
                                </q-item-section>
                            </q-item>

                            <q-item>

                                <q-item-section>
                                    <q-item-label caption>Class Grade</q-item-label>
                                    <q-item-label>{{classed.grade_level}}</q-item-label>
                                </q-item-section>
                            </q-item>

                            <q-separator class="separator-bottom"  />

                            <q-card-actions class="items-bottom" align="right">

                                <q-btn @click="deleteConfirmation(classed)" dense flat round color="gray" icon="o_delete"/>
                                <q-btn @click="editClass(classed)" dense flat round color="gray" icon="o_edit"/>


                            </q-card-actions>
                        </q-card>






<!--                        <q-card-->
<!--                                class="cardHandle addLesson"-->
<!--                                bordered>-->
<!--                            <q-card-section>-->
<!--                                <div>Class Name: {{classed.class_name}}</div>-->
<!--                                <div>Class Grade: {{classed.grade_level}}</div>-->
<!--                            </q-card-section>-->

<!--                            <q-card-actions>-->
<!--                                <q-btn @click="deleteConfirmation(classed)" color="primary" label="Delete"/>-->
<!--                                <q-btn @click="editClass(classed)" color="primary" label="Edit"/>-->
<!--                            </q-card-actions>-->

<!--                        </q-card>-->
                    </div>

<!--                     </div>-->

<!--            <div class="selectEventNotification" v-else>Create A Class</div>-->

                </masonry>

                <!-- CREATE NEW CLASS DIALOG -->
                <CreateClassDialog ref="newClassDialog"/>



        </div>
    </div>
</template>

<script>
    import SearchHeader from "../components/SearchHeader";
    import CreateClassDialog from "../components/lessons/CreateClassDialog";


    export default {

        components: {
            CreateClassDialog,
            SearchHeader
        },
        data() {
            return {
                create_class_dialog: false,
                class_selection: null,
                search: ''
            };
        },

        methods: {

            editClass(classData){
                this.$refs.newClassDialog.popupEdit(classData);
            },

            // calls popup for create class
            newClassDialogPopup() {
                this.$refs.newClassDialog.popupAdd();
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
        },

        created() {

        },
        computed: {
            class_list() {
                let classes =  this.$store.getters['getUserClasses'];

                if (this.search.length > 0) {
                    // return filter array looking for matches
                    var result = classes.filter(obj => {
                        // return matching results for classname and search term
                        return obj.class_name.toLowerCase().includes(this.search.toLowerCase());
                    });
                    return result;
                }

                return classes

            }
        }
    };
</script>

<style lang="scss">
</style>

