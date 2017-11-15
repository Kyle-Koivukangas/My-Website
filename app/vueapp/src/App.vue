<template>
  <div id="app">
    <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
    <!-- <p>SHOW VALUE: {{ showNav }}</p> -->

    <!-- <img src="./assets/logo.png"> -->
    <vue-nav @show="showNav = $event"></vue-nav>
    <!-- <vue-navigation></vue-navigation> -->
    <router-view class="view" :class="{pushRight: showNav, pushLeft: !showNav}"/>
  </div>
</template>

<script>
export default {
    name: 'app',
    components: {
        vueNav: () => import("./components/Nav.vue"),
        vueNavigation: () => import("./components/Navigation.vue"),
    },
    data() {
        return {
            showNav: false,
        }
    },
    methods: {
        navTransform(show) {
            if (show === true) {

            } if (show === false) {

            } else {
                console.log("invalid 'show' property; show must be boolean value");
            }
        }
    },

};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  margin-top: 0px;
  width: 100%;
}
// .pushRight {
//   transition: all ease 0.5s, width ease 0.5s, margin ease 0.5s;
//   -webkit-transition: all ease 0.5s, width ease 0.5s, margin ease 0.5s;
//   transform: translateX(300px);
//   width: calc(100% - 300px);
//   margin: 0 0 0 -150px;
// }
// .pushLeft {
//   transition: all ease 0.5s, width ease 0.5s;
//   -webkit-transition: all ease 0.5s, width ease 0.5s;
//   transform: translateX(0px);
//   width: 100%;
//   margin-left: 50%;
//   margin: 0 50% 0 0;
// }
.view {
    margin: auto;
}
</style>
