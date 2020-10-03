<template>


    <q-banner elevated rounded inline-actions class="page-bar shadow-3">
                <div class="row">

                    <div class="col-3 title" tabindex="0">
                        <div>Lessons</div>
                    </div>

                    <div class="col-5 title" tabindex="0">
                        <q-select v-model="class_selection_filter" @input="classFilter" :options="class_options_filter"
                                  label="Select Class"/>
                    </div>

                    <div class="col-4" tabindex="0">


                        <q-input v-model="search" @input="searchTerm" label="Search Lessons" class="q-ml-md">
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
            class_options_filter: Array
        },

        data() {
            return {
                search: '',
                class_selection_filter: {
                    label: 'All',
                    value: 'all'
                },

            }
        },

        methods: {

            searchTerm() {
                // pass emit event to parent component and pass data changed
                this.$emit('searchTerm', this.search);
            },

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