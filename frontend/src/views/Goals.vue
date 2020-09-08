<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >

        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">
                    <div class="col-8 title" tabindex="0">
                        <div>Goals</div>
                    </div>

                    <div class="col-4" tabindex="0">


                        <q-input v-model="search" label="Search Goals" class="q-ml-md">
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

        <div class="col-4" v-for="goal in goal_list" :key="goal.id">
            <q-card
                    :class="{ active: goal_id_list.includes(goal.id) }"
                    bordered
                    @click="eventAction(goal.id)">

                <q-card-section>
                    <h4>{{ goal.goal }}</h4>
                    <!--                    <p>{{ goal.collection_event }}</p>-->
                    <!--                    <p>{{ goal.collection_name }}</p>-->
                </q-card-section>
            </q-card>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                goal_id_list: [],
                search: ''
            };
        },

        methods: {

            clearSearch() {
                this.search = "";
            },
            eventAction(event) {

                // this.$store.dispatch("setSelectedEvent", event);
                // this.goal_id_list = event;

                // if (this.goal_id_list === event) {
                //     this.goal_id_list = this.goal_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.goal_id_list.push(event);
                // }


                // if (this.goal_id_list.includes(event)) {
                //     this.goal_id_list = this.goal_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.goal_id_list.push(event);
                // }


                if (this.goal_id_list.includes(event)) {
                    console.log('REMOVE');
                    // this.$store.dispatch("setSelectedLexis", event);

                    this.goal_id_list = this.goal_id_list.filter(function (item) {
                        return item !== event;
                    });
                } else {
                    // this.$store.dispatch("setSelectedLexis", event);

                    console.log('ADD');
                    this.goal_id_list.push(event);
                }


            },


        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            this.$store.dispatch("fetchGoals");
            this.goal_id_list = this.$store.getters["getSelectedGoals"];
        },

        computed: {


            goal_list() {

                let goals = this.$store.getters["getGoals"];
                console.log(this.search);

                if (this.search.length > 0) {
                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))

                    var result = goals.filter(obj => {
                        // return obj.term === this.search
                        return obj.goal.toLowerCase().includes(this.search.toLowerCase());
                    });

                    // let newLex = lexis.find(x => x.term === this.search);
                    return result;
                }

                return goals


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
