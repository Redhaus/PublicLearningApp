<template>


    <!--    <div v-for="lex in lexis_list" :key="lex.id" class="bottom-padding">-->
    <q-card class="cardHandle"
            :class="{ active: selected_list.includes(lex.id) }"
            bordered
            @click="eventAction(lex.id)">

        <q-card-section class="parent">
            <div class="text-title ">{{ lex.term }}
                <span class="pos">{{ lex.part_of_speech }}</span>
            </div>
        </q-card-section>

        <q-separator/>

        <q-card-section>
            <div class="subtitle">Highlight:</div>
            <div v-for="highlight in lex.highlight.slice(0, 1)" :key="highlight.id">
                <div>{{highlight.value}}</div>
            </div>
            <q-separator/>

            <div class="subtitleEtymology">Etymology:</div>
            <div v-html="short_overview(lex.etymology)"></div>
        </q-card-section>

        <q-separator/>

        <div class="q-pa-md q-gutter-sm">
            <q-btn-group spread>
                <q-btn color="purple" label="Preview" icon="visibility"
                       @click.stop="dialogPopup(lex)"/>
            </q-btn-group>

        </div>
    </q-card>



</template>

<script>

    /* eslint-disable */
    import clip from "text-clipper";


    export default {
        props: ['lex', 'selected_list', 'eventActionHandler', 'dialogPopupHandler'],
        name: "LexisCard.vue",
        methods: {
            eventAction(id) {

                this.eventActionHandler(id);
            },

            dialogPopup(lex) {
                this.dialogPopupHandler(lex);
            },

            short_overview(html) {
                const content = clip(html, 100, {html: true, maxLines: 5});
                return content
            },
        },

    }
</script>

<style scoped>

</style>