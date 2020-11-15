<template>
    <!--<q-scroll-area >-->

    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md">

          <div style="width: 100%">
            <NextBtn class="float-right" section_name="Goals" :selected_item="selected_item"/>
        </div>

        <div class="col-12">
            <SearchHeader name="Extensions" @searchTerm="search = $event"/>
        </div>


        <div style="width: 100%">

            <div v-if="selected_event">

                <div v-if="extensions_list.length > 0">
                    <masonry :cols="4" :gutter="20">
                        <div v-for="ex in extensions_list" :key="ex.id" class="bottom-padding">
                            <q-card
                                    class="cardHandle"
                                    :class="{ active: selected_list.includes(ex.id) }"
                                    bordered
                                    @click="eventAction(ex.id)"
                            >
                                <q-card-section>
                                    <div class="text-title">{{ ex.action }}</div>
                                </q-card-section>
                                <q-separator/>

                                <q-card-section>

                                    <div v-html="short_overview(ex.explanation)"></div>
                                </q-card-section>

                                <div class="btnContainer">
                                    <q-separator/>
                                    <q-card-actions class="items-bottom" align="right">
                                        <q-btn @click.stop="dialogPopup(ex)" dense flat round
                                               color="grey" icon="o_open_in_new"/>
                                    </q-card-actions>
                                </div>


                            </q-card>
                        </div>
                    </masonry>

                    <ExtensionsDialog ref="dialogComponent" style="min-width: 70%"
                     :eventActionHandler="eventAction"
                                 :selected_list="selected_list"
                    />
                </div>
                <div class="selectEventNotification" v-else>No Extensions Available</div>

            </div>

            <div class="selectEventNotification" v-else>Please select an Event</div>
        </div>

        <!--        <div class="col-4" v-for="lex in lexis_list" :key="lex.id">-->

        <!--            <q-card-->
        <!--                    :class="{'active': event_id_list.includes(lex.id)}"-->

        <!--                    bordered-->
        <!--                    @click="eventAction(lex.id)">-->

        <!--                <q-card-section>-->
        <!--                    <h4>{{lex.term}}</h4>-->
        <!--                    <div v-html="lex.etymology"></div>-->
        <!--                </q-card-section>-->

        <!--            </q-card>-->

        <!--        </div>-->

        <div style="height: 50px"/>
    </div>
</template>
<script>
    import clip from "text-clipper";

    import SearchHeader from "../components/SearchHeader";
    import ExtensionsDialog from "../components/extensions/ExtensionsDialog";
    import NextBtn from "../components/NextBtn";

    export default {


        components: {
            SearchHeader,
            ExtensionsDialog,
            NextBtn
        },
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                // extensions_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchExtensions");
            // this.extensions_id_list = this.$store.getters["getSelectedExtensions"];

        },

        computed: {

             selected_item() {
                if (this.selected_list.length > 0) {
                    return true;
                } else {
                    return false;
                }
            },

            // this tracks the selected items from the store and highlights accordingly
            selected_list() {
                return this.$store.getters["getSelectedExtensions"];
            },

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                // console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },


            extensions_list() {
                let extensions = this.$store.getters["getExtensions"];

                // console.log(this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = extensions.filter(obj => {
                        // return obj.term === this.search
                        return obj.action.toLowerCase().includes(this.search.toLowerCase());
                    });
                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }
                //
                // if(this.search.length > 0){
                //       newLex  = lexis.filter(function (item) {
                //         return item === this.search;
                //     });
                //     return newLex
                // }

                return extensions;
            }
        },

        methods: {

              dialogPopup(ext) {
                // call child popup function
                this.$refs.dialogComponent.popupContent(ext);
            },

            short_overview(html) {

                const clippedHtml = clip(html, 100, {html: true, maxLines: 5});

                // console.log('HTMLTRIM', clippedHtml);
                return clippedHtml
            },

            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                this.$store.dispatch("setSelectedExtensions", event);

                // if (this.extensions_id_list.includes(event)) {
                //     this.$store.dispatch("setSelectedExtensions", event);
                //     this.extensions_id_list = this.extensions_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //       this.$store.dispatch("setSelectedExtensions", event);
                //     this.extensions_id_list.push(event);
                // }
            }
        }
    };
</script>

<style lang="scss" scoped>

    .active {
        background-color: #cccccc;
    }

    /*.my-card*/
    /*width: 48%*/
</style>
