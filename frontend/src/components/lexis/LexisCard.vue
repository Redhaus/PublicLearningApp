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

            <div class="subtitle padTop">Etymology:</div>
            <div class="shortOverview" v-html="short_overview(lex.etymology)"></div>
        </q-card-section>



        <div class="btnContainer">
                    <q-separator/>

        <q-card-actions class="items-bottom" align="right">
                          <q-btn @click.stop="dialogPopup(lex)" dense flat round color="grey" icon="o_open_in_new"/>
        </q-card-actions>
            </div>



<!--        <div class="q-pa-md q-gutter-sm">-->
<!--             <q-btn @click.stop="dialogPopup(lex)" dense flat round color="gray" icon="o_open_in_new"/>-->

<!--        </div>-->
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

<style >


    .btnContainer{
        display: block;
        height: 50px;
        width: 100%;
    }


     .items-bottom {
        position: absolute;
        bottom: 0;
        right: 0;
    }

    div.shortOverview > p{
        margin: 0;
    }

    .padTop {
                padding-top: 10px;

    }





</style>