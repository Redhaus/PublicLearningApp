<template>

    <q-tabs
                    v-model="tab"
                    dense
                    inline-label
                    class="text-grey"
                    no-caps>
                <q-tab @click="clearFilter()" name="all" icon="explore" label="All"/>
                <q-tab @click="filterLexis('device')" name="device" icon="explore" label="Device"/>
                <q-tab @click="filterLexis('essential')" name="essential" icon="stars" label="Essential"/>
                <q-tab @click="filterLexis('common')" name="common" icon="language" label="Common"/>
                <q-tab @click="filterLexis('concept')" name="concept" icon="lightbulb" label="Concept"/>
                <q-tab @click="filterLexis('person')" name="person" icon="account_box" label="Person"/>

            </q-tabs>

    
</template>

<script>
    export default {
        name: "lexis_filter",

        data(){
            return{
                tab: 'all',
                filter: ''
            }
        },

        methods: {
            //sets lexis filter data var
            filterLexis(_filter) {
                this.filter = _filter;
                this.$emit('filterTerm', this.filter);
            },

            clearFilter() {
                this.filter = '';
                this.$emit('filterTerm', this.filter);
            },

        },



    }
</script>

<style scoped>

</style>