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

        <!--create a card for every category-->
        <div style="width: 100%">
            <masonry :cols="3" :gutter="20">

                <div v-for="cat in goal_categories" :key="cat.id" class="bottom-padding">
                    <q-card>

                        <q-card-section>
                            <div class="text-h6">{{ cat.standard_type }}</div>
                        </q-card-section>
                    </q-card>

                    <!--                        <q-separator/>-->

                    <!--                        <q-card-section>-->

                    <div class="col-4" v-for="goal in goal_list" :key="goal.id">

                        <q-card
                                class="cardHandle"
                                :class="{ active: selected_list.includes(goal.id) }"
                                bordered
                                @click="eventAction(goal.id)"
                                v-if="cat.standard_type === goal.standard_type.standard_type"
                        >

                            <q-card-section class="row">
                                <div class="col-10"><p class="goal-text"> {{ goal.goal }}</p></div>
                                <q-btn class="col-2 full-screen-btn" @click.stop="popupContent(goal)" flat
                                       color="grey-5" icon="aspect_ratio"/>

                                <!--                    <p>{{ goal.collection_event }}</p>-->
                                <!--                    <p>{{ goal.collection_name }}</p>-->
                            </q-card-section>
                        </q-card>

                        <!--                                <div v-if="cat.standard_type === goal.standard_type.standard_type">-->
                        <!--                                    {{goal.goal}}-->
                        <!--                                </div>-->
                    </div>
                    <!--                        </q-card-section>-->
                    <!--                    </q-card>-->
                </div>

            </masonry>

            <q-dialog v-model="icon" >
                <q-card style="width: 60%">
                    <q-card-section class="row items-center q-pb-none">
                        <div class="text-h6">{{dialog.goal}} </div>
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


        <!--        <div class="col-4" v-for="goal in goal_list" :key="goal.id">-->
        <!--            <q-card-->
        <!--                    :class="{ active: goal_id_list.includes(goal.id) }"-->
        <!--                    bordered-->
        <!--                    @click="eventAction(goal.id)">-->

        <!--                <q-card-section>-->
        <!--                    <h4>{{ goal.goal }}</h4>-->
        <!--                    &lt;!&ndash;                    <p>{{ goal.collection_event }}</p>&ndash;&gt;-->
        <!--                    &lt;!&ndash;                    <p>{{ goal.collection_name }}</p>&ndash;&gt;-->
        <!--                </q-card-section>-->
        <!--            </q-card>-->
        <!--        </div>-->
    </div>
</template>
<script>
    export default {
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

                // console.log('VIDEO',goal.video_link);

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

            selected_list(){
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

<style lang="scss" scoped>


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