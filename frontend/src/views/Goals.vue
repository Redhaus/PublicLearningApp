<template>
    <div
            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "
    >

        <div class="col-12">
            <SearchHeader name="Goals" @searchTerm="search = $event"/>

        </div>

<!-- <div v-if="is_new && !is_editing" style="width: 100%">-->


        <!--create a card for every category-->
        <div style="width: 100%">
            <masonry :cols="3" :gutter="20">

                <q-expansion-item v-for="cat in goal_categories" :key="cat.id"
                                  class="accordion-header shadow-3"
                                  :label="cat.standard_type">
<!--                    <q-card>-->

<!--                        <q-card-section>-->
<!--                            <div class="text-h6">{{ cat.standard_type }}</div>-->
<!--                        </q-card-section>-->
<!--                    </q-card>-->

                    <div class="col-4" v-for="goal in goal_list" :key="goal.id">

                        <q-card

                                class="cardHandle shadow-1"
                                :class="{ active: selected_list.includes(goal.id) }"
                                bordered
                                @click="eventAction(goal.id)"
                                v-if="cat.standard_type === goal.standard_type.standard_type"
                        >

                            <q-card-section class="row">
                                <div class="col-10"><p class="goal-text"> {{ goal.goal }}</p></div>
                                <q-btn class="col-2 full-screen-btn" @click.stop="popupContent(goal)" flat
                                       color="grey" icon="o_open_in_new"/>
                            </q-card-section>




                        </q-card>
                    </div>
                </q-expansion-item>


            </masonry>

            <q-dialog v-model="icon">
                <q-card style="width: 60%">
                    <q-card-section class="row items-center q-pb-none">
                        <div class="text-h6">{{dialog.goal}}</div>
                        <q-space/>
                        <q-btn icon="close" flat round dense v-close-popup/>
                    </q-card-section>

                    <q-card-section>
                        <p>Explanation:</p>
                        <div v-html="dialog.explanation"></div>
                    </q-card-section>
                    <q-card-section>
                        <p>Video:</p>

                        <q-video
                                v-if="dialog.video"
                                :ratio="16/9"
                                :src="dialog.video"
                        />
                    </q-card-section>
                </q-card>
            </q-dialog>
        </div>

<!--                </div>-->

<!--         <div v-else>Please create a new lesson on dashboard</div>-->


    </div>
</template>
<script>
    import SearchHeader from "../components/SearchHeader";

    export default {
        components: {
            SearchHeader,
        },
        data() {
            return {
                // goal_id_list: [],
                search: '',
                goal_categories: [],
                icon: false,
                dialog: {
                    goal: '',
                    explanation: '',
                    video: '',
                }
            };
        },

        methods: {

            // this is the dialog for lexis preview
            popupContent(goal) {

                this.icon = true;
                this.dialog = {
                    goal: goal.goal,
                    explanation: goal.explanation,
                    video: goal.video_link
                }
            },


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

                this.$store.dispatch("setSelectedGoals", event);

                // if (this.goal_id_list.includes(event)) {
                //     // console.log('REMOVE');
                //     this.$store.dispatch("setSelectedGoals", event);
                //
                //     this.goal_id_list = this.goal_id_list.filter(function (item) {
                //         return item !== event;
                //     });
                // } else {
                //     this.$store.dispatch("setSelectedGoals", event);
                //
                //     // console.log('ADD');
                //     this.goal_id_list.push(event);
                // }


            },


        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            this.$store.dispatch("fetchGoals");
            // this.goal_id_list = this.$store.getters["getSelectedGoals"];
            this.goal_categories = this.$store.getters["getGoalCategories"];


        },

        computed: {

            selected_list() {
                return this.$store.getters["getSelectedGoals"];
            },


            goal_list() {

                let goals = this.$store.getters["getGoals"];
                // console.log(this.search);

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

<style lang="scss" >

    .accordion-header:hover{
        background-color: #eee;
    }


    .accordion-header > .q-hoverable:hover{
        /*border-radius: 10px !important;*/
        background-color: #eee;
                /*padding: 10px 0 10px 0;*/

    }


    .accordion-header{
        background-color: white;
        border-radius: 10px;
        margin-top: 10px;
        padding: 10px 0 10px 0;

    }

    .full-screen-btn.q-btn__wrapper {
        padding: 0 !important;
        min-height: 0 !important;

    }

    p {
        margin-bottom: 0px !important;
    }

    /*.active*/
    /*    background-color: #cccccc*/

    /*    .test*/
    /*        padding-top: 20px*/
    /*        padding-left: 20px*/

    /*    .page-bar*/
    /*        background-color: #ffffff*/

    /*    .title*/
    /*        font-size: 1.15rem !important*/
    /*        margin: auto*/

    /*        &:focus*/
    /*            outline: none*/

    /*    .full-width-banner*/
    /*        width: 100%*/
    /*        padding-bottom: 20px*/

    /*    .text-white*/
    /*        min-height: 320px*/

    /*    .banner-margin*/
    /*        margin-left: 15px*/

</style>


<!--<iframe width="560" height="315" src="" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->








<!--WORKING-->















<!--<template>-->
<!--    <div-->
<!--            class="test fit row wrap justify-start items-start content-start q-col-gutter-md "-->
<!--    >-->

<!--        <div class="col-12">-->
<!--            <SearchHeader name="Goals" @searchTerm="search = $event"/>-->

<!--        </div>-->

<!--&lt;!&ndash; <div v-if="is_new && !is_editing" style="width: 100%">&ndash;&gt;-->


<!--        &lt;!&ndash;create a card for every category&ndash;&gt;-->
<!--        <div style="width: 100%">-->
<!--            <masonry :cols="3" :gutter="20">-->

<!--                <div v-for="cat in goal_categories" :key="cat.id" class="bottom-padding">-->
<!--                    <q-card>-->

<!--                        <q-card-section>-->
<!--                            <div class="text-h6">{{ cat.standard_type }}</div>-->
<!--                        </q-card-section>-->
<!--                    </q-card>-->

<!--                    <div class="col-4" v-for="goal in goal_list" :key="goal.id">-->

<!--                        <q-card-->
<!--                                class="cardHandle"-->
<!--                                :class="{ active: selected_list.includes(goal.id) }"-->
<!--                                bordered-->
<!--                                @click="eventAction(goal.id)"-->
<!--                                v-if="cat.standard_type === goal.standard_type.standard_type"-->
<!--                        >-->

<!--                            <q-card-section class="row">-->
<!--                                <div class="col-10"><p class="goal-text"> {{ goal.goal }}</p></div>-->
<!--                                <q-btn class="col-2 full-screen-btn" @click.stop="popupContent(goal)" flat-->
<!--                                       color="grey" icon="o_open_in_new"/>-->
<!--                            </q-card-section>-->




<!--                        </q-card>-->
<!--                    </div>-->
<!--                </div>-->

<!--            </masonry>-->

<!--            <q-dialog v-model="icon">-->
<!--                <q-card style="width: 60%">-->
<!--                    <q-card-section class="row items-center q-pb-none">-->
<!--                        <div class="text-h6">{{dialog.goal}}</div>-->
<!--                        <q-space/>-->
<!--                        <q-btn icon="close" flat round dense v-close-popup/>-->
<!--                    </q-card-section>-->

<!--                    <q-card-section>-->
<!--                        <p>Explanation:</p>-->
<!--                        <div v-html="dialog.explanation"></div>-->
<!--                    </q-card-section>-->
<!--                    <q-card-section>-->
<!--                        <p>Video:</p>-->

<!--                        <q-video-->
<!--                                v-if="dialog.video"-->
<!--                                :ratio="16/9"-->
<!--                                :src="dialog.video"-->
<!--                        />-->
<!--                    </q-card-section>-->
<!--                </q-card>-->
<!--            </q-dialog>-->
<!--        </div>-->

<!--&lt;!&ndash;                </div>&ndash;&gt;-->

<!--&lt;!&ndash;         <div v-else>Please create a new lesson on dashboard</div>&ndash;&gt;-->


<!--    </div>-->
<!--</template>-->
<!--<script>-->
<!--    import SearchHeader from "../components/SearchHeader";-->

<!--    export default {-->
<!--        components: {-->
<!--            SearchHeader,-->
<!--        },-->
<!--        data() {-->
<!--            return {-->
<!--                // goal_id_list: [],-->
<!--                search: '',-->
<!--                goal_categories: [],-->
<!--                icon: false,-->
<!--                dialog: {-->
<!--                    goal: '',-->
<!--                    explanation: '',-->
<!--                    video: '',-->
<!--                }-->
<!--            };-->
<!--        },-->

<!--        methods: {-->

<!--            // this is the dialog for lexis preview-->
<!--            popupContent(goal) {-->

<!--                // console.log('VIDEO',goal.video_link);-->

<!--                this.icon = true;-->
<!--                this.dialog = {-->
<!--                    goal: goal.goal,-->
<!--                    explanation: goal.explanation,-->
<!--                    video: goal.video_link-->
<!--                }-->
<!--            },-->


<!--            clearSearch() {-->
<!--                this.search = "";-->
<!--            },-->
<!--            eventAction(event) {-->

<!--                // this.$store.dispatch("setSelectedEvent", event);-->
<!--                // this.goal_id_list = event;-->

<!--                // if (this.goal_id_list === event) {-->
<!--                //     this.goal_id_list = this.goal_id_list.filter(function (item) {-->
<!--                //         return item !== event;-->
<!--                //     });-->
<!--                // } else {-->
<!--                //     this.goal_id_list.push(event);-->
<!--                // }-->


<!--                // if (this.goal_id_list.includes(event)) {-->
<!--                //     this.goal_id_list = this.goal_id_list.filter(function (item) {-->
<!--                //         return item !== event;-->
<!--                //     });-->
<!--                // } else {-->
<!--                //     this.goal_id_list.push(event);-->
<!--                // }-->

<!--                this.$store.dispatch("setSelectedGoals", event);-->

<!--                // if (this.goal_id_list.includes(event)) {-->
<!--                //     // console.log('REMOVE');-->
<!--                //     this.$store.dispatch("setSelectedGoals", event);-->
<!--                //-->
<!--                //     this.goal_id_list = this.goal_id_list.filter(function (item) {-->
<!--                //         return item !== event;-->
<!--                //     });-->
<!--                // } else {-->
<!--                //     this.$store.dispatch("setSelectedGoals", event);-->
<!--                //-->
<!--                //     // console.log('ADD');-->
<!--                //     this.goal_id_list.push(event);-->
<!--                // }-->


<!--            },-->


<!--        },-->

<!--        created() {-->
<!--            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});-->
<!--            this.$store.dispatch("fetchGoals");-->
<!--            // this.goal_id_list = this.$store.getters["getSelectedGoals"];-->
<!--            this.goal_categories = this.$store.getters["getGoalCategories"];-->


<!--        },-->

<!--        computed: {-->

<!--            selected_list() {-->
<!--                return this.$store.getters["getSelectedGoals"];-->
<!--            },-->


<!--            goal_list() {-->

<!--                let goals = this.$store.getters["getGoals"];-->
<!--                // console.log(this.search);-->

<!--                if (this.search.length > 0) {-->
<!--                    // arr.filter(obj => obj.term.toLowerCase().includes(searchStr.toLowerCase()))-->

<!--                    var result = goals.filter(obj => {-->
<!--                        // return obj.term === this.search-->
<!--                        return obj.goal.toLowerCase().includes(this.search.toLowerCase());-->
<!--                    });-->

<!--                    // let newLex = lexis.find(x => x.term === this.search);-->
<!--                    return result;-->
<!--                }-->

<!--                return goals-->


<!--            }-->
<!--        }-->
<!--    };-->
<!--</script>-->

<!--<style lang="scss" scoped>-->


<!--    .full-screen-btn.q-btn__wrapper {-->
<!--        padding: 0 !important;-->
<!--        min-height: 0 !important;-->

<!--    }-->

<!--    p {-->
<!--        margin-bottom: 0px !important;-->
<!--    }-->

<!--    /*.active*/-->
<!--    /*    background-color: #cccccc*/-->

<!--    /*    .test*/-->
<!--    /*        padding-top: 20px*/-->
<!--    /*        padding-left: 20px*/-->

<!--    /*    .page-bar*/-->
<!--    /*        background-color: #ffffff*/-->

<!--    /*    .title*/-->
<!--    /*        font-size: 1.15rem !important*/-->
<!--    /*        margin: auto*/-->

<!--    /*        &:focus*/-->
<!--    /*            outline: none*/-->

<!--    /*    .full-width-banner*/-->
<!--    /*        width: 100%*/-->
<!--    /*        padding-bottom: 20px*/-->

<!--    /*    .text-white*/-->
<!--    /*        min-height: 320px*/-->

<!--    /*    .banner-margin*/-->
<!--    /*        margin-left: 15px*/-->

<!--</style>-->


<!--&lt;!&ndash;<iframe width="560" height="315" src="" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>&ndash;&gt;-->