<template>

          <q-btn  @click.stop="nextSection('Readings')" dense flat round
                   :color="btnColor" icon="arrow_right_alt"/>


</template>

<script>


    export default {
        props: ['selected_item', 'section_name'],
        name: "NextBtn.vue",
        computed: {

            btnColor() {
                if (this.selected_item) {
                    return 'black'
                } else {
                    return 'grey'
                }
            },
        },

        methods:{


            nextSection() {
                 this.$router.push({name: this.section_name});
            },

        }
    }
</script>

<style scoped>



    .event .q-hoverable:hover > .q-focus-helper {
        background: currentColor;
        opacity: .15;
        border-radius: 20px !important;
    }

    .event .q-ripple {
        border-radius: 20px !important;
    }




</style>