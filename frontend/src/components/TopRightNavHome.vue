<template>

    <div class="q-gutter-sm row items-center no-wrap">
        <!--        <q-btn round dense flat color="grey-8" icon="video_call" v-if="$q.screen.gt.sm">-->
        <!--            <q-tooltip>Create a video or post</q-tooltip>-->
        <!--        </q-btn>-->
        <q-btn @click="navSwitch('/register')"
                dense flat color="grey-8"
               label="Register"
        >

<!--                           v-if="$q.screen.gt.sm"-->

<!--            <q-tooltip>Create New Class</q-tooltip>-->
        </q-btn>
        <!--        <q-btn round dense flat color="grey-8" icon="message" v-if="$q.screen.gt.sm">-->
        <!--            <q-tooltip>Messages</q-tooltip>-->
        <!--        </q-btn>-->
        <!--        <q-btn round dense flat color="grey-8" icon="notifications">-->
        <!--            <q-badge color="red" text-color="white" floating>-->
        <!--                2-->
        <!--            </q-badge>-->
        <!--            <q-tooltip>Notifications</q-tooltip>-->
        <!--        </q-btn>-->
        <q-btn @click="navSwitch('/signin')"
                dense flat color="grey-8"
               label="Signin"



        >

        </q-btn>
    </div>

</template>

<script>
    export default {
        name: "SideNav",

        methods: {

            navSwitch(path) {
                // const path = '/classes';
                if (this.$route.path !== path) this.$router.push(path);
            }

        }
    }

</script>