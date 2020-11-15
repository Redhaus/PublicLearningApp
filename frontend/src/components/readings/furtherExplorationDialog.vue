<template>

    <q-dialog v-model="explorationModel">
        <q-card class="lex-card">


            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.title_minor}}</div>
                <q-space/>

<!--                check if selected item and display add or remove-->
                <q-btn :label="selected_list.includes(dialog.id) ? 'remove' : 'add' "  @click="eventAction(dialog.id)" flat  dense v-close-popup/>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">
                <q-card-section class="col-3">

                    <div class="subtitle">Resource:</div>
                    <q-item-label>
                        <a :href="dialog.resource_link">
                            <q-skeleton animation="none" height="250px" square/>
                        </a>
                    </q-item-label>


                    <div v-if="dialog.reading_category" class="subtitle dialog-top">Type:</div>
                    <div>{{readingCat}}</div>

                    <q-separator vertical/>
                </q-card-section>

                <q-card-section class="col-9 ">
                    <div class="subtitle">Excerpt:</div>
                    <div v-html="dialog.excerpt"></div>

                    <div v-if="dialog.author_first_name || dialog.author_last_name" class="subtitle dialog-top">
                        Author:
                    </div>
                    <div>{{dialog.author_first_name}} {{dialog.author_last_name}}</div>

                    <div v-if="dialog.translator_name" class="subtitle dialog-top">Translator:</div>
                    <div>{{dialog.translator_name}}</div>

                    <div v-if="dialog.author_dob" class="subtitle dialog-top">Author DOB:</div>
                    <div>{{dialog.author_dob}}</div>

                    <div v-if="dialog.source" class="subtitle dialog-top">Source:</div>
                    <div v-html="dialog.source"></div>

                    <div class="subtitle dialog-top">Keywords & Concepts:</div>
                    <div class="keyPadding">
                        <q-chip v-for="concept in dialog.keywords" dense
                                color="black" text-color="white"
                                :key="concept.id"
                                  outline
                                clickable
                                @click="conceptSelect(concept.value)"
                                :label="concept.value"/>
                    </div>


                </q-card-section>

                <!--                                <q-card-section class="col-3 ">-->
                <!--                                    <div class="subtitle">Applications:</div>-->
                <!--                                    <ul class="indent">-->
                <!--                                        <li v-for="application in dialog.application" :key="application.id">-->
                <!--                                            {{application.value}}-->
                <!--                                        </li>-->
                <!--                                    </ul>-->
                <!--                                    <q-separator vertical/>-->

                <!--                                    <div class="subtitle dialog-top">Exploration:</div>-->
                <!--                                    <ol class="indent">-->
                <!--                                        <li v-for="exploration in dialog.exploration" :key="exploration.id">-->
                <!--                                            {{exploration.value}}-->
                <!--                                        </li>-->
                <!--                                    </ol>-->

                <!--                                </q-card-section>-->

            </div>

        </q-card>
    </q-dialog>


</template>

<script>
    export default {
        props: ['conceptSelectHandler', 'eventActionHandler', 'selected_list'],
        name: "ExplorationsDialog.vue",

        data() {
            return {
                explorationModel: false,
                dialog: {}
            }
        },

        methods: {

            conceptSelect(id){
                // this.explorationModel = false;
                this.conceptSelectHandler(id)
            },

            popupEx(exploration) {
                this.explorationModel = true;
                this.dialog = exploration
            },

              eventAction(id){
                console.log('ID', id);
                // this.selectedState = !this.selectedState;
                this.eventActionHandler(id)
            }

        },

        computed: {
            readingCat() {
                if (this.dialog.reading_category) {
                    return this.dialog.reading_category.category_name
                } else {
                    return ''
                }

            }
        }


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

    .keyPadding{
        margin-left: -5px;
    }

    body.desktop .q-chip--clickable:focus {
    background-color: black !important;
    color: white !important;
}

</style>