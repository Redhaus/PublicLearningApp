<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >

        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Events</div>
                    </div>

                    <div class="col-4" tabindex="0">


                        <q-input v-model="search" label="Search Events" class="q-ml-md">
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
                    no-caps
            >
                <q-tab @click="filterEvent('')" name="all" label="All"/>

                <q-tab @click="filterEvent('A Survey in Western Literature I')" name="aswl1"
                       label="Western Literature I"/>
                <q-tab @click="filterEvent('A Survey in Western Literature II')" name="aswl2"
                       label="Western Literature II"/>
                <q-tab @click="filterEvent('A Survey in European Literature I')" name="asel1"
                       label="European Literature I"/>
                <q-tab @click="filterEvent('A Survey in American Literature I')" name="asal1"
                       label="American Literature I"/>

            </q-tabs>

        </div>

        <div style="width: 100%">
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

                </q-card>
            </div>

               </masonry>

        </div>


        <div v-else>No Events Available</div>

             </div>

    </div>
</template>
<script>
    export default {
        data() {
            return {
                event_id_list: 0,
                search: '',
                tab: 'all',
                filter: ''
            };
        },

        methods: {

            //sets lexis filter data var
            filterEvent(_filter) {
                this.filter = _filter;
            },

            clearSearch() {
                this.search = "";
            },
            eventAction(event) {

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
        },

        computed: {

            selected_item(){
                return this.$store.getters["getSelectedEvent"];
            },


            events_list() {

                let events = this.$store.getters["getEvents"];
                // console.log(this.search);


                if (this.filter) {

                    // create empty array to hold filtered values
                    let filteredList = [];

                    // loop through each lex item to get to their icon_list
                    events.forEach((item) => {

                        // collection_name
                        if (item.collection_name.toLowerCase() === this.filter.toLowerCase()) {
                            filteredList.push(item)
                        }

                    });

                    // if there is also a search value and filter value check search against filteredList array
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    if (this.search.length > 0) {

                        // check if items term include search values
                        return filteredList.filter(obj => {
                            return obj.event_title.toLowerCase().includes(this.search.toLowerCase());
                        });
                        // return filterSearch;
                    }

                    // return filteredList if no search value
                    return filteredList


                }


                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = events.filter(obj => {
                        // return obj.term === this.search
                        return obj.event_title.toLowerCase().includes(this.search.toLowerCase());
                    });

                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }

                return events


            }
        }
    };
</script>

<style lang="scss" >

    .text-title {
    font-size: 1rem;
    font-weight: 500;
    letter-spacing: 0.0125em;
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