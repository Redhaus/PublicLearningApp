<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Exploration</div>
                    </div>

                    <div class="col-4" tabindex="0">
                        <q-input v-model="search" label="Search Lexis" class="q-ml-md">
                            <template v-slot:append>
                                <q-icon v-if="search === ''" name="search"/>
                                <q-icon
                                        v-else
                                        name="clear"
                                        class="cursor-pointer"
                                        @click="clearSearch"
                                />
                            </template>
                        </q-input>

                    </div>
                </div>
            </q-banner>
        </div>
        <div style="width: 100%">

            <div v-if="selected_event">

                               <div v-if="exploration_list.length > 0">

            <masonry :cols="3" :gutter="20">
                <div v-for="ex in exploration_list" :key="ex.id" class="bottom-padding">
                    <q-card
                            :class="{ active: exploration_id_list.includes(ex.id) }"
                            bordered
                            @click="eventAction(ex.id)"
                    >
                        <q-card-section>
                            <h4>{{ ex.title_minor }}</h4>

                        </q-card-section>
                    </q-card>
                </div>
            </masonry>
                </div>
                    <div v-else>No Explorations Available</div>

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
    export default {
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                exploration_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchExplorations");
            this.exploration_id_list = this.$store.getters["getSelectedExplorations"];

        },

        computed: {

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },

            exploration_list() {
                let explorations = this.$store.getters["getExplorations"];

                console.log(this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = explorations.filter(obj => {
                        // return obj.term === this.search
                        return obj.title_minor.toLowerCase().includes(this.search.toLowerCase());
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

                return explorations;
            }
        },

        methods: {
            clearSearch() {
                this.search = "";
            },

            eventAction(event) {
                if (this.exploration_id_list.includes(event)) {
                     this.$store.dispatch("setSelectedExplorations", event);
                    this.exploration_id_list = this.exploration_id_list.filter(function (item) {
                        return item !== event;
                    });
                } else {
                     this.$store.dispatch("setSelectedExplorations", event);
                    this.exploration_id_list.push(event);
                }
            }
        }
    };
</script>

<style lang="scss" scoped>

      .active {
        background-color: #cccccc;
    }

</style>
