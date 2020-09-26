<template>
    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">

        <!-- SEARCHBAR-->
        <div class="col-12">

            <SearchHeader name="Lexis" @searchTerm="search = $event"/>
<!--            <q-banner elevated rounded inline-actions class="page-bar shadow-3">-->
<!--                <div class="row">-->
<!--                    <div class="col-8 title" tabindex="0">-->
<!--                        <div>Lexis</div>-->
<!--                    </div>-->

<!--                    <div class="col-4" tabindex="0">-->
<!--                        <q-input v-model="search" label="Search Lexis" class="q-ml-md">-->
<!--                            <template v-slot:append>-->
<!--                                <q-icon v-if="search === ''" name="search"/>-->
<!--                                <q-icon-->
<!--                                        v-else-->
<!--                                        name="clear"-->
<!--                                        class="cursor-pointer"-->
<!--                                        @click="clearSearch"-->
<!--                                />-->
<!--                            </template>-->
<!--                        </q-input>-->
<!--                    </div>-->

<!--                </div>-->
<!--            </q-banner>-->

            <!-- FILTER TABS-->
            <q-tabs
                    v-model="tab"
                    dense
                    inline-label
                    class="text-grey"
                    no-caps>
                <q-tab @click="clearFilter()" name="all" icon="explore" label="All"/>
                <q-tab @click="filterLexis('device')" name="device" icon="explore" label="Device"/>
                <q-tab @click="filterLexis('essential')" name="essential" icon="stars" label="Essential"/>
                <q-tab @click="filterLexis('common')" name="common" icon="language" label="Common"/>
                <q-tab @click="filterLexis('concept')" name="concept" icon="lightbulb" label="Concept"/>
                <q-tab @click="filterLexis('person')" name="person" icon="account_box" label="Person"/>

            </q-tabs>

        </div>


        <!-- LEXIS CARDS-->
        <div style="width: 100%">
            <div v-if="selected_event">
                <div v-if="lexis_list.length > 0">
                    <masonry :cols="4" :gutter="20">
                        <div v-for="lex in lexis_list" :key="lex.id" class="bottom-padding">
                            <q-card
                                    class="cardHandle"
                                    :class="{ active: selected_list.includes(lex.id) }"
                                    bordered
                                    @click="eventAction(lex.id)">

                                <q-card-section class="parent">
                                    <div class="text-title ">{{ lex.term }}<span
                                            class="pos">{{ lex.part_of_speech }}</span></div>
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
                                               @click.stop="popupContent(lex)"/>
                                    </q-btn-group>

                                </div>
                            </q-card>

                        </div>

                    </masonry>


                    <!-- DIALOG -->
                    <q-dialog v-model="icon">
                        <q-card class="lex-card">

                            <q-card-section class="row items-center q-pb-none">
                                <div class="text-h6">{{dialog2.term}}</div>
                                <q-space/>
                                <q-btn icon="close" flat round dense v-close-popup/>
                            </q-card-section>


                            <q-separator/>
                            <div class="row">
                                <q-card-section class="col-2 ">
                                    <div class="subtitle">Part of Speech:</div>
                                    <div>{{dialog2.part_of_speech}}</div>
                                    <div class="subtitle dialog-top">Derivations:</div>
                                    <div v-for="derivation in dialog2.derivations" :key="derivation.id">
                                        <div>{{derivation.value}}</div>
                                    </div>

                                    <div class="subtitle dialog-top">Linked Lexis:</div>
                                    <div v-for="lex2 in dialog2.lexis_link" :key="lex2.id">
                                        <div>{{lex2.value}}</div>
                                    </div>


                                    <q-separator vertical/>

                                </q-card-section>
                                <q-card-section class="col-5 ">
                                    <div class="subtitle">Etymology:</div>
                                    <div v-html="dialog2.etymology"></div>

                                    <div class="subtitle dialog-top">Quote:</div>

                                    <div>"{{dialog2.quotation}}"</div>
                                    <div class="dialog-top">{{dialog2.quote_source}}</div>
                                    <div>{{dialog2.quotation_author}}</div>


                                </q-card-section>

                                <q-card-section class="col-5 ">
                                    <div class="subtitle">Applications:</div>
                                    <ul class="indent">
                                        <li v-for="application in dialog2.application" :key="application.id">
                                            {{application.value}}
                                        </li>
                                    </ul>
                                    <q-separator vertical/>

                                    <div class="subtitle dialog-top">Exploration:</div>
                                    <ol class="indent">
                                        <li v-for="exploration in dialog2.exploration" :key="exploration.id">
                                            {{exploration.value}}
                                        </li>
                                    </ol>

                                </q-card-section>

                            </div>
                        </q-card>
                    </q-dialog>

                </div>

                <div v-else>No Lexis Available</div>
            </div>

            <div v-else>Please select an Event</div>
        </div>

        <div style="height: 50px"/>

    </div>
</template>


<!--SCRIPTS-->
<script>
    import clip from "text-clipper";
    import SearchHeader from "../components/SearchHeader";

    export default {

        components: {
            SearchHeader
        },
        data() {
            return {
                loader_visible: false,
                showSimulatedReturnData: false,
                // lexis_id_list: [],
                search: '',
                filter: '',
                tab: 'all',
                icon: false,
                dialog2: {}
            };
        },

        created() {
            // console.log('LEXISLIST', this.lexis_list);
            this.$store.dispatch("fetchLexis");
            // this.lexis_id_list = this.$store.getters["getSelectedLexis"];
        },

        computed: {

            selected_list(){
                return this.$store.getters["getSelectedLexis"];
            },

            // this makes sure there is selected event before content is displayed
            selected_event() {
                return this.$store.getters["getSelectedEvent"];
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

        // watch: {
        //     'this.$store.state': function () {
        //         console.log('LEXFULLSTATE', this.$store.state)
        //     }
        // },

        methods: {

            short_overview(html) {

                const clippedHtml = clip(html, 100, {html: true, maxLines: 5});
                return clippedHtml
            },

            // this is the dialog for lexis preview
            popupContent(lex) {
                this.icon = true;
                this.dialog = {
                    term: lex.term,
                    etymology: lex.etymology,
                    part_of_speech: lex.part_of_speech
                };
                this.dialog2 = lex
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
                console.log(event)

                // if (this.lexis_id_list.includes(event)) {
                //     this.lexis_id_list = this.lexis_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
               this.$store.dispatch("setSelectedLexis", event);
                //     this.lexis_id_list.push(event);
                // }
            }
        }
    };
</script>


<!--STYLES-->

<style lang="scss">

    .indent {
        padding-left: 20px;
    }

    .cardHandle {
        transition: all .15s ease-in-out;

        &:hover {
            background-color: #EEEEEE;
            /*transform: scale(.96);*/
        }


    }

    .q-tab--active {
        color: #000000 !important;
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

    }

    .subtitle {
        font-size: .8rem !important;
        font-weight: bold;
    }

    .subtitleEtymology {
        padding-top: 10px;
        font-size: .8rem !important;
        font-weight: bold;
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

    .banner-margin {
        margin-left: 15px;
    }


    .pos {
        float: right;
        font-weight: normal;
    }

    .q-dialog__inner--minimized > div {
        /*max-width: none !important;*/
    }

    .dialog-top {
        padding-top: 10px;
    }

    .lex-card {
        max-width: 70% !important;
    }


</style>

