<template>

    <q-dialog v-model="extModel">
        <q-card class="lex-card">

            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.action}}</div>
                <q-space/>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">

                <q-card-section class="col-2">
                    <div class="subtitle">Command Type:</div>
                    <div style="text-transform:capitalize">{{commandName}}</div>

                    <div v-if="lexLength">
                        <div class="subtitle dialog-top">Related Lexis:</div>
                        <div v-for="lex in dialog.extension_lexis_link" :key="lex.id">
                            <q-chip dense :label="lex.term"/>
                        </div>
                    </div>

                </q-card-section>

                <q-card-section class="col-10">
                    <div class="subtitle">Explanation:</div>
                    <div v-html="dialog.explanation"></div>

                    <div v-if="dialog.video_link">
                        <div class="subtitle dialog-top">Play Video
                            <q-icon name="play_circle_outline"/>
                        </div>

                        <q-video
                                :ratio="16/9"
                                :src="dialog.video_link"
                        />
                    </div>


                </q-card-section>


            </div>
        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        // props: ['dialog', 'iconState'],
        name: "EventDialog.vue",

        data() {
            return {
                extModel: false,
                dialog: {}
            }
        },

        computed: {
            commandName() {
                if (this.dialog.assignment_command_types) {
                    return this.dialog.assignment_command_types.command_name
                } else {
                    return ''
                }
            },

            lexLength(){

                 if(this.dialog.extension_lexis_link && this.dialog.extension_lexis_link.length > 0){
                    return true
                }else{
                    return false
                }

            }
        },

        methods: {
            popupContent(event) {
                this.extModel = true;
                this.dialog = event
            },


        },


    }
</script>

<style scoped>

    .quote {
        font-size: 1rem;
        line-height: 1.2rem;
        font-family: "Times New Roman", serif;
    }

    .author {
        text-align: right;
        font-size: .8rem;
        padding-top: 10px;
    }

    .author_source {
        padding-top: 10px;
        font-size: 10px;
    }

</style>