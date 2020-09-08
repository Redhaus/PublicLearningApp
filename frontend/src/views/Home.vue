<template>



       <div class="test fit row wrap justify-start items-start content-start q-col-gutter-md ">


        <div class="col-12">
            <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="title">Dashboard</div>
            </q-banner>
        </div>





            <div class="col-4" v-for="i in 5" :key="i" >

                <q-card
                    class=""
                    style="background: white"
                    bordered>

                <q-card-section>
                    <h4>Title</h4>
                    <p>{{lorem}}</p>
                </q-card-section>

            </q-card>


            </div>

    </div>
</template>
<script>


    export default {
        data() {
            return {
              lorem : "Lorem ipsum dolor sit amet, sale audiam viderer ei cum, munere labitur expetenda sed ad, mea albucius prodesset no. Ne interesset referrentur qui, simul nusquam ne eam, id est appetere legendos. Cu usu cibo legere ullamcorper, ut decore assueverit qui, his iusto lucilius singulis id. Mazim noster usu ei. Sonet voluptua eu mea."
            }
        },

        created() {
            // this.$store.dispatch('fetchEvents', {endpoint: this.slug});
            // this.$store.dispatch('fetchEvents');

        },

        computed: {
            // events_list() {
            //     return this.$store.getters['getEvents'];
            // }
        }
    }

</script>


<style lang="sass" scoped>








    /*////*/








    .test
        padding-top: 20px
        padding-left: 20px

    .page-bar
        background-color: #ffffff

    .title
        font-size: 1.15rem !important

    .full-width-banner
        width: 100%
        padding-bottom: 20px
    .text-white
        min-height: 320px

    .banner-margin
         margin-left: 15px
    /*.my-card*/
        /*width: 48%*/
</style>