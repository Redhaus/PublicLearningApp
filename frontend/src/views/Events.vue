<template>
    <div class="test event fit row wrap justify-start items-start content-start q-col-gutter-md ">

            <div style="width: 100%">
        <NextBtn class="float-right" section_name="Readings" :selected_item="selected_item"/>
            </div>

        <div class="col-12">

              <LessonSearchHeader
                    pageName="Events"
                    filterName="Filter Collection"
                    :class_options_filter=options_filter
                    @searchTerm="search = $event"
                    @classFilter="filter = $event.value"/>


<!--            <SearchHeader name="Events" @searchTerm="search = $event"/>-->

            <!--  v-if="is_new && !is_editing"-->
<!--            <q-tabs v-if="!is_editing"-->
<!--                    v-model="tab"-->
<!--                    dense-->
<!--                    inline-label-->
<!--                    class="text-grey paddingFive"-->
<!--                    no-caps>-->
<!--                -->
<!--                <q-tab @click="filterEvent('')" name="all" label="All"/>-->

<!--                <q-tab @click="filterEvent('A Survey in Western Literature I')" name="aswl1"-->
<!--                       label="Western Literature I"/>-->
<!--                <q-tab @click="filterEvent('A Survey in Western Literature II')" name="aswl2"-->
<!--                       label="Western Literature II"/>-->
<!--                <q-tab @click="filterEvent('A Survey in European Literature I')" name="asel1"-->
<!--                       label="European Literature I"/>-->
<!--                <q-tab @click="filterEvent('A Survey in American Literature I')" name="asal1"-->
<!--                       label="American Literature I"/>-->


<!--            </q-tabs>-->

<!--            <q-btn class="float-right marginNegThirty" @click.stop="nextSection('Readings')" dense flat round-->
<!--                   :color="btnColor" icon="arrow_right_alt"/>-->

            <!--            -->
            <!--     <q-icon-->
            <!--             size="20px"-->
            <!--      name="arrow_right_alt"-->
            <!--      class="float-right"-->
            <!--    />-->


        </div>

<!--SINGLE EVENTS FOR EDIT LESSON-->

        <div v-if="is_editing" style="width: 100%">

            <!--EVENTS-->
            <div class="col-12">
                <!--          <div class="q-pa-md col-xs-12 col-sm-6 col-md-6 col-lg-6">-->

<!--                 <masonry :cols="1" :gutter="20">-->

<!--                    <div v-for="event in events_list[1]" :key="event.id">-->
                        <q-card
                                class="cardHandle"
                                :class="{ active: selected_item === current_event.id }"
                                bordered
                             >



                             <q-card-section class="row items-center q-pb-none">
                <div class="text-h6">{{current_event.event_title}}</div>
                <q-space/>
<!--                <q-btn icon="close" flat round dense v-close-popup/>-->
            </q-card-section>


            <q-separator/>
            <div class="row">

                <q-card-section class="col-4">
                    <div class="subtitle">Collection Name:</div>
                    <div>{{current_event.collection_name}}</div>

                    <div class="subtitle dialog-top">Event Description:</div>
                    <div v-html="current_event.event_descriptor"></div>
                </q-card-section>

                <q-card-section class="col-4">
                    <div class="quote">"{{current_event.quotation}}"</div>
                    <div class="author">–{{current_event.quotation_author}}</div>
                    <div class="author_source" v-html="current_event.quote_source"></div>

                </q-card-section>
                <q-card-section class="col-4">
                    <q-item-label>
                        <q-skeleton animation="none" height="200px" square/>
                    </q-item-label>
                </q-card-section>

            </div>

                 </q-card>



<!--                            <div class="btnContainer">-->
<!--                                <q-separator/>-->
<!--                                <q-card-actions class="items-bottom" align="right">-->
<!--                                    <q-btn @click.stop="dialogPopup(current_event)" dense flat round-->
<!--                                           color="grey" icon="o_open_in_new"/>-->
<!--                                </q-card-actions>-->
<!--                            </div>-->


<!--                    </div>-->

<!--                </masonry>-->

<!--                -->
<!--                <q-card>-->
<!--                    <q-card-section>-->
<!--                        <div class="subtitle ">Current Event:</div>-->
<!--                        <div class="dialog-top">-->
<!--                            <div class="event_title">{{current_event.event_title}}</div>-->
<!--                        </div>-->
<!--                    </q-card-section>-->
<!--                </q-card>-->
                <!--          </div>-->
            </div>


        </div>

<!--LIST OF EVENTS FOR NEW LESSON-->
        <div v-if="!is_editing" style="width: 100%">
            <!--                    <div v-if="!is_editing" style="width: 100%">-->

            <div v-if="events_list.length > 0">

                <masonry :cols="4" :gutter="20">

                    <div v-for="event in events_list" :key="event.id">
                        <q-card
                                class="cardHandle"
                                :class="{ active: selected_item === event.id }"
                                bordered
                                @click="eventAction(event.id)">
                            <q-card-section>
                                <div class="text-title">{{ event.event_title }}</div>
                            </q-card-section>
                            <q-separator/>
                            <q-card-section>
                                <p>{{ event.event_descriptor }}</p>
                            </q-card-section>


                            <div class="btnContainer">
                                <q-separator/>
                                <q-card-actions class="items-bottom" align="right">
                                    <q-btn @click.stop="dialogPopup(event)" dense flat round
                                           color="grey" icon="o_open_in_new"/>
                                </q-card-actions>
                            </div>

                        </q-card>
                    </div>

                </masonry>

                <!-- DIALOG -->
                <EventDialog ref="dialogComponent" :eventActionHandler="eventAction"/>
<!-- @gradeLevelEvent="grade_level = $event"-->

            </div>


            <div v-else>No Events Available</div>

        </div>

        <!--          <div v-else>Please create a new lesson on dashboard</div>-->

    </div>
</template>
<script>
    import {MyFunctions} from "../utils/utils";
    // import SearchHeader from "../components/SearchHeader";
    import EventDialog from "../components/events/EventDialog";
    import NextBtn from "../components/NextBtn";
    import LessonSearchHeader from "../components/lessons/LessonSearchHeader";


    export default {
        components: {
            // SearchHeader,
            EventDialog,
            NextBtn,
            LessonSearchHeader
        },

        data() {
            return {
                event_id_list: 0,
                search: '',
                tab: 'all',
                filter: '',
                is_editing: '',

                options_filter: [
                    {
                        label: 'All',
                        value: ''
                    },
                    {
                        label: 'A Survey in Western Literature I',
                        value: 'A Survey in Western Literature I'
                    },
                    {
                        label: 'A Survey in Western Literature II',
                        value: 'A Survey in Western Literature II'
                    },
                    {
                        label: 'A Survey in European Literature I',
                        value: 'A Survey in European Literature I'
                    },
                    {
                        label: 'A Survey in American Literature I',
                        value: 'A Survey in American Literature I'
                    }
                   ]






                // selected_event: ''
            };
        },

        methods: {





            // nextSection(section) {
            //      this.$router.push({name: section});
            // },

            dialogPopup(events) {
                // call child popup function
                this.$refs.dialogComponent.popupContent(events);
            },


            //sets lexis filter data var
            filterEvent(_filter) {
                this.filter = _filter;
            },

            clearSearch() {
                this.search = "";
            },
            eventAction(event) {


                this.$store.dispatch('clearOldEventLesson');
                this.$store.dispatch("setSelectedEvent", event);

                // if (this.event_id_list === event) {
                //     this.$store.dispatch("setSelectedEvent", event);
                //     this.event_id_list = '';
                // } else {
                //     this.$store.dispatch("setSelectedEvent", event);
                //     this.event_id_list = event;
                // }
                // if (this.event_id_list === event) {
                //     this.event_id_list = this.event_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.event_id_list.push(event);
                // }


                // if (this.event_id_list.includes(event)) {
                //     this.event_id_list = this.event_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.event_id_list.push(event);
                // }
            },


        },

        created() {


            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            this.$store.dispatch("fetchEvents");
            this.event_id_list = this.$store.getters["getSelectedEvent"];
            this.is_editing = this.$store.getters['getIsEditing'];
            this.is_new = this.$store.getters['getIsNew'];

            // this.selected_event = this.$store.getters
        },

        computed: {

            // btnColor(){
            //     if (this.selected_item){
            //         return 'secondary'
            //     }else{
            //         return 'grey'
            //     }
            // },

            selected_item() {
                return this.$store.getters["getSelectedEvent"];
            },

            current_event() {
                let events = this.$store.getters["getEvents"];
                return events.find(element => element.id === this.event_id_list)
                // return event
            },

            events_list() {

                let events = this.$store.getters["getEvents"];
                // console.log(this.search);

                if (this.filter) {
                    // filter search function (lexis, filter search)
                    return MyFunctions.filterEventsSearch(events, this.filter, this.search, 'collection_name', 'event_title');
                }

                // If search field has value
                if (this.search.length > 0) {
                    // search filter (data, search, item to compare)
                    return MyFunctions.searchFunction(events, this.search, 'event_title');
                }


                // if (this.filter) {
                //
                //     // create empty array to hold filtered values
                //     let filteredList = [];
                //
                //     // loop through each lex item to get to their icon_list
                //     events.forEach((item) => {
                //
                //         // collection_name
                //         if (item.collection_name.toLowerCase() === this.filter.toLowerCase()) {
                //             filteredList.push(item)
                //         }
                //
                //     });
                //
                //     // if there is also a search value and filter value check search against filteredList array
                //     // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                //     if (this.search.length > 0) {
                //
                //         // check if items term include search values
                //         return filteredList.filter(obj => {
                //             return obj.event_title.toLowerCase().includes(this.search.toLowerCase());
                //         });
                //         // return filterSearch;
                //     }
                //
                //     // return filteredList if no search value
                //     return filteredList
                //
                //
                // }


                // if (this.search.length > 0) {
                //     // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                //
                //     var result = events.filter(obj => {
                //         // return obj.term === this.search
                //         return obj.event_title.toLowerCase().includes(this.search.toLowerCase());
                //     });
                //
                //     // let newLex = lexis.find(x => x.term === this.search);
                //     return result;
                // }

                return events


            }
        }
    };
</script>

<style lang="scss">

    .text-title {
        font-size: 1rem;
        font-weight: 500;
        letter-spacing: 0.0125em;
    }

    .event_title {
        font-size: 2rem;
        font-weight: 500;
        letter-spacing: 0.0125em;
    }

    .subtitle {
        color: gray;
        font-weight: normal;
        /*border-bottom: 1px solid gray;*/
    }


    .items-bottom {
        position: absolute;
        bottom: 0;
        right: 0;
        min-height: 50px;
        display: block;
    }

    .paddingFive {
        padding-top: 5px;
    }



    .quote {
        font-size: 1rem;
        line-height: 1.2rem;
        font-family: "Times New Roman", serif;
    }

    .author {
        text-align: right;
        font-size: .8rem;
        padding-top: 10px;
    }

    .author_source {
        padding-top: 10px;
        font-size: 10px;
    }




</style>


<!--    .active-->
<!--        background-color: #cccccc-->

<!--        .test-->
<!--            padding-top: 20px-->
<!--            padding-left: 20px-->

<!--        .page-bar-->
<!--            background-color: #ffffff-->

<!--        .title-->
<!--            font-size: 1.15rem !important-->
<!--            margin: auto-->

<!--            &:focus-->
<!--                outline: none-->

<!--        .full-width-banner-->
<!--            width: 100%-->
<!--            padding-bottom: 20px-->

<!--        .text-white-->
<!--            min-height: 320px-->

<!--        .banner-margin-->
<!--            margin-left: 15px-->