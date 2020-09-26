<template>

    <div class="q-pa-md">
        <div class="q-gutter-md row items-start">
            <q-input v-model="username" filled type="text" hint="username"/>

            <q-input v-model="password" filled :type="isPwd ? 'password' : 'text'" hint="Password with toggle">
                <template v-slot:append>
                    <q-icon
                            :name="isPwd ? 'visibility_off' : 'visibility'"
                            class="cursor-pointer"
                            @click="isPwd = !isPwd"
                    />
                </template>
            </q-input>
             <q-btn color="primary" label="Signin" @click.prevent="SigninData"/>
        </div>
    </div>

</template>

<script>
    export default {
        name: "Signin",
        data() {
            return {
                password: '',
                isPwd: true,
                username: '',

            }
        },
        methods:{
            SigninData(){
                console.log('SIGNIN DATA', {password: this.password, username: this.username});
                let data = {password: this.password, username: this.username};
                this.$store.dispatch("signinFunction", data)
            }
        }

    }
</script>

<style scoped>

</style>