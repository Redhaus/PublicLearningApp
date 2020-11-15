<template>
    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">


               <div style="width: 100%">
            <NextBtn class="float-right" section_name="Questions" :selected_item="selected_item"/>
        </div>

        <div class="col-12">
            <!-- SEARCHBAR-->
<!--            <SearchHeader name="Lexis" @searchTerm="search = $event"/>-->
            <LessonSearchHeader
                    pageName="Lexis"
                    filterName="Filter Categories"
                    :class_options_filter=options_filter
                    @searchTerm="search = $event"
                    @classFilter="filter = $event.value"/>

            <!-- FILTER TABS-->
            <div v-if="selected_event">
<!--            <LexisFilter @filterTerm="filter = $event"/>-->
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
                    <LexisDialog ref="dialogComponent"
                                 :eventActionHandler="eventAction"
                                 :selected_list="selected_list"
                                 :lexisLinkHandler="dialogPopup2"
                    />

                    <LexisDialog2 ref="dialogComponent2"
                                 :eventActionHandler="eventAction"
                                 :selected_list="selected_list"

                    />



                </div>
                <!-- if not items available-->
                <div class="selectEventNotification" v-else>No Lexis Available</div>
            </div>
            <!--  if no event separate-->
            <div class="selectEventNotification" v-else>Please select an Event</div>
        </div>

        <div style="height: 50px"/>

    </div>
</template>


<!--SCRIPTS-->
<script>
    // import SearchHeader from "../components/SearchHeader";
    // import LexisFilter from "../components/lexis/LexisFilter";
    import LexisDialog from "../components/lexis/LexisDialog";
    import LexisCard from "../components/lexis/LexisCard";
    import {MyFunctions} from "../utils/utils";
    import NextBtn from "../components/NextBtn";
    import LessonSearchHeader from "../components/lessons/LessonSearchHeader";
    import LexisDialog2 from "../components/lexis/LexisDialog2";





    export default {

        components: {
            // SearchHeader,
            // LexisFilter,
            LexisDialog,
            LexisCard,
            NextBtn,
            LessonSearchHeader,
            LexisDialog2

        },
        data() {
            return {
                loader_visible: false,
                showSimulatedReturnData: false,
                search: '',
                filter: '',
                options_filter: [
                    {
                        label: 'All',
                        value: ''
                    },
                    {
                        label: 'Device',
                        value: 'Device'
                    },
                    {
                        label: 'Essential',
                        value: 'Essential'
                    },
                    {
                        label: 'Common',
                        value: 'Common'
                    },
                    {
                        label: 'Concept',
                        value: 'Concept'
                    },
                    {
                        label: 'Person',
                        value: 'Person'
                    }]

            }
        },


        created() {
            // console.log('LEXISLIST', this.lexis_list);
            this.$store.dispatch("fetchLexis");
            // this.lexis_id_list = this.$store.getters["getSelectedLexis"];
        },

        computed: {



              selected_item(){

                if(this.selected_list.length > 0){
                    console.log('OFF');
                    return true;
                }else{
                    console.log('ON');
                    return false;
                }

            },

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

            dialogPopup2(id) {
                // call child popup function

                let lexis = this.$store.getters["getLexis"];


  // let newLex = lexis.find(x => x.term === this.search);

                let lex = lexis.find(x => x.id === id);
                console.log(lex);
                this.$refs.dialogComponent2.popupContent(lex);
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

    .highlight-content{
        padding-bottom: 5px;
    }


</style>

