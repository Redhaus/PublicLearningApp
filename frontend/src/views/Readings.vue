<template>
    <!--<q-scroll-area >-->

    <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">
        <div class="col-12">
            <SearchHeader name="Readings" @searchTerm="search = $event"/>
        </div>

        <div style="width: 100%">


            <div v-if="selected_event">

                <div v-if="reading_list.length > 0">

                    <masonry :cols="3" :gutter="20">
                        <div v-for="book in reading_list" :key="book.id" class="bottom-padding">
                            <q-card
                                    class="cardHandle"
                                    :class="{ active: selected_item === book.id }"
                                    bordered
                                    @click="eventAction(book.id)"
                            >
                                <q-card-section>
                                    <div class="text-title">{{ book.title_major }}</div>
                                    <div class="ability">{{ book.level_ability }}</div>
                                </q-card-section>

                                <q-separator/>

                                <q-card-section>

                                    <div v-html="short_overview(book.synopsis)"></div>
                                    <!--                                <p>Author: {{book.author_first_name}} </p>-->
                                    <!--                                <p>Level: {{book.level_ability}} </p>-->
                                    <!--                                <p>Type: {{book.reading_category.category_name}} | Pages: {{book.page_count}}</p>-->

                                </q-card-section>


                                <div class="btnContainer">
                                    <q-separator/>
                                    <q-card-actions class="items-bottom" align="right">
                                        <q-btn @click.stop="dialogPopup(book)" dense flat round
                                               color="grey" icon="o_open_in_new"/>
                                    </q-card-actions>
                                </div>



                                <!--                                <q-separator class="separator-bottom"/>-->
                                <!--                                <q-card-actions align="right">-->
                                <!--                                    <q-btn @click="eventDetail(event)" dense flat round color="gray"-->
                                <!--                                           icon="o_open_in_new"/>-->
                                <!--                                </q-card-actions>-->

                                <!--                                <q-separator/>-->
                                <!--                                <q-card-actions class="items-bottom" align="right">-->
                                <!--                                    <q-btn @click.stop="dialogPopup(lex)" dense flat round color="gray"-->
                                <!--                                           icon="o_open_in_new"/>-->
                                <!--                                </q-card-actions>-->


                            </q-card>
                        </div>
                    </masonry>

                       <!-- DIALOG -->
                    <PrimaryReadingDialog ref="dialogComponent" />

                </div>
                <div v-else>No Readings Available</div>

            </div>

            <div v-else>Please select an Event</div>


        </div>

        <div style="height: 50px"/>
    </div>
</template>


<script>
    import clip from "text-clipper";

    import SearchHeader from "../components/SearchHeader";
    import PrimaryReadingDialog from "../components/readings/primaryReadingDialog"

    export default {
        components: {
            SearchHeader,
            PrimaryReadingDialog
        },
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

            selected_item() {
                return this.$store.getters["getSelectedReading"];
            },

            // this makes sure there is selected event before content is displayed
            selected_event() {

                let selectedEvent = this.$store.getters["getSelectedEvent"];
                // console.log('SELECTED_EVENT, :', selectedEvent);
                return selectedEvent
            },


            reading_list() {
                let readings = this.$store.getters["getReadings"];

                // console.log('SEARCH', this.search);

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

              dialogPopup(reading) {
                // call child popup function
                this.$refs.dialogComponent.popupContent(reading);
            },


            short_overview(html) {

                const clippedHtml = clip(html, 100, {html: true, maxLines: 5});

                // const clippedString = clip(string, 80);

                // console.log('HTMLTRIM', clippedHtml);
                return clippedHtml
            },

            clearSearch() {
                this.search = "";
            },

            eventAction(event) {

                this.$store.dispatch("setSelectedReading", event);

                //   if (this.book_id_list === event) {
                //     this.$store.dispatch("setSelectedReading", event);
                //     this.book_id_list = '';
                // } else {
                //     this.$store.dispatch("setSelectedReading", event);
                //     this.book_id_list = event;
                // }


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

    .ability {
        font-size: .7rem;
    }

    .active {
        background-color: #cccccc;
    }


</style>