<template>
  <div id="app">
    <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
    <!-- <p>SHOW VALUE: {{ showNav }}</p> -->

    <!-- <img src="./assets/logo.png"> -->
    <vue-nav @show="showNav = $event"></vue-nav>
    <!-- <vue-navigation></vue-navigation> -->
    <div class="view-wrapper" :class="{pushRight: showNav, pushLeft: !showNav}">
        <transition mode="out-in" name="fade">
            <router-view class="view" />
        </transition>
    </div>
    <vue-login v-if="showLogin" :show="showLogin" @close="showLogin = false"></vue-login>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {
    vueNav: () => import("./components/Nav.vue"),
    vueLogin: () => import("./components/Login.vue")
  },
  data() {
    return {
      showNav: false,
      showLogin: false,
      counter: 0
    };
  },
  methods: {
    navTransform(show) {
      if (show === true) {
      }
      if (show === false) {
      } else {
        console.log("invalid 'show' property; show must be boolean value");
      }
    }
  },
  created() {
    //This listener will open the login menu after pressing escape five times in quick succession
    var keyPressCounter = 0;
    document.addEventListener("keydown", e => {
      if (e.keyCode == 27) {
        if (keyPressCounter == 0) {
          setTimeout(() => {
            keyPressCounter = 0;
          }, 3000);
        }
        keyPressCounter += 1;
      }

      if (keyPressCounter >= 5) {
        this.showLogin = true;
      }
    });
  }
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
  @media (max-width: $mediaSmall) {
    font-size: 0.9rem;
  }
}
</style>
