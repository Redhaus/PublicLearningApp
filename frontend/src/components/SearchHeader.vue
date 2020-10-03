<template>


    <q-banner elevated rounded inline-actions class="page-bar shadow-3">
        <div class="row">
            <div class="col-8 title" tabindex="0">
                <div>{{name}}</div>
            </div>

            <div class="col-4" tabindex="0">
                <q-input v-model="search" @input="searchTerm" :label="searchName" class="q-ml-md">
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

</style>