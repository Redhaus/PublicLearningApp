<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <SearchHeader name="Performances" @searchTerm="search = $event"/>

        </div>
        <div style="width: 100%">

            <div v-if="selected_event">

                <div v-if="performances_list.length > 0">
                    <masonry :cols="4" :gutter="20">
                        <div v-for="performance in performances_list" :key="performance.id" class="bottom-padding">
                            <q-card
                                    class="cardHandle"
                                    :class="{ active: selected_list.includes(performance.id) }"
                                    bordered
                                    @click="eventAction(performance.id)"
                            >
                                <q-card-section>
                                    <div class="text-title">{{ performance.performance_title }}</div>
                                </q-card-section>

                                <q-separator/>
                                <q-card-section>
                                    <div v-html="short_overview(performance.performance_overview)"></div>
                                </q-card-section>


                            </q-card>
                        </div>
                    </masonry>

                </div>
                <div v-else>No Performances Available</div>


            </div>

            <div v-else>Please select an Event</div>

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

    export default {
        components: {
            SearchHeader,
        },
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                // performance_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchPerformances");
            // this.performance_id_list = this.$store.getters["getSelectedPerformances"];

        },

        computed: {

            selected_list() {
                return this.$store.getters["getSelectedPerformances"];
            },


            // this makes sure there is selected event before content is displayed
            selected_event() {

                return this.$store.getters["getSelectedEvent"];
                // console.log('SELECTED_EVENT, :', selectedEvent);
            },

            performances_list() {
                let performances = this.$store.getters["getPerformances"];

                // console.log(this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = performances.filter(obj => {
                        // return obj.term === this.search
                        return obj.performance_title.toLowerCase().includes(this.search.toLowerCase());
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

                return performances;
            }
        },

        methods: {

            short_overview(html) {

                const clippedHtml = clip(html, 140, {html: true, maxLines: 5});

                // console.log('HTMLTRIM', clippedHtml);
                return clippedHtml
            },

            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                this.$store.dispatch("setSelectedPerformances", event);

                // if (this.performance_id_list.includes(event)) {
                //                         this.$store.dispatch("setSelectedPerformances", event);
                //
                //     this.performance_id_list = this.performance_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //                         this.$store.dispatch("setSelectedPerformances", event);
                //
                //     this.performance_id_list.push(event);
                // }
            }
        }
    };
</script>

<style lang="scss" scoped>

    .active {
        background-color: #cccccc;
    }

    /*    .bottom-padding*/
    /*        padding-bottom: 20px*/

    /*        .flex-break*/
    /*            flex: 1 0 100% !important*/
    /*            width: 0 !important*/

    /*        .active*/
    /*            background-color: #cccccc*/

    /*        .test*/
    /*            padding-top: 20px*/
    /*            padding-left: 20px*/

    /*        .page-bar*/
    /*            background-color: #ffffff*/

    /*        .title*/
    /*            font-size: 1.15rem !important*/
    /*            margin: auto*/

    /*            &:focus*/
    /*                outline: none*/

    /*        .full-width-banner*/
    /*            width: 100%*/
    /*            padding-bottom: 20px*/

    /*        .text-white*/
    /*            min-height: 320px*/

    /*        .banner-margin*/
    /*            margin-left: 15px*/
    /*.my-card*/
    /*width: 48%*/
</style>
