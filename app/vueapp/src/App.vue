<template>
  <div id="app">
    <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
    <!-- <p>SHOW VALUE: {{ showNav }}</p> -->

    <!-- <img src="./assets/logo.png"> -->
    <vue-nav @show="showNav = $event"></vue-nav>
    <!-- <vue-navigation></vue-navigation> -->
    <div class="view-wrapper" :class="{pushRight: showNav, pushLeft: !showNav}">
        <router-view class="view" />
        <vue-footer/>
    </div>
  </div>
</template>

<script>
export default {
    name: 'app',
    components: {
        vueNav: () => import("./components/Nav.vue"),
        vueFooter: () => import("./components/Footer.vue"),
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
  color: $darkgrey;
  margin-top: 0px;
  width: 100%;
}
a {
  color: $highlight2;
  text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
.pushRight {
  transition: all ease 0.5s, width ease 0.5s, margin ease 0.5s;
  -webkit-transition: all ease 0.5s, width ease 0.5s, margin ease 0.5s;
  transform: translateX(300px);
  width: calc(100% - 300px);
  //  half of the sidebar size (to keep main content centered when sidebar is open)
  left: 150px; // ***CHANGE THIS IF YOU CHANGE SIDEBAR WIDTH***
}
.pushLeft {
  transition: all ease 0.5s, width ease 0.5s;
  -webkit-transition: all ease 0.5s, width ease 0.5s;
  transform: translateX(0px);
  width: 100%;
  left: 0px;
}
.view-wrapper {
  //   margin: auto;
  font-size: 1.2rem;
  @media (max-width: 900px) {
      font-size: .9rem;
  }
}
</style>
