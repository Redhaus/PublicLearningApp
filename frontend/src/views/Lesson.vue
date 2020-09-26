<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >

        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">

                    <div class="col-8 title" tabindex="0">
                        <div>Lessons</div>
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

<!--            <q-tabs-->
<!--                    v-model="tab"-->
<!--                    dense-->
<!--                    inline-label-->
<!--                    class="text-grey"-->
<!--                    no-caps-->
<!--            >-->
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

        </div>

        <div style="width: 100%">
        <div v-if="lesson_list.length > 0">

               <masonry :cols="4" :gutter="20">

            <div v-for="lesson in lesson_list" :key="lesson.id">
                <q-card
                         class="cardHandle"
                        :class="{ active: lesson_id_list === lesson.id }"
                        bordered
                        @click="eventAction(lesson.id)">
                    <q-card-section>
                         <strong>{{lesson.lesson_title}}</strong>
                        <div v-for="(lex, index) in lesson.lexis" :key="index">
                            {{getLexis(lex)}}
                        </div>
<!--                        {{lexList(lesson.selections)}}-->

<!--                        <div class="text-title" v-for="(lex, index) in lexList(lesson.lesson_selections)" :key="index"> {{ getLexis(lex) }}</div>-->
                    </q-card-section>
<!--                    <q-separator/>-->
<!--                    <q-card-section>-->
<!--                        <p>{{ event.event_descriptor }}</p>-->
<!--                    </q-card-section>-->

                </q-card>
            </div>

               </masonry>

<!--            <button @click="saveLesson">Save</button>-->

        </div>


        <div v-else>No Lesson Available</div>

             </div>
        <button @click="saveLesson">Save</button>
<!--            <button @click="saveLesson">Save</button>-->

    </div>
</template>
<script>
    export default {
        data() {
            return {
                lesson_id_list: 0,
                search: '',
                filter: '',
                lexis: [],
                selections: {}

            };
        },

        methods: {

            // lexList(data){
            //     // var obj = JSON.parse(data);
            //     // console.log(obj);
            //     // return obj
            //
            //      return  data.selected_lexis.forEach(element => {
            //         console.log('RETURN', this.getLexis(element));
            //         return this.getLexis(element);
            //     });
            //
            //      // console.log('TERM', term)
            //
            //     // console.log('LEXLIST', data.selected_lexis);
            //     // this.getLexis(data.selected_lexis);
            //
            // },

            saveLesson(){

                console.log('SAVE LESSON CALLED');
                console.log('GET RETURN OF SELECTIONS',this.$store.getters["getSelections"] );

                // bypass getters
                console.log('DATA SELECTIONS',this.$store.state.lesson_store.lesson );


                // let payload = ;
                 this.$store.dispatch("postLesson", this.selections);

            },

            // this fetches the words based on id passed
             getLexis(id){

                console.log('GETLEXIS', id);

                 // console.log('ID', id);
                 // loop through items and return the item with the matching id
                 let lex = this.lexis.find(item => item.id === id);
                 // return lex.term;
                if(lex){
                    console.log('LEX', lex.term);
                    return lex.term
                }

            },

            // sets lexis filter data var
            filterEvent(_filter) {
                this.filter = _filter;
            },

            clearSearch() {
                this.search = "";
            },
            eventAction(event) {


                if (this.lesson_id_list === event) {
                    // this.$store.dispatch("setSelectedEvent", event);
                    this.lesson_id_list = '';
                } else {
                    // this.$store.dispatch("setSelectedEvent", event);
                    this.lesson_id_list = event;
                }
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
            // this.$store.dispatch("fetchEvents");
            // this.lexis_id_list = this.$store.getters["getSelectedEvent"];
            // this.$store.dispatch("fetchLexis");
            this.lexis = this.$store.getters["getLexis"];
            // console.log('SELECTIONS', this.selections);

            // console.log('GET RETURN OF SELECTIONS',this.$store.getters["getSelections"] );
            // console.log('GET RETURN OF CURRENTLESSON',this.$store.getters["getCurrentLesson"] );

            //
            //
            // console.log('CREATED LESSON CALLED FOR GET SELECTIONS');
            this.selections = this.$store.getters["getSelections"];
            //             console.log('AFTER GET SELECTIONS', this.selections);

        },



        computed: {




            lesson_list() {

                let lessons = this.$store.getters["getLessons"];
                // console.log(this.search);


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
                //
                //
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

                return lessons


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

