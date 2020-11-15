<template>
      <q-layout view="hHh lpR lFf" class="bg-grey-2">


        <HomePageHeader/>
<!--          <q-header bordered class="bg-white text-grey-8 q-py-xs" height-hint="58">-->
<!--            <q-toolbar>-->

<!--                <q-btn flat no-caps no-wrap class="q-ml-xs" v-if="$q.screen.gt.xs">-->


<!--                    <q-toolbar-title shrink class="text-weight-bold">-->

<!--                    <LogoTemplate/>-->

<!--                    </q-toolbar-title>-->
<!--                </q-btn>-->

<!--                <q-space/>-->
<!--                <q-space/>-->

<!--                <TopRightNavHome/>-->

<!--            </q-toolbar>-->
<!--        </q-header>-->


    <q-page-container>



  <q-page class="" style="background-color: #f7f7f7">
    <q-card class="bg-transparent">
      <q-card-section class="q-pa-none">
        <div class="row">
          <div class="col-lg-12 col-sm-12 col-xs-12 col-md-12">
            <q-carousel
              v-model="slide"
              transition-prev="slide-right"
              transition-next="slide-left"
              swipeable infinite
              animated
              control-color="primary"
              auto-play

              height="500px"
              class="rounded-borders bg-transparent"
            >
              <q-carousel-slide :name="1" class="column no-wrap">
                <div class="row fit justify-start items-center q-gutter-xs q-col-gutter no-wrap">
<!--                                    <q-img class="rounded-borders  full-height" :src="require('../assets/twain.jpg')"/>-->

                  <q-img class="rounded-borders  full-height"  style="background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);"/>
                  <div class="absolute-center text-center  full-width text-white">
                    <div class="text-h4 text-black  q-pa-sm">The Ideal Solution to Education</div>
<!--                    <div class="text-h2">-->
<!--                      <q-btn class="text-capitalize bg-black text-white-8 text-weight-bolder" label="Login"></q-btn>-->
<!--                    </div>-->
                  </div>
                </div>
              </q-carousel-slide>
            </q-carousel>
          </div>
        </div>

      </q-card-section>



      <q-card-section>
        <div class="text-center q-mt-xl text-black text-h4  q-mb-md">
          Our Pricing Plans
        </div>
        <div class="row justify-center q-col-gutter-lg q-pa-lg">
          <div class="col-lg-4 col-sm-12 col-xs-12 col-md-4">

            <q-intersection
              once
              transition="scale"
            >
              <q-card style="background-color: #fff" class="text-black">
                <q-card-section class="text-center text-h6 q-pa-lg">
                  STANDARD PLAN
                </q-card-section>
                <q-card-section class="text-center"
                                style="background-image: linear-gradient(to top, #a8edea 0%, #fed6e3 100%);">
                  <div class="text-weight-bolder">
                    <span class="text-h6">$</span><span class="text-h3">1</span><span class="text-h6">Million</span>
                  </div>
                </q-card-section>

                <q-card-section class="text-center">
                  <q-item class="text-center">
                    <q-item-section>
                      The good stuff
                    </q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item>
                    <q-item-section>
                      The good stuff
                    </q-item-section>
                  </q-item>
                  <q-separator />
                  <q-item>
                    <q-item-section>
                      The good stuff
                    </q-item-section>
                  </q-item>
                </q-card-section>

                <q-card-actions vertical align="center">
                  <q-btn class="text-capitalize q-mb-md q-pa-xs" style="background-color: #181728" outline color="">Buy
                    Plan Now
                  </q-btn>
                </q-card-actions>
              </q-card>
            </q-intersection>
          </div>
          <div class="col-lg-4 col-sm-12 col-xs-12 col-md-4">
            <q-intersection
              once
              transition="scale"
            >
              <q-card style="background-color: #fff" class="text-black">
                <q-card-section class="text-center text-h6 q-pa-lg">
                  GOLDEN PLAN
                </q-card-section>

                <q-card-section class="text-center"
                                style="background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);">
                  <div class="text-weight-bolder">
                    <span class="text-h6">$</span><span class="text-h3">2</span><span class="text-h6">Million</span>
                  </div>
                </q-card-section>

                <q-card-section class="text-center">
                  <q-item class="text-center">
                    <q-item-section>
                      The better stuff
                    </q-item-section>
                  </q-item>
                  <q-separator color="white"/>
                  <q-item>
                    <q-item-section>
                      The better stuff
                    </q-item-section>
                  </q-item>
                  <q-separator color="white"/>
                  <q-item>
                    <q-item-section>
                      The better stuff
                    </q-item-section>
                  </q-item>
                </q-card-section>
                <q-card-actions vertical align="center">
                  <q-btn class="text-capitalize q-mb-md q-pa-xs" style="background-color: #181728" outline color="">Buy
                    Plan Now
                  </q-btn>
                </q-card-actions>
              </q-card>
            </q-intersection>
          </div>
          <div class="col-lg-4 col-sm-12 col-xs-12 col-md-4">
            <q-intersection
              once
              transition="scale"
            >
              <q-card style="background-color: #fff" class="text-black">
                <q-card-section class=" text-center text-h6 q-pa-lg">
                  PLATINUM PLAN
                </q-card-section>

                <q-card-section class="text-center"
                                style="background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                  <div class="text-weight-bolder">
                    <span class="text-h6">$</span><span class="text-h3">3</span><span class="text-h6">Million</span>
                  </div>
                </q-card-section>

                <q-card-section class="text-center">
                  <q-item class="text-center">
                    <q-item-section>
                      The best stuff
                    </q-item-section>
                  </q-item>
                  <q-separator color="white"/>
                  <q-item>
                    <q-item-section>
                      The best stuff
                    </q-item-section>
                  </q-item>
                  <q-separator color="white"/>
                  <q-item>
                    <q-item-section>
                      The best stuff
                    </q-item-section>
                  </q-item>
                </q-card-section>
                <q-card-actions vertical align="center">
                  <q-btn class="text-capitalize q-mb-md q-pa-xs" size="md" style="background-color: #181728" outline
                         color="">
                    Buy
                    Plan Now
                  </q-btn>
                </q-card-actions>

              </q-card>
            </q-intersection>
          </div>
        </div>
      </q-card-section>

      <q-card-section>
        <section style="min-height: 25vh;">
          <div class="row justify-center q-col-gutter-lg q-pa-lg items-center">
            <div class="col-lg-6 col-sm-12 col-xs-12 col-md-6 items-center">
              <div class="text-h4 ">Register for our Newsletter now</div>
            </div>
            <div class="col-lg-5 col-sm-12 col-xs-12 col-md-5 items-center">
              <div class="text-h6 ">
                <q-input  outlined v-model="email" type="email" >
                  <template v-slot:before>
                    <q-icon name="mail" color="black"/>
                  </template>
                </q-input>
              </div>
            </div>
          </div>
        </section>
      </q-card-section>


    </q-card>

  </q-page>

    </q-page-container>
      </q-layout>
</template>

<script>

    //   import TopRightNavHome from "@/components/TopRightNavHome.vue";
    // import LogoTemplate from "../components/LogoTemplate";
    import HomePageHeader from "../components/HomePageHeader";

    export default {
       components: {
            HomePageHeader,
        },
        name: 'PageIndex',
        data() {
            return {
                email: '',
                tab: 'Most Popular Streams',
                slide: 1,
               text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

            }
        },
    }
</script>
<style>

  .text-stroke {
    color: white;
    -webkit-text-stroke: 1px #F8F8F8;
    text-shadow: 0px 1px 4px #23430C;
  }

  .q-carousel__slide, .q-carousel .q-carousel--padding{
    padding: 0px;
  }
</style>
