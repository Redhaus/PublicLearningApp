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
        </div>

        <div class="col-4" v-for="event in events_list" :key="event.id">
            <q-card
                    :class="{ active: event_id_list === event.id }"
                    bordered
                    @click="eventAction(event.id)"
            >
                <q-card-section>
                    <h4>{{ event.event_title }}</h4>
                    <p>{{ event.collection_event }}</p>
                    <p>{{ event.collection_name }}</p>
                </q-card-section>
            </q-card>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                event_id_list: 0,
                search: ''
            };
        },

        methods: {

            clearSearch() {
                this.search = "";
            },
            eventAction(event) {



                if (this.event_id_list === event) {
                    this.$store.dispatch("setSelectedEvent", event);
                    this.event_id_list = '';
                } else {
                    this.$store.dispatch("setSelectedEvent", event);
                    this.event_id_list = event;
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
            this.$store.dispatch("fetchEvents");
            this.event_id_list = this.$store.getters["getSelectedEvent"];
        },

        computed: {


            events_list() {

                let events = this.$store.getters["getEvents"];
                console.log(this.search);

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

<style lang="sass" scoped>


    .active
        background-color: #cccccc

        .test
            padding-top: 20px
            padding-left: 20px

        .page-bar
            background-color: #ffffff

        .title
            font-size: 1.15rem !important
            margin: auto

            &:focus
                outline: none

        .full-width-banner
            width: 100%
            padding-bottom: 20px

        .text-white
            min-height: 320px

        .banner-margin
            margin-left: 15px

</style>
