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
                  <q-btn unelevated label="Add Photo" class="text-capitalize bg-black text-white"   style="max-width: 120px"></q-btn>
                </q-item-section>
              </q-item>

              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input color="black" dense v-model="user_details.user.username" label="Username"/>
                </q-item-section>
              </q-item>
              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input  color="black" dense v-model="user_details.user.email" label="Email Address"/>
                </q-item-section>
              </q-item>
              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input  color="black" dense v-model="user_details.user.first_name" label="First Name"/>
                </q-item-section>
              </q-item>
              <q-item class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                <q-item-section>
                  <q-input  color="black" dense v-model="user_details.user.last_name" label="Last Name"/>
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
                  <q-input  color="black" type="textarea" dense v-model="user_details.teacher_bio" label="About"/>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn @click="updateProfile" unelevated class="text-capitalize bg-black text-white">Update Info</q-btn>
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
                <q-input type="password"  dense outlined color="black" round v-model="password_dict.current_password"
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
                <q-input type="password"  dense outlined color="black" round v-model="password_dict.new_password"
                         label="New Password"/>
              </q-item-section>
            </q-item>
            <q-item class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-item-section>
                Confirm New Password
              </q-item-section>
            </q-item>
            <q-item class="col-lg-8 col-md-8 col-sm-12 col-xs-12">
              <q-item-section>
                <q-input type="password"  dense outlined round color="black" v-model="password_dict.confirm_new_password"
                         label="Confirm New Password"/>
              </q-item-section>
            </q-item>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn unelevated class="text-capitalize bg-black text-white">Change Password</q-btn>
          </q-card-actions>

        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
    export default {
        name: "UserProfile",
        data() {
            return {
                user_details: {},
                password_dict: {}
            }
        },

        created() {

            this.user_details = this.$store.getters["getInstructor"];
        },

      methods:{
          updateProfile(){
            let data = {
              email: this.user_details.user.email,
              first_name: this.user_details.user.first_name,
              last_name: this.user_details.user.last_name,
            };

            this.$store.dispatch('putProfile', data);

          }
      }

    }
</script>

<style scoped>
  .card-bg {
    background-color: #fff;
  }
</style>