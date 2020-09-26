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

            <q-tabs
                    v-model="tab"
                    dense
                    inline-label
                    class="text-grey"
            >
                <q-tab @click="clearFilter()" name="all" icon="explore" label="all"/>
                <q-tab v-for="cat in reading_categories" :key="cat.id" @click="filterLexis(cat.category_name)" :name="cat.category_name" icon="explore" :label="cat.category_name"/>

<!--&lt;!&ndash;                <q-tab @click="filterLexis('device')" name="device" icon="explore" label="device"/>&ndash;&gt;-->
<!--&lt;!&ndash;                <q-tab @click="filterLexis('essential')" name="essential" icon="stars" label="essential"/>&ndash;&gt;-->
<!--&lt;!&ndash;                <q-tab @click="filterLexis('common')" name="common" icon="language" label="common"/>&ndash;&gt;-->
<!--&lt;!&ndash;                <q-tab @click="filterLexis('concept')" name="concept" icon="lightbulb" label="concept"/>&ndash;&gt;-->
<!--&lt;!&ndash;                <q-tab @click="filterLexis('person')" name="person" icon="account_box" label="person"/>&ndash;&gt;-->

            </q-tabs>





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
                    <div v-else>No {{filter}} Explorations Available</div>

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
                search: "",
                filter: '',
                reading_categories: [],
                tab: 'all',
                splitterModel: 20
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchExplorations");
            this.exploration_id_list = this.$store.getters["getSelectedExplorations"];

            this.reading_categories = this.$store.getters["getReadingCategories"];


        },

        computed: {

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                // console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
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