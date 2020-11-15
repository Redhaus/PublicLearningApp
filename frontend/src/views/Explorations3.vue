<template>
    <!--<q-scroll-area >-->

    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md">

        <div style="width: 100%">
            <NextBtn class="float-right" section_name="Lexis" :selected_item="selected_item"/>
        </div>


        <div class="col-12">
            <SearchHeader name="Explorations" @searchTerm="search = $event"/>
        </div>


        <div style="width: 100%">

            <div v-if="selected_event">


                <div class="exploration page-bar rounded-borders">
                    <q-splitter
                            v-model="splitterModel"
                    >

                        <template v-slot:before>
                            <q-tabs
                                    v-model="tab"
                                    vertical
                                    no-caps
                            >
                                <q-tab content-class="content-right" v-for="cat in reading_categories" :key="cat.id"
                                       :name="cat.category_name" :label="cat.category_name"
                                       @click="filterLexis(cat.category_name)"/>

                            </q-tabs>
                        </template>

                        <template v-slot:after>


                            <q-tab-panels
                                    v-model="tab"
                                    animated
                                    swipeable
                                    vertical
                                    transition-prev="jump-up"
                                    transition-next="jump-up"
                            >
                                <q-tab-panel v-for="cat in reading_categories" :key="cat.id" :name="cat.category_name">
                                    <div class="text-h4 q-mb-md">{{cat.category_name}}</div>

                                    <div style="width: 100%">

                                        <!--                                    <div v-if="selected_event">-->

                                        <div v-if="exploration_list.length > 0">

                                            <masonry :cols="3" :gutter="20">
                                                <div v-for="ex in exploration_list" :key="ex.id" class="bottom-padding">
                                                    <q-card
                                                            class="cardHandle"
                                                            :class="{ active: selected_list.includes(ex.id) }"
                                                            bordered
                                                            @click="eventAction(ex.id)"
                                                    >
                                                        <q-card-section>
                                                            <div class="text-title">{{ ex.title_minor }}</div>
                                                              <div class="ability">{{ex.reading_category.category_name}}</div>
                                                        </q-card-section>
                                                        <q-separator/>

                                                        <q-card-section>
                                                            <div v-html="short_overview(ex.excerpt)"></div>
                                                        </q-card-section>

                                                        <div class="btnContainer">
                                                            <q-separator/>
                                                            <q-card-actions >

                                                                <div  v-if="conceptChecker(ex.id)">
                                                                    <q-chip dense
                                                                            color="black" text-color="white"
                                                                            :label="selectedConceptTerm"/>
                                                                </div>


                                                                <div class="items-exploration">
                                                                <q-btn  @click.stop="dialogPopup(ex)" dense flat round
                                                                       color="grey" icon="o_open_in_new"/>
                                                                    </div>
                                                            </q-card-actions>
                                                        </div>


                                                    </q-card>
                                                </div>
                                            </masonry>

                                            <!-- DIALOG -->


                                        </div>

                                        <div class="selectEventNotification" v-else>No {{filter}} Explorations Available</div>


                                    </div>
                                </q-tab-panel>


                            </q-tab-panels>


                        </template>

                    </q-splitter>
                </div>

            </div>


            <div class="selectEventNotification" v-else>Please select an Event</div>
            <ExplorationsDialog ref="dialogExplorationComponent"
                                :conceptSelectHandler="conceptSelect"
                                :selected_list="selected_list"
                                :eventActionHandler="eventAction"/>
        </div>

        <div style="height: 50px"/>
    </div>
</template>
<script>

    import clip from "text-clipper";
    import SearchHeader from "../components/SearchHeader";
    import ExplorationsDialog from "../components/readings/furtherExplorationDialog";
    import NextBtn from "../components/NextBtn";

    export default {


        components: {
            SearchHeader,
            ExplorationsDialog,
            NextBtn
        },
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                // exploration_id_list: [],
                search: "",
                filter: '',
                reading_categories: [],
                tab: 'Poem',
                splitterModel: 20,
                selectedConceptTerm: '',
                selectedConceptList: []
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchExplorations");
            // this.exploration_id_list = this.$store.getters["getSelectedExplorations"];

            this.reading_categories = this.$store.getters["getReadingCategories"];
            this.filter = "Poem"


        },

        computed: {


            selected_item() {

                if (this.selected_list.length > 0) {
                    console.log('OFF');
                    return true;
                } else {
                    console.log('ON');
                    return false;
                }

            },

            selected_list() {
                return this.$store.getters["getSelectedExplorations"];
            },

            // this makes sure there is selected event before content is displayed
            selected_event() {
                return this.$store.getters["getSelectedEvent"];
            },

            exploration_list() {
                let explorations = this.$store.getters["getExplorations"];

                // console.log(this.search);


                // if there is a filter value run function to filter results
                if (this.filter) {

                    // create empty array to hold filtered values
                    let filteredList = [];

                    // loop through each lex item to get to their icon_list
                    explorations.forEach((item) => {


                        // console.log(item);
                        // console.log(item.reading_category.category_name)

                        // if matches add original item to filterList Array
                        if (item.reading_category.category_name.toLowerCase() === this.filter.toLowerCase()) {
                            filteredList.push(item)
                        }

                        // // loop through each icon list to see if icon matches filter
                        // item.reading_category..forEach(obj => {
                        //
                        //     // if matches add original item to filterList Array
                        //     if (obj.icons.toLowerCase() === this.filter.toLowerCase()) {
                        //         filteredList.push(item)
                        //     }
                        // })
                    });

                    // if there is also a search value and filter value check search against filteredList array
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    if (this.search.length > 0) {

                        // check if items term include search values
                        return filteredList.filter(obj => {
                            return obj.title_minor.toLowerCase().includes(this.search.toLowerCase());
                        });
                        // return filterSearch;
                    }

                    // return filteredList if no search value
                    return filteredList


                }
                //  end if filter statement


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


            // function to check if key concept is part of exploration
            conceptChecker(id){

                if (this.selectedConceptList.find( item => item.id === id )){
                    return true
                } else {
                    return false
                }
            },

            // processes the key concept term and adds words list to data for checker processing
            conceptSelect(term) {

                this.selectedConceptTerm = term;
                let list = [];
                let explorations = this.$store.getters["getExplorations"];

                explorations.forEach((item) => {
                    // loop through each icon list to see if icon matches filter
                    item.keywords.find((concept) => {
                        if (concept.value.toLowerCase() === term.toLowerCase()) {
                            list.push(item)
                        }
                    })
                });

                this.selectedConceptList = list;

            },

            dialogPopup(exploration) {
                // call child popup function
                this.$refs.dialogExplorationComponent.popupEx(exploration);
            },


            short_overview(html) {

                const clippedHtml = clip(html, 100, {html: true, maxLines: 5});
                // const clippedString = clip(string, 80);
                // console.log('HTMLTRIM', clippedHtml);
                return clippedHtml
            },


            // this clears filter when all is selected
            clearFilter() {
                this.filter = '';
            },


            //sets lexis filter data var
            filterLexis(_filter) {
                this.filter = _filter;
            },

            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                this.$store.dispatch("setSelectedExplorations", event);

                // if (this.exploration_id_list.includes(event)) {
                //      this.$store.dispatch("setSelectedExplorations", event);
                //     this.exploration_id_list = this.exploration_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //      this.$store.dispatch("setSelectedExplorations", event);
                //     this.exploration_id_list.push(event);
                // }
            }
        }
    };
</script>

<style lang="scss">

    .items-exploration {
    position: absolute;
    bottom: 9px;
    right: 0;
        padding-right: 3px;
}

    .q-tab--active {
        /*background-color: #cccccc;*/
        color: #ffffff;
    }

    .content-right {
        text-align: right;
    }

    .active {
        background-color: #cccccc;
    }

    .exploration {
        background-color: #ffffff;
        margin-top: 20px;
    }

    .ability {
        font-size: .7rem;
    }

</style>


<!--<q-splitter-->
<!--      v-model="splitterModel"-->
<!--      style="height: 250px"-->
<!--    >-->

<!--      <template v-slot:before>-->
<!--        <q-tabs-->
<!--          v-model="tab"-->
<!--          vertical-->
<!--          class="text-teal"-->
<!--        >-->
<!--          <q-tab name="mails" icon="mail" label="Mails" />-->
<!--          <q-tab name="alarms" icon="alarm" label="Alarms" />-->
<!--          <q-tab name="movies" icon="movie" label="Movies" />-->
<!--        </q-tabs>-->
<!--      </template>-->

<!--      <template v-slot:after>-->
<!--        <q-tab-panels-->
<!--          v-model="tab"-->
<!--          animated-->
<!--          swipeable-->
<!--          vertical-->
<!--          transition-prev="jump-up"-->
<!--          transition-next="jump-up"-->
<!--        >-->
<!--          <q-tab-panel name="mails">-->
<!--            <div class="text-h4 q-mb-md">Mails</div>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--          </q-tab-panel>-->

<!--          <q-tab-panel name="alarms">-->
<!--            <div class="text-h4 q-mb-md">Alarms</div>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--          </q-tab-panel>-->

<!--          <q-tab-panel name="movies">-->
<!--            <div class="text-h4 q-mb-md">Movies</div>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis praesentium cumque magnam odio iure quidem, quod illum numquam possimus obcaecati commodi minima assumenda consectetur culpa fuga nulla ullam. In, libero.</p>-->
<!--          </q-tab-panel>-->
<!--        </q-tab-panels>-->
<!--      </template>-->

<!--    </q-splitter>-->