<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Lexis</div>


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

            <q-tabs
                    v-model="tab"
                    dense
                    inline-label
                    class="text-grey"
            >
                <q-tab @click="clearFilter()" name="all" icon="explore" label="all"/>
                <q-tab @click="filterLexis('device')" name="device" icon="explore" label="device"/>
                <q-tab @click="filterLexis('essential')" name="essential" icon="stars" label="essential"/>
                <q-tab @click="filterLexis('common')" name="common" icon="language" label="common"/>
                <q-tab @click="filterLexis('concept')" name="concept" icon="lightbulb" label="concept"/>
                <q-tab @click="filterLexis('person')" name="person" icon="account_box" label="person"/>

            </q-tabs>


        </div>


        <div v-if="selected_event">

            <div v-if="lexis_list.length > 0">

                <masonry :cols="3" :gutter="20">

                    <div v-for="lex in lexis_list" :key="lex.id" class="bottom-padding">

                        <q-card
                                class="cardHandle"
                                :class="{ active: lexis_id_list.includes(lex.id) }"
                                bordered
                                @click="eventAction(lex.id)">

                            <q-card-section>
                                <div class="q-pa-md q-gutter-sm">
                                    <q-btn label="Preview" color="primary" @click.stop="popupContent(lex)"/>
                                </div>
                                <!--                                        <q-btn label="Close Icon" color="primary" @click="icon = true" />-->
                                <h4>{{ lex.term }}</h4>
                                <div v-html="lex.etymology"></div>
                            </q-card-section>
                        </q-card>


                    </div>

                </masonry>


                <q-dialog v-model="icon">
                    <q-card>
                        <q-card-section class="row items-center q-pb-none">
                            <div class="text-h6">{{dialog.term}} | {{dialog.part_of_speech}}</div>
                            <q-space/>
                            <q-btn icon="close" flat round dense v-close-popup/>
                        </q-card-section>

                        <q-card-section>
                            {{dialog.etymology}}
                        </q-card-section>
                    </q-card>
                </q-dialog>

            </div>


            <div v-else>No Lexis Available</div>


        </div>


        <div v-else>Please select an Event</div>


        <div style="height: 50px"/>

        <!--        this is a loader for inner areas connected to content loading computed property-->
        <!--         <q-inner-loading :showing="contentLoading">-->
        <!--        <q-spinner-oval size="50px" color="primary" />-->
        <!--      </q-inner-loading>-->

    </div>
</template>
<script>
    export default {
        data() {
            return {

                loader_visible: false,
                showSimulatedReturnData: false,

                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                lexis_id_list: [],
                search: '',
                filter: '',
                tab: 'all',
                icon: false,
                dialog: {
                    term: '',
                    etymology: '',
                    part_of_speech: '',
                }
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            // showTextLoading () {
            // this.loader_visible = true;
            // this.showSimulatedReturnData = false
            // setTimeout(() => {
            //   this.visible = false
            //   this.showSimulatedReturnData = true
            // }, 3000)

            console.log('LEXISLIST', this.lexis_list);
            this.$store.dispatch("fetchLexis");
            this.lexis_id_list = this.$store.getters["getSelectedLexis"];

        },

        computed: {

            // contentLoading(){
            //     // return false
            //     console.log('LOADING:', this.lexis_list.length <= 0);
            //     return this.lexis_list.length <= 0;
            // },

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },


            // This handles all the lexis and filter of lexis
            lexis_list() {
                // get Lexis from store
                let lexis = this.$store.getters["getLexis"];

                // if there is a filter value run function to filter results
                if (this.filter) {

                    // create empty array to hold filtered values
                    let filteredList = [];

                    // loop through each lex item to get to their icon_list
                    lexis.forEach((item) => {

                        // loop through each icon list to see if icon matches filter
                        item.icon_list.forEach(obj => {

                            // if matches add original item to filterList Array
                            if (obj.icons.toLowerCase() === this.filter.toLowerCase()) {
                                filteredList.push(item)
                            }
                        })
                    });

                    // if there is also a search value and filter value check search against filteredList array
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    if (this.search.length > 0) {

                        // check if items term include search values
                        return filteredList.filter(obj => {
                            return obj.term.toLowerCase().includes(this.search.toLowerCase());
                        });
                        // return filterSearch;
                    }

                    // return filteredList if no search value
                    return filteredList


                }
                //  end if filter statement


                // If search field has value
                if (this.search.length > 0) {
                    // return all filtered items whose term include the search values
                    return lexis.filter(obj => {
                        return obj.term.toLowerCase().includes(this.search.toLowerCase());
                    });
                }

                // if not filters return full lexis
                return lexis;

            }
        },

        methods: {

            // this is the dialog for lexis preview
            popupContent(lex) {
                this.icon = true;
                this.dialog = {
                    term: lex.term,
                    etymology: lex.etymology,
                    part_of_speech: lex.part_of_speech
                }
            },

            // this clears filter when all is selected
            clearFilter() {
                this.filter = '';
            },

            //sets lexis filter data var
            filterLexis(_filter) {
                this.filter = _filter;
            },

            // this clears search field
            clearSearch() {
                this.search = "";
            },

            // this sets active class on selected items
            eventAction(event) {


                if (this.lexis_id_list.includes(event)) {
                    console.log('REMOVE');
                    this.$store.dispatch("setSelectedLexis", event);

                    this.lexis_id_list = this.lexis_id_list.filter(function (item) {
                        return item !== event;
                    });
                } else {
                    this.$store.dispatch("setSelectedLexis", event);

                    console.log('ADD');
                    this.lexis_id_list.push(event);
                }
            }
        }
    };
</script>

<style lang="scss">

    .cardHandle {
        transition: all .15s ease-in-out;

        &:hover {
            background-color: #EEEEEE;
            /*transform: scale(.96);*/
        }

        /*&:active {*/
        /*    !*color: #B25500;*!*/
        /*    transform: scale(.95);*/

        /*}*/

    }


    .bottom-padding {
        padding-bottom: 20px;
    }

    .flex-break {
        flex: 1 0 100% !important;
        width: 0 !important;
    }

    .active {
        background-color: #cccccc !important;
            transform: scale(.96);

        /*&:hover {*/
        /*    background-color: #EEEEEE;*/
        /*}*/
    }

    .test {
        padding-top: 20px;
        padding-left: 20px;
    }

    .page-bar {
        background-color: #ffffff;
    }

    .title {
        font-size: 1.15rem !important;
        margin: auto;

        &:focus {
            outline: none;
        }
    }

    .full-width-banner {
        width: 100%;
        padding-bottom: 20px;
    }

    /*.text-white*/
    /*min-height: 320px*/


    .banner-margin {
        margin-left: 15px;
    }

    /*.my-card*/
    /*width: 48%*/
</style>



