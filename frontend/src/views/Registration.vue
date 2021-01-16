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

<!--                                iterate through errors and display them as needed-->
                                <div class="signin-error"  v-for="(e, index) in error_message" :key="index" >{{e[0]}}</div>

                                <q-form class="q-px-sm q-pt-md">
                                    <q-input square v-model="username" type="username" label="Username">
                                        <template v-slot:prepend>
                                            <q-icon name="person"/>
                                        </template>
                                    </q-input>

                                    <q-input square v-model="email"
                                             type="email"
                                             label="Email"
                                             :rules="isValidEmail"
                                    >
                                        <template v-slot:prepend>
                                            <q-icon name="email"/>
                                        </template>
                                    </q-input>


<!--                                    <q-input-->
<!--                                        v-model="password_dict.new_password"-->
<!--                                        dense color="black"-->
<!--                                        label="New Password"-->
<!--                                        v-bind:type="isPwd ? 'password' : ''"-->
<!--                                        lazy-rules-->
<!--                                        v-bind:rules="Required"-->
<!--                                        ref="fldPasswordChange">-->
<!--                                    <template v-slot:append>-->
<!--                                        <q-icon :name="isPwd ? 'visibility_off' : 'visibility'"-->
<!--                                                class="cursor-pointer"-->
<!--                                                v-on:click="isPwd = !isPwd"></q-icon>-->
<!--                                    </template>-->
<!--                                </q-input>-->

                                    <q-input label="Password"
                                             v-model="password1"
                                             :type="isPwd ? 'password' : 'text'"
                                            lazy-rules
                                            v-bind:rules="Required"
                                            ref="fldPasswordChange">

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


                                    <q-input label="Confirm Password"
                                             v-model="password2"
                                             :type="isPwd ? 'password' : 'text'"
                                             lazy-rules
                                             v-bind:rules="ConfirmPWD"
                                             ref="fldPasswordChangeConfirm">

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

<!--                                    <q-input dense color="black"-->
<!--                                         v-model="password_dict.confirm_new_password"-->
<!--                                         label="Confirm New Password"-->
<!--                                         v-bind:type="isPwd ? 'password' : ''"-->
<!--                                         lazy-rules-->
<!--                                         v-bind:rules="ConfirmPWD"-->
<!--                                         ref="fldPasswordChangeConfirm">-->
<!--                                    <template v-slot:append>-->
<!--                                        <q-icon :name="isPwd ? 'visibility_off' : 'visibility'"-->
<!--                                                class="cursor-pointer"-->
<!--                                                v-on:click="isPwd = !isPwd"></q-icon>-->
<!--                                    </template>-->
<!--                                </q-input>-->


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
                                <q-btn :disable="!testEditBtn" @click.prevent="RegisterData" unelevated size="lg" color="black"
                                       class="full-width text-white" label="Register"/>
                            </q-card-actions>
                            <q-card-section class="text-center q-pa-sm">
                                <p @click="signinLink" class="text-grey-6">Already have an account?</p>
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

                username: '',
                email: '',
                password1: '',
                password2: '',

                isPwd: true,

                // eslint-disable-next-line
                reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
                // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
                // reg: (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
                // reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
            }

        },

        mounted() {
           this.$store.commit("clear_error_message");
        },


        methods: {

            // logout(){
            //     this.$store.dispatch("signoutFunction")
            // },

            signinLink(){
                this.$router.push('/signin');
            },

            RegisterData() {
                console.log('SIGNIN DATA', {password: this.password, username: this.username});
                let data = {password1: this.password1, password2: this.password2, username: this.username, email: this.email};
                this.$store.dispatch("registerFunction", data)
            }
        },

        computed:{

            error_message(){
                return this.$store.getters["getErrorMessage"]
            },

            testEditBtn() {
                if (this.password1.length >= 8 && (this.password1 === this.password2)) {
                    return true
                } else {
                    return false
                }
            },


            ConfirmPWD() {
                return [
                    (v) => !!v || "Required to update password",
                    (v) => v == this.$refs.fldPasswordChange.value || "These passwords don't match."
                ]
            },

             isValidEmail() {
                return [
                     (v) =>  this.reg.test(v) || "Please enter valid email."
                    // (this.email === "")? "" : (this.reg.test(this.email)) ? 'has-success' : 'has-error'

                ]
            },

            Required() {


                return [
                    (v) => !!v || "Required to update password",
                    (v) => v.length >= 8 || "Password must be at least 8 Characters long",
                    // val => val.length <= 3
                ]
            },

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