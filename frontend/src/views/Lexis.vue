<template>
    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">


        <div class="col-12">
            <!-- SEARCHBAR-->
            <SearchHeader name="Lexis" @searchTerm="search = $event"/>

            <!-- FILTER TABS-->
            <div v-if="selected_event">
            <LexisFilter @filterTerm="filter = $event"/>
                 </div>

        </div>

        <!-- LEXIS CARDS-->
        <div style="width: 100%">
            <div v-if="selected_event">
                <div v-if="lexis_list.length > 0">
                    <masonry :cols="4" :gutter="20">
                        <div v-for="lex in lexis_list" :key="lex.id" class="bottom-padding">

                            <!--    LEXIS CARDS-->
                            <LexisCard :eventActionHandler="eventAction"
                                       :dialogPopupHandler="dialogPopup"
                                       :selected_list="selected_list"
                                       :lex="lex"/>
                        </div>
                    </masonry>

                    <!-- DIALOG -->
                    <LexisDialog ref="dialogComponent"/>

                </div>
                <!-- if not items available-->
                <div v-else>No Lexis Available</div>
            </div>
            <!--  if no event separate-->
            <div v-else>Please select an Event</div>
        </div>

        <div style="height: 50px"/>

    </div>
</template>


<!--SCRIPTS-->
<script>
    import SearchHeader from "../components/SearchHeader";
    import LexisFilter from "../components/lexis/LexisFilter";
    import LexisDialog from "../components/lexis/LexisDialog";
    import LexisCard from "../components/lexis/LexisCard";
    import {MyFunctions} from "../utils/utils";

    export default {

        components: {
            SearchHeader,
            LexisFilter,
            LexisDialog,
            LexisCard
        },
        data() {
            return {
                loader_visible: false,
                showSimulatedReturnData: false,
                search: '',
                filter: '',
            };
        },

        created() {
            // console.log('LEXISLIST', this.lexis_list);
            this.$store.dispatch("fetchLexis");
            // this.lexis_id_list = this.$store.getters["getSelectedLexis"];
        },

        computed: {
            // used for highlight selected checks list and highlights accordingly
            selected_list() {
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
                if (this.filter) {
                    // filter search function (lexis, filter search)
                    return MyFunctions.filterSearchFunction(lexis, this.filter, this.search, 'icons', 'term');
                }

                // If search field has value
                if (this.search.length > 0) {
                    // search filter (data, search, item to compare)
                    return MyFunctions.searchFunction(lexis, this.search, 'term');
                }

                // if not filters return full lexis
                return lexis;

            }
        },
        methods: {

            dialogPopup(lex) {
                // call child popup function
                this.$refs.dialogComponent.popupContent(lex);
            },

            // this sets active class on selected items
            eventAction(event) {
                this.$store.dispatch("setSelectedLexis", event);
            }
        }
    };
</script>


<!--STYLES-->

<style lang="scss">


</style>

