<template>


    <q-banner elevated rounded inline-actions class="page-bar">
        <div class="row">
            <div class="col-9 title" tabindex="0">
                <div>{{name}}</div>
            </div>

            <div class="col-3" tabindex="0" style="padding: 5px 0 5px 0">
<!--                <q-input standout="bg-teal text-white" v-model="text" label="Custom standout" />-->
<!--standout="bg-secondary text-white"-->
<!--                <q-input color="black" bg-color="white"  filled  dense   v-model="search" @input="searchTerm" :label="searchName" class="q-ml-md">-->

                <q-input color="black" bg-color="white"  filled  dense   v-model="search" @input="searchTerm" label="Search" class="q-ml-md">
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


</template>


<script>
    export default {

        props: {
            name: String
        },

        data() {
            return {
                search: ''
            }
        },

        computed:{
            searchName(){
                return "Search " + this.name
            }
        },

        methods: {

            searchTerm() {

                // pass emit event to parent component and pass data changed
                this.$emit('searchTerm', this.search);


            },

            // this clears search field
            clearSearch() {
                this.search = "";
                this.$emit('searchTerm', this.search);
            },

        }


    }

</script>


<style>

    .q-field--standout .q-field__control {
    /*padding: 0 12px;*/
    /*background: rgba(0, 0, 0, 0.05);*/
    /*border-radius: 4px;*/
    transition: none !important;
}

        .q-field--standout.q-field--focused .q-field__control {
    box-shadow: none !important;
}


    .q-field--filled .q-field__control {
    padding: 0 12px;
    background: rgba(0, 0, 0, 0.03);
    border-radius: 4px !important;
}

/*    .q-field__control {*/
/*    height: 45px !important;*/
/*}*/



</style>