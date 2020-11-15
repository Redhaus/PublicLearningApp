<template>

    <q-dialog v-model="primaryReadingModel">
        <q-card class="lex-card">


            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.title_major}}</div>
                <q-space/>
                <q-btn label="add"  @click="eventAction(dialog.id)" flat round dense v-close-popup/>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">
                <q-card-section class="col-3">

                    <div class="subtitle dialog-top">Book Cover:</div>

                    <q-item-label v-if="dialog.book_image">
                        <q-img
                                :src="dialog.book_image"
                                spinner-color="white"
                                style="height: 250px;"
                        />
                    </q-item-label>

                    <q-item-label v-if="!dialog.book_image">
                        <a :href="dialog.purchase_link">
                            <q-skeleton animation="none" height="250px" square/>
                        </a>
                    </q-item-label>

                    <div v-if="dialog.level_ability" class="subtitle dialog-top">Reading Level:</div>
                    <div>{{dialog.level_ability}}</div>
                    <div v-if="dialog.page_count" class="subtitle dialog-top">Page Count:</div>
                    <div>{{dialog.page_count}}</div>
                    <div v-if="readingCat" class="subtitle dialog-top">Type:</div>
                    <div>{{readingCat}}</div>

                    <q-separator vertical/>
                </q-card-section>

                <q-card-section class="col-9 ">
                    <div class="subtitle">Synopsis:</div>
                    <div v-html="dialog.synopsis"></div>

                    <div class="subtitle dialog-top">Author:</div>
                    <div>{{dialog.author_first_name}} {{dialog.author_last_name}}</div>

                    <div class="subtitle dialog-top">Author DOB:</div>
                    <div>{{dialog.author_dob}}</div>

                    <div v-if="dialog.translator_name" class="subtitle dialog-top">Translator:</div>
                    <div>{{dialog.translator_name}}</div>

                    <div class="subtitle dialog-top">Source:</div>
                    <div>{{dialog.source}}</div>

                    <div class="subtitle dialog-top">Keywords & Concepts:</div>
                    <div class="keyPadding">





                        <q-chip v-for="concept in dialog.keywords" dense
                                :key="concept.id"
                                 color="black" text-color="white"
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
        props: ['eventActionHandler', 'conceptSelectHandler'],
        name: "PrimaryReadingDialog.vue",

        data() {
            return {
                primaryReadingModel: false,
                dialog: {}
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
        },

        methods: {

               conceptSelect(id){
                // this.primaryReadingModel = false;
                this.conceptSelectHandler(id)
            },

            popupContent(event) {
                this.primaryReadingModel = true;
                this.dialog = event
            },

             eventAction(id){
                console.log('ID', id);
                // this.selectedState = !this.selectedState;
                this.eventActionHandler(id)
            }


        },


    }
</script>

<style scoped>

    .keyPadding{
        margin-left: -5px;
    }

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