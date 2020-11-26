<template>
    <q-page class="q-pa-sm">
        <div class="row q-col-gutter-sm">
            <div class="col-lg-12 col-md-12 col-xs-12 col-sm-12">
                <q-card class="card-bg ">
                    <q-card-section class="text-h6 ">
                        <div class="text-h6">Edit Profile</div>
                        <div class="text-subtitle2">Complete your profile</div>
                    </q-card-section>
                    <q-card-section class="q-pa-sm">
                        <q-list class="row">
                            <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                                <q-item-section side>
                                    <q-avatar size="100px">
                                        <img src="https://cdn.quasar.dev/img/boy-avatar.png">
                                    </q-avatar>
                                </q-item-section>
                                <q-item-section>
                                    <q-btn unelevated label="Add Photo" class="text-capitalize bg-black text-white"
                                           style="max-width: 120px"></q-btn>
                                </q-item-section>
                            </q-item>

                            <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                <q-item-section>
                                    <q-input disable color="black" dense v-model="user_details.user.username"
                                             label="Username"/>
                                </q-item-section>
                            </q-item>
                            <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                <q-item-section>
                                    <q-input color="black" dense v-model="user_details.user.email"
                                             label="Email Address"/>
                                </q-item-section>
                            </q-item>
                            <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                <q-item-section>
                                    <q-input color="black" dense v-model="user_details.user.first_name"
                                             label="First Name"/>
                                </q-item-section>
                            </q-item>
                            <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                                <q-item-section>
                                    <q-input color="black" dense v-model="user_details.user.last_name"
                                             label="Last Name"/>
                                </q-item-section>
                            </q-item>
                            <!--              <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">-->
                            <!--                <q-item-section>-->
                            <!--                  <q-input  color="black" autogrow dense v-model="user_details.address" label="Address"/>-->
                            <!--                </q-item-section>-->
                            <!--              </q-item>-->
                            <!--              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">-->
                            <!--                <q-item-section>-->
                            <!--                  <q-input  color="black" dense v-model="user_details.city" label="City"/>-->
                            <!--                </q-item-section>-->
                            <!--              </q-item>-->
                            <!--              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">-->
                            <!--                <q-item-section>-->
                            <!--                  <q-input  color="black" dense v-model="user_details.post_code" label="Postal Code"/>-->
                            <!--                </q-item-section>-->
                            <!--              </q-item>-->
                            <q-item class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                                <q-item-section>
                                    <q-input color="black" type="textarea" dense v-model="user_details.teacher_bio"
                                             label="About"/>
                                </q-item-section>
                            </q-item>
                        </q-list>
                    </q-card-section>
                    <q-card-actions align="right">
                        <q-btn @click="updateProfile" unelevated class="text-capitalize bg-black text-white">Update
                            Info
                        </q-btn>
                    </q-card-actions>
                </q-card>
            </div>
            <!--      <div class="col-lg-4 col-md-4 col-xs-12 col-sm-12">-->

            <!--        <q-card class="card-bg text-black">-->
            <!--          <q-card-section class="text-center bg-transparent">-->
            <!--            <q-avatar size="100px" class="shadow-10">-->
            <!--&lt;!&ndash;              <img src="../statics/profile.svg">&ndash;&gt;-->
            <!--            </q-avatar>-->
            <!--            <div class="text-subtitle2 q-mt-lg">by Pratik Patel</div>-->
            <!--            <div class="text-h6 q-mt-md">Pratik Patel</div>-->
            <!--          </q-card-section>-->
            <!--          <q-card-section>-->
            <!--            <div class="text-body2 text-justify">-->
            <!--              My name is Pratik Patel (also known as @pratik227). I noticed myself pulling into programming since 2013,-->
            <!--              and then determined myself to become a skilled and knowledgeable programmer. My passion for my programming-->
            <!--              increases as I started working for Incentius (where I am currently working in).-->
            <!--            </div>-->
            <!--          </q-card-section>-->
            <!--        </q-card>-->
            <!--      </div>-->

            <div class="col-lg-12 col-md-12 col-xs-12 col-sm-12">


                <q-card class="card-bg text-black">
                    <q-card-section class="text-h6 q-pa-sm">
                        <div class="text-h6">Change Password</div>
                    </q-card-section>
                    <q-card-section class="q-pa-sm row">
                        <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                            <q-item-section>
                                Current Password
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
                            <q-item-section>
                                <div :v-if="validCheck">{{validCheck}}</div>
                                <q-input type="password" dense color="black"
                                         v-model="password_dict.current_password"
                                         lazy-rules
                                         v-bind:rules="Current"
                                         ref="current"
                                         label="Current Password"/>
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                            <q-item-section>
                                New Password


                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
                            <q-item-section>

                                <q-input
                                        v-model="password_dict.new_password"
                                        dense color="black"
                                        label="New Password"
                                        v-bind:type="isPwd ? 'password' : ''"
                                        lazy-rules
                                        v-bind:rules="Required"
                                        ref="fldPasswordChange">
                                    <template v-slot:append>
                                        <q-icon :name="isPwd ? 'visibility_off' : 'visibility'"
                                                class="cursor-pointer"
                                                v-on:click="isPwd = !isPwd"></q-icon>
                                    </template>
                                </q-input>


                                <!--                <q-input type="password"  -->
                                <!--                         dense outlined color="black" -->
                                <!--                         round v-model="password_dict.new_password"-->
                                <!--                         label="New Password"/>-->
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                            <q-item-section>
                                Confirm New Password
                            </q-item-section>
                        </q-item>
                        <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
                            <q-item-section>


                                <q-input dense color="black"
                                         v-model="password_dict.confirm_new_password"
                                         label="Confirm New Password"
                                         v-bind:type="isPwd ? 'password' : ''"
                                         lazy-rules
                                         v-bind:rules="ConfirmPWD"
                                         ref="fldPasswordChangeConfirm">
                                    <template v-slot:append>
                                        <q-icon :name="isPwd ? 'visibility_off' : 'visibility'"
                                                class="cursor-pointer"
                                                v-on:click="isPwd = !isPwd"></q-icon>
                                    </template>
                                </q-input>


                                <!--                                <q-input type="password" dense outlined round color="black"-->
                                <!--                                         v-model="password_dict.confirm_new_password"-->
                                <!--                                         label="Confirm New Password"/>-->
                            </q-item-section>
                        </q-item>
                    </q-card-section>
                    <q-card-actions align="right">
                        <q-btn @click="cancelPassword" unelevated
                               class="text-capitalize bg-black text-white">Cancel
                        </q-btn>

                        <q-btn :disable="!testEditBtn" @click="updatePassword" unelevated
                               class="text-capitalize bg-black text-white">Change
                            Password
                        </q-btn>
                    </q-card-actions>

                </q-card>
            </div>
        </div>

        <q-inner-loading :showing="visible" class="qspin">
            <q-spinner size="50px" color="black"/>
        </q-inner-loading>

        <!--    <q-dialog  :position="position">-->
        <!--      <q-card style="width: 350px">-->
        <!--        <q-card-section class="row items-center no-wrap">-->
        <!--          {{validCheck}}-->
        <!--        </q-card-section>-->
        <!--      </q-card>-->
        <!--    </q-dialog>-->

        <!--        save dialog-->
        <q-dialog v-model="seamlessSave" seamless position="bottom">
            <!--        <q-dialog v-model="seamless" seamless position="bottom">-->
            <q-card dark style="width: 350px">
                <q-card-section class="row items-center justify-center no-wrap">
                    <div>
                        <div class="text-weight-bold">Profile Updated</div>
                    </div>
                </q-card-section>
            </q-card>
        </q-dialog>


    </q-page>
</template>

<script>
    export default {
        name: "UserProfile",
        data() {
            return {
                // user_details: {
                //     user: {
                //         first_name: '',
                //         last_name: '',
                //         username: '',
                //         email: '',
                //         teacher_bio: ''
                //     }
                // },
                password_dict: {
                    current_password: '',
                    new_password: '',
                    confirm_new_password: ''
                },
                dialog: true,
                position: 'top',
                isPwd: 'password',
                visible: false,
                showSimulatedReturnData: false
            }
        },


        created() {
            console.log('CREATED CALLED')
            // this.user_details = this.$store.getters["getInstructor"];
        },

        computed: {

            user_details() {

                return this.$store.getters["getInstructor"];
                },


            testEditBtn() {
                if ((this.password_dict.current_password.length >= 3) && this.password_dict.new_password.length >= 8 && (this.password_dict.new_password === this.password_dict.confirm_new_password)) {
                    return true
                } else {
                    return false
                }
            },

            seamlessSave: {
                get() {
                    return this.$store.getters['getSeamlessSave']
                },
                set(val) {
                    this.seamlessSave = val
                }
            },


            validCheck() {
                return this.$store.getters["getValidation"];
            },


            ConfirmPWD() {
                return [
                    (v) => !!v || "Required to update password",
                    (v) => v == this.$refs.fldPasswordChange.value || "These passwords don't match."
                ]
            },

            Required() {


                return [
                    (v) => !!v || "Required to update password",


                    (v) => v.length >= 8 || "Password must be at least 8 Characters long",
                    // val => val.length <= 3
                ]
            },

            Current() {

                let msg = this.validCheck
                console.log('MSGMSG', msg);

                return [
                    (v) => !!v || "Required to update password",
                    (v) => v.length >= 5 || "Please enter full current password to update",
                    (v) => v.length > 0 || msg
                ]

                    // val => val.length <= 3

                // return [(v) => !!v || 'Required to update password',
                //     (v) => !!v || "Required to update password",
                //
                // ]
            }

        },

        methods: {


            cancelPassword() {

                this.$refs.current.resetValidation();
                this.$refs.fldPasswordChange.resetValidation();
                this.$refs.fldPasswordChangeConfirm.resetValidation();

                this.password_dict = {
                    current_password: '',
                    new_password: '',
                    confirm_new_password: ''
                }


            },


            // loading on save
            showTextLoading() {
                this.visible = true
                this.showSimulatedReturnData = false
                setTimeout(() => {
                    this.visible = false
                    this.showSimulatedReturnData = true
                }, 3000)
            },


            updateProfile() {
                this.showTextLoading();

                let data = {

                    teacher_bio: this.user_details.teacher_bio,

                    user: {
                        email: this.user_details.user.email,
                        first_name: this.user_details.user.first_name,
                        last_name: this.user_details.user.last_name,
                    }
                };

                this.$store.dispatch('updateInstructor', data);

            },

            updatePassword() {
                this.showTextLoading();


                let data = {
                    "old_password": this.password_dict.current_password,
                    "password_01": this.password_dict.new_password,
                    "password_02": this.password_dict.confirm_new_password
                };

                this.$store.dispatch('updateUserPassword', data);

            }
        }

    }
</script>

<style scoped>
    .card-bg {
        background-color: #fff;
    }
</style>