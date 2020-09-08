<template>
    <!--<q-scroll-area >-->

    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >
        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Readings</div>
                    </div>

                    <div class="col-4" tabindex="0">
                        <q-input v-model="search" label="Search Readings" class="q-ml-md">
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

               <div v-if="reading_list.length > 0">

                <masonry :cols="3" :gutter="20">
                    <div v-for="book in reading_list" :key="book.id" class="bottom-padding">
                        <q-card
                                 :class="{ active: book_id_list === book.id }"
                                bordered
                                @click="eventAction(book.id)"
                        >
                            <q-card-section>
                                <h4>{{ book.title_major }}</h4>

                                <p>Author: {{book.author_first_name}} </p>
                                <p>Level: {{book.level_ability}} </p>
                                <p>Type: {{book.reading_category.category_name}} | Pages: {{book.page_count}}</p>

                            </q-card-section>
                        </q-card>
                    </div>
                </masonry>
                   </div>
                    <div v-else>No Readings Available</div>

            </div>

            <div v-else>Please select an Event</div>


        </div>

        <div style="height: 50px"/>
    </div>
</template>


<script>
    export default {
        data() {
            return {
                lorem:
                    "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea.",
                book_id_list: [],
                search: ""
            };
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');
            this.$store.dispatch("fetchReadings");
            this.book_id_list = this.$store.getters["getSelectedReading"];

        },

        computed: {

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },


            reading_list() {
                let readings = this.$store.getters["getReadings"];

                console.log('SEARCH', this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))
                    var result = readings.filter(obj => {
                        // return obj.term === this.search
                        return obj.title_major.toLowerCase().includes(this.search.toLowerCase());
                    });
                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }

                return readings;
            }
        },

        methods: {
            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                  if (this.book_id_list === event) {
                    this.$store.dispatch("setSelectedReading", event);
                    this.book_id_list = '';
                } else {
                    this.$store.dispatch("setSelectedReading", event);
                    this.book_id_list = event;
                }




                // if (this.book_id_list.includes(event)) {
                //     this.book_id_list = this.book_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.book_id_list.push(event);
                // }
            }
        }
    };
</script>

<style lang="scss" scoped>

       .active {
        background-color: #cccccc;
    }



</style>
