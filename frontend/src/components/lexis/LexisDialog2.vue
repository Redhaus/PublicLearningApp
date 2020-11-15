<template>


    <q-dialog v-model="icon">
        <q-card class="lex-card">

            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.term}}</div>
                <q-space/>

                <q-btn :label="selected_list.includes(dialog.id) ? 'remove' : 'add' " @click="eventAction(dialog.id)"
                       flat dense v-close-popup/>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">
                <q-card-section class="col-2 ">
                    <div class="subtitle">Part of Speech:</div>
                    <div>{{dialog.part_of_speech}}</div>

                    <div v-if="dialog.derivations && dialog.derivations.length > 0">
                        <div class="subtitle dialog-top">Derivations:</div>
                        <div v-for="derivation in dialog.derivations" :key="derivation.id">
                            <div>{{derivation.value}}</div>
                        </div>
                    </div>

                    <div v-if="dialog.lexis_link && dialog.lexis_link.length > 0">
                        <div class="subtitle dialog-top">Linked Lexis:</div>
                        <div v-for="lex2 in dialog.lexis_link" :key="lex2.id">
                            <div>{{lex2.term_link.term}}</div>
                            <!--                                                                                <div @click="lexisLink(lex2.term_link.id)">{{lex2.term_link.term}}</div>-->
                        </div>
                    </div>


                    <q-separator vertical/>

                </q-card-section>
                <q-card-section class="col-5 ">
                    <div class="subtitle">Etymology:</div>
                    <div v-html="dialog.etymology"></div>

                    <div class="subtitle dialog-top">Quote:</div>

                    <div>"{{dialog.quotation}}"</div>
                    <div class="dialog-top" :v-html="dialog.quote_source"></div>
                    <div>{{dialog.quotation_author}}</div>


                </q-card-section>

                <q-card-section class="col-5 ">
                    <div class="subtitle">Applications:</div>
                    <ul class="indent">
                        <li v-for="application in dialog.application" :key="application.id">
                            {{application.value}}
                        </li>
                    </ul>
                    <q-separator vertical/>

                    <div class="subtitle dialog-top">Exploration:</div>
                    <ol class="indent">
                        <li v-for="exploration in dialog.exploration" :key="exploration.id">
                            {{exploration.value}}
                        </li>
                    </ol>

                </q-card-section>

            </div>
        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        props: ['eventActionHandler', 'selected_list'],
        name: "LexisDialog.vue",

        data() {
            return {
                icon: false,
                dialog: {}
            }
        },

        methods: {
            popupContent(lex) {
                this.icon = true;
                this.dialog = lex
            },

            eventAction(id) {
                console.log('ID', id);
                // this.selectedState = !this.selectedState;
                this.eventActionHandler(id)
            },


            // this handles lexis link id from dialog
            lexisLink(linkID) {
                console.log('LINKID', linkID);
            }


        },


    }
</script>

<style scoped>

</style>