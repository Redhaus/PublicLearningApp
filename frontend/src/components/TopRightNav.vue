<template>

    <div class="q-gutter-sm row items-center no-wrap">
        <!--        <q-btn round dense flat color="grey-8" icon="video_call" v-if="$q.screen.gt.sm">-->
        <!--            <q-tooltip>Create a video or post</q-tooltip>-->
        <!--        </q-btn>-->

        <q-btn @click="logout"
                dense flat color="grey-8"
               label="Logout"
        />


        <q-btn @click="navSwitch('/classes')"
               round dense flat color="grey-8"
               icon="group_add"
               v-if="$q.screen.gt.sm"

               v-tooltip.left="{
                  content: 'Create New Class',
                  classes: ['info'],
                  targetClasses: ['it-has-a-tooltip'],
                  offset: 5,
                  delay: {
                    show: 500,
                    hide: 300,
                  },
                }"

        >
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
        <q-btn round flat  @click="navSwitch('/profile')">
            <q-avatar size="26px">
                <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
<!--            <q-tooltip>Account</q-tooltip>-->
        </q-btn>
    </div>

</template>

<script>
    export default {
        name: "SideNav",

        methods: {

            logout(){
                this.$store.dispatch("signoutFunction")
            },

            navSwitch(path) {
                // const path = '/classes';
                if (this.$route.path !== path) this.$router.push(path);
            }

        }
    }

</script>