<template>

    <div class="q-gutter-sm row items-center no-wrap">
        <q-btn round dense flat color="grey-8" icon="video_call" v-if="$q.screen.gt.sm">
            <q-tooltip>Create a video or post</q-tooltip>
        </q-btn>
        <q-btn @click="navSwitch" round dense flat color="grey-8" icon="apps" v-if="$q.screen.gt.sm">
            <q-tooltip>Apps</q-tooltip>
        </q-btn>
        <q-btn round dense flat color="grey-8" icon="message" v-if="$q.screen.gt.sm">
            <q-tooltip>Messages</q-tooltip>
        </q-btn>
        <q-btn round dense flat color="grey-8" icon="notifications">
            <q-badge color="red" text-color="white" floating>
                2
            </q-badge>
            <q-tooltip>Notifications</q-tooltip>
        </q-btn>
        <q-btn round flat>
            <q-avatar size="26px">
                <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
            <q-tooltip>Account</q-tooltip>
        </q-btn>
    </div>

</template>

<script>
    export default {
        name: "SideNav",

        methods: {

            navSwitch() {
                const path = '/classes';
                if (this.$route.path !== path) this.$router.push(path);
            }

        }
    }

</script>