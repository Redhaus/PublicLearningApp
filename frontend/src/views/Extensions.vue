<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Extensions</div>
                    </div>

                    <div class="col-4" tabindex="0">
                        <q-input v-model="search" label="Search Extensions" class="q-ml-md">
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
                        <!--                        <q-input filled bottom-slots v-model="search"  label="Search Lexis"  class="q-ml-md">-->
                        <!--                            <template v-slot:append>-->
                        <!--                                <q-icon v-if="search === ''" name="search"/>-->
                        <!--                                <q-icon v-else name="clear" class="cursor-pointer" @click="clearSearch"/>-->
                        <!--                            </template>-->
                        <!--                        </q-input>-->
                    </div>
                </div>
            </q-banner>
        </div>

        <div style="width: 100%">

            <div v-if="selected_event">

              <div v-if="extensions_list.length > 0">
                <masonry :cols="4" :gutter="20">
                    <div v-for="ex in extensions_list" :key="ex.id" class="bottom-padding">
                        <q-card
                                :class="{ active: extensions_id_list.includes(ex.id) }"
                                bordered
                                @click="eventAction(ex.id)"
                        >
                            <q-card-section>
                                <h4>{{ ex.action }}</h4>
                                <div v-html="ex.explanation"></div>
                            </q-card-section>
                        </q-card>
                    </div>
                </masonry>
                  </div>
                    <div v-else>No Extensions Available</div>

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
                extensions_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchExtensions");
            this.extensions_id_list = this.$store.getters["getSelectedExtensions"];

        },

        computed: {

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },


            extensions_list() {
                let extensions = this.$store.getters["getExtensions"];

                console.log(this.search);

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
            clearSearch() {
                this.search = "";
            },

            eventAction(event) {
                if (this.extensions_id_list.includes(event)) {
                    this.$store.dispatch("setSelectedExtensions", event);
                    this.extensions_id_list = this.extensions_id_list.filter(function (item) {
                        return item !== event;
                    });
                } else {
                      this.$store.dispatch("setSelectedExtensions", event);
                    this.extensions_id_list.push(event);
                }
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
