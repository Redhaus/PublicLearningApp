<template>


          <q-header bordered class="bg-white text-grey-8 q-py-xs" height-hint="58">
            <q-toolbar>

                <q-btn flat no-caps no-wrap class="q-ml-xs" v-if="$q.screen.gt.xs">


                    <q-toolbar-title shrink class="text-weight-bold">

                    <LogoTemplate/>

                    </q-toolbar-title>
                </q-btn>

                <q-space/>
                <q-space/>

                <TopRightNavHome/>

            </q-toolbar>
        </q-header>
    
</template>

<script>
     import TopRightNavHome from "@/components/TopRightNavHome.vue";
    import LogoTemplate from "../components/LogoTemplate";

    export default {
       components: {
            TopRightNavHome,
            LogoTemplate
        },
        name: "HomePageHeader.vue"
    }
</script>

<style scoped>

</style>