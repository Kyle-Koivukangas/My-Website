<template>
  <div id="app">
    <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
    <!-- <p>SHOW VALUE: {{ showNav }}</p> -->

    <!-- <img src="./assets/logo.png"> -->
    <vue-nav @show="showNav = $event"></vue-nav>
    <!-- <vue-navigation></vue-navigation> -->
    <router-view class="content" :class="{pushRight: showNav, pushLeft: !showNav, widthLess: showNav}"/>
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
  color: #2c3e50;
  margin-top: 0px;
}
.pushRight {
  transition: all ease 1s, width ease 1s;
  -webkit-transition: all ease 1s, width ease 1;
  transform: translateX(300px);
  //   display: block;
  width: calc(100% - 300px);
}
.pushLeft {
  transition: all ease 1s, width ease 1s;
  -webkit-transition: all ease 1s, width ease 1;
  transform: translateX(0px);
  width: 100%;
}
</style>
