<template>


    <q-banner elevated rounded inline-actions class="page-bar">
                <div class="row">

                    <div class="col-3 title" tabindex="0" >
                        <div>{{pageName}}</div>
                    </div>

                    <div class="col-4 title offset-1" tabindex="0" style="padding: 5px 0 5px 0">
                        <q-select  bg-color="white" dense options-dense  filled v-model="class_selection_filter" @input="classFilter" :options="class_options_filter"
                                  :label="filterName">

<!--                            <template v-if="class_selection_filter" v-slot:append>-->
<!--          <q-icon name="cancel" @click.stop="clearFilter" class="cursor-pointer" />-->
<!--        </template>-->


                        </q-select>
                    </div>







                    <div class="col-3 offset-1" tabindex="0" style="padding: 5px 0 5px 0">

                       <q-input color="black"  bg-color="white" filled dense   v-model="search" @input="searchTerm" label="Search" class="q-ml-md">

<!--                        <q-input v-model="search" @input="searchTerm" label="Search Lessons" class="q-ml-md">-->
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
        name: "LessonSearchHeader.vue",

        props: {
            class_options_filter: Array,
            pageName: String,
            filterName: String
        },

        data() {
            return {
                search: '',
                class_selection_filter: {
                    label: 'All',
                    value: ''
                },

                // clear_filter: {
                //     label: 'All',
                //     value: ''
                // },

            }
        },

        methods: {

            searchTerm() {
                // pass emit event to parent component and pass data changed
                this.$emit('searchTerm', this.search);
            },

            // clearFilter() {
            //     // pass emit event to parent component and pass data changed
            //     this.class_selection_filter = null;
            //     this.$emit('classFilter', this.clear_filter);
            // },

            classFilter() {
                // pass emit event to parent component and pass data changed
                this.$emit('classFilter', this.class_selection_filter);
            },

            // this clears search field
            clearSearch() {
                this.search = "";
                this.$emit('searchTerm', this.search);
            },

        }

    }
</script>

<style scoped>

</style>