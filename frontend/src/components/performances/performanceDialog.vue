<template>

    <q-dialog v-model="primaryReadingModel">
        <q-card class="lex-card">


            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.performance_title}}</div>
                <q-space/>
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

                    <div class="subtitle dialog-top">Student Sample:</div>
                    <q-item-label>
                        <a :href="dialog.student_sample">
                            <q-skeleton animation="none" height="250px" square/>
                        </a>
                    </q-item-label>


                    <div v-if="dialog.star_valuey" class="subtitle dialog-top">Star Rating:</div>
                    <div>{{dialog.star_valuey}}</div>

                    <div v-if="lexLength">
                        <div class="subtitle dialog-top">Related Lexis:</div>
                        <div v-for="lex in dialog.performance_lexis_link" :key="lex.id">
                            <q-chip dense :label="lex.term"/>
                        </div>
                    </div>



                    <q-separator vertical/>
                </q-card-section>

                <q-card-section class="col-9 ">
                    <div class="subtitle">Performance Description:</div>
                    <div v-html="dialog.performance_description"></div>

                    <div class="subtitle dialog-top">Performance Overview:</div>
                    <div>{{dialog.performance_overview}}</div>


                    <div class="subtitle dialog-top">Performance Feats:</div>
                    <div>
                        <q-list bordered separator dense>
                            <q-item v-for="feat in dialog.performance_feat_link" :key="feat.id" >
                                <q-item-section>{{feat.performance_feats}}</q-item-section>
                                </q-item>
                        </q-list>
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
        // props: ['dialog', 'iconState'],
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

            },

            lexLength(){

                 if(this.dialog.performance_lexis_link && this.dialog.performance_lexis_link.length > 0){
                    return true
                }else{
                    return false
                }

            }

        },

        methods: {
            popupContent(event) {
                this.primaryReadingModel = true;
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