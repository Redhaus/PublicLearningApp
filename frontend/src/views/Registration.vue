<template>
    <q-layout view="hHh lpR lFf" class="bg-grey-2">

        <HomePageHeader/>

        <q-page-container>
            <q-page
                    class="window-height window-width row justify-center items-center"
                    style="background: #f7f7f7"
            >

                <!--                    style="background: linear-gradient(#8274C5, #5A4A9F);"-->


                <div class="column q-pa-sm">
                    <!--            <button @click="logout">logout</button>-->
                    <div class="row">
                        <q-card class="" style="width:400px;height:485px;">
                            <q-card-section
                                    style="background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);">
                                <h4 class="text-h5 text-black q-mx-md q-my-md">Register</h4>
                                <!--                        <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">-->
                                <!--                            <q-btn fab icon="add" color="purple-4"/>-->
                                <!--                        </div>-->
                            </q-card-section>
                            <q-card-section>
                                <q-form class="q-px-sm q-pt-md">
                                    <q-input square v-model="username" type="username" label="Username">
                                        <template v-slot:prepend>
                                            <q-icon name="person"/>
                                        </template>
                                    </q-input>

                                    <q-input square v-model="email" type="email" label="Email">
                                        <template v-slot:prepend>
                                            <q-icon name="email"/>
                                        </template>
                                    </q-input>


                                    <q-input label="Password" v-model="password1" :type="isPwd ? 'password' : 'text'"
                                            >

                                        <template v-slot:prepend>
                                            <q-icon name="lock" size="20px"/>
                                        </template>

                                        <template v-slot:append>
                                            <q-icon
                                                    :name="isPwd ? 'visibility_off' : 'visibility'"
                                                    class="cursor-pointer"
                                                    @click="isPwd = !isPwd"
                                            />
                                        </template>
                                    </q-input>


                                    <q-input label="Confirm Password" v-model="password2"
                                             :type="isPwd ? 'password' : 'text'" >

                                        <template v-slot:prepend>
                                            <q-icon name="lock" size="20px"/>
                                        </template>

                                        <template v-slot:append>
                                            <q-icon
                                                    :name="isPwd ? 'visibility_off' : 'visibility'"
                                                    class="cursor-pointer"
                                                    @click="isPwd = !isPwd"
                                            />
                                        </template>
                                    </q-input>


                                    <!--                            <q-input square clearable v-model="password" type="password" label="Password">-->
                                    <!--                                <template v-slot:prepend>-->
                                    <!--                                    <q-icon name="lock"/>-->
                                    <!--                                </template>-->
                                    <!--                            </q-input>-->
                                </q-form>
                            </q-card-section>
                            <!--                    <q-card-section>-->
                            <!--                        <div class="text-center q-pa-md q-gutter-md">-->
                            <!--                            <q-btn round color="indigo-7">-->
                            <!--                                <q-icon name="fab fa-facebook-f" size="1.2rem"/>-->
                            <!--                            </q-btn>-->
                            <!--                            <q-btn round color="red-8">-->
                            <!--                                <q-icon name="fab fa-google-plus-g" size="1.2rem"/>-->
                            <!--                            </q-btn>-->
                            <!--                            <q-btn round color="light-blue-5">-->
                            <!--                                <q-icon name="fab fa-twitter" size="1.2rem"/>-->
                            <!--                            </q-btn>-->
                            <!--                        </div>-->
                            <!--                    </q-card-section>-->
                            <q-card-actions class="q-px-lg">
                                <q-btn @click.prevent="SigninData" unelevated size="lg" color="black"
                                       class="full-width text-white" label="Register"/>
                            </q-card-actions>
                            <q-card-section class="text-center q-pa-sm">
                                <p class="text-grey-6">Already have an account?</p>
                            </q-card-section>
                        </q-card>
                    </div>
                </div>
                <!--        <div class="column q-pa-lg">-->
                <!--            <div class="row">-->
                <!--                <q-card square class="shadow-24" style="width:300px;height:485px;">-->
                <!--                    <q-card-section class="bg-deep-purple-7">-->
                <!--                        <h4 class="text-h5 text-white q-my-md">Registration</h4>-->
                <!--                        <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">-->
                <!--                            <q-btn fab icon="close" color="purple-4"/>-->
                <!--                        </div>-->
                <!--                    </q-card-section>-->
                <!--                    <q-card-section>-->
                <!--                        <q-form class="q-px-sm q-pt-xl q-pb-lg">-->
                <!--                            <q-input square clearable v-model="email" type="email" label="Email">-->
                <!--                                <template v-slot:prepend>-->
                <!--                                    <q-icon name="email"/>-->
                <!--                                </template>-->
                <!--                            </q-input>-->
                <!--                            <q-input square clearable v-model="username" type="username" label="Username">-->
                <!--                                <template v-slot:prepend>-->
                <!--                                    <q-icon name="person"/>-->
                <!--                                </template>-->
                <!--                            </q-input>-->
                <!--                            <q-input square clearable v-model="password" type="password" label="Password">-->
                <!--                                <template v-slot:prepend>-->
                <!--                                    <q-icon name="lock"/>-->
                <!--                                </template>-->
                <!--                            </q-input>-->
                <!--                        </q-form>-->
                <!--                    </q-card-section>-->
                <!--                    <q-card-actions class="q-px-lg">-->
                <!--                        <q-btn unelevated size="lg" color="purple-4" class="full-width text-white" label="Get Started"/>-->
                <!--                    </q-card-actions>-->
                <!--                    <q-card-section class="text-center q-pa-sm">-->
                <!--                        <p class="text-grey-6">Return to login</p>-->
                <!--                    </q-card-section>-->
                <!--                </q-card>-->
                <!--            </div>-->
                <!--        </div>-->
            </q-page>
        </q-page-container>
    </q-layout>
</template>

<script>
    import HomePageHeader from "../components/HomePageHeader";

    export default {
        components: {
            HomePageHeader,
        },
        name: 'Login',

        data() {
            return {
                email: '',
                password1: '',
                password2: '',

                isPwd: true,
                username: '',

            }
        },
        methods: {

            // logout(){
            //     this.$store.dispatch("signoutFunction")
            // },

            SigninData() {
                console.log('SIGNIN DATA', {password: this.password, username: this.username});
                let data = {password: this.password, username: this.username};
                this.$store.dispatch("signinFunction", data)
            }
        }


    }
</script>

<style>
</style>


<!--<template>-->

<!--    <div class="q-pa-md">-->
<!--        <div class="q-gutter-md row items-start">-->
<!--            <q-input v-model="username" filled type="text" hint="username"/>-->

<!--            <q-input v-model="password" filled :type="isPwd ? 'password' : 'text'" hint="Password with toggle">-->
<!--                <template v-slot:append>-->
<!--                    <q-icon-->
<!--                            :name="isPwd ? 'visibility_off' : 'visibility'"-->
<!--                            class="cursor-pointer"-->
<!--                            @click="isPwd = !isPwd"-->
<!--                    />-->
<!--                </template>-->
<!--            </q-input>-->
<!--            <q-btn color="primary" label="Signin" @click.prevent="SigninData"/>-->
<!--        </div>-->
<!--    </div>-->

<!--</template>-->

<!--<script>-->
<!--    export default {-->
<!--        name: "Signin",-->
<!--        data() {-->
<!--            return {-->
<!--                password: '',-->
<!--                isPwd: true,-->
<!--                username: '',-->

<!--            }-->
<!--        },-->
<!--        methods: {-->
<!--            SigninData() {-->
<!--                console.log('SIGNIN DATA', {password: this.password, username: this.username});-->
<!--                let data = {password: this.password, username: this.username};-->
<!--                this.$store.dispatch("signinFunction", data)-->
<!--            }-->
<!--        }-->

<!--    }-->
<!--</script>-->

<!--<style scoped>-->

<!--</style>-->