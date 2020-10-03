<template>

    <q-dialog v-model="icon">
                        <q-card class="lex-card">

                            <q-card-section class="row items-center q-pb-none">
                                <div class="text-h6">{{dialog.term}}</div>
                                <q-space/>
                                <q-btn icon="close" flat round dense v-close-popup/>
                            </q-card-section>


                            <q-separator/>
                            <div class="row">
                                <q-card-section class="col-2 ">
                                    <div class="subtitle">Part of Speech:</div>
                                    <div>{{dialog.part_of_speech}}</div>
                                    <div class="subtitle dialog-top">Derivations:</div>
                                    <div v-for="derivation in dialog.derivations" :key="derivation.id">
                                        <div>{{derivation.value}}</div>
                                    </div>

                                    <div class="subtitle dialog-top">Linked Lexis:</div>
                                    <div v-for="lex2 in dialog.lexis_link" :key="lex2.id">
                                        <div>{{lex2.value}}</div>
                                    </div>


                                    <q-separator vertical/>

                                </q-card-section>
                                <q-card-section class="col-5 ">
                                    <div class="subtitle">Etymology:</div>
                                    <div v-html="dialog.etymology"></div>

                                    <div class="subtitle dialog-top">Quote:</div>

                                    <div>"{{dialog.quotation}}"</div>
                                    <div class="dialog-top">{{dialog.quote_source}}</div>
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
        // props: ['dialog', 'iconState'],
        name: "LexisDialog.vue",

        data(){
            return{
               icon: false,
                dialog: {}
            }
        },

        methods:{
            popupContent(lex) {
                this.icon = true;
                this.dialog = lex
            },
        },



    }
</script>

<style scoped>

</style>