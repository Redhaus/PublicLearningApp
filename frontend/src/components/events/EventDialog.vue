<template>

    <q-dialog v-model="eventModel">
        <q-card class="lex-card">

            <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{dialog.event_title}}</div>
                <q-space/>
                <q-btn icon="close" flat round dense v-close-popup/>
            </q-card-section>


            <q-separator/>
            <div class="row">

                <q-card-section class="col-4">
                    <div class="subtitle">Collection Name:</div>
                    <div>{{dialog.collection_name}}</div>

                    <div class="subtitle dialog-top">Event Description:</div>
                    <div v-html="dialog.event_descriptor"></div>
                </q-card-section>

                <q-card-section class="col-4">
                    <div class="quote">"{{dialog.quotation}}"</div>
                    <div class="author">–{{dialog.quotation_author}}</div>
                    <div class="author_source" v-html="dialog.quote_source"></div>

                </q-card-section>
                <q-card-section class="col-4">
                    <q-item-label>
                        <q-skeleton animation="none" height="200px" square/>
                    </q-item-label>
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
                eventModel: false,
                dialog: {}
            }
        },

        methods: {
            popupContent(event) {
                this.eventModel = true;
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