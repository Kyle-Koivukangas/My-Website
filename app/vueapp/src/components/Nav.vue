<template>
    <div class="navigation">
        <transition enter-active-class="slideInLeft" leave-active-class="slideOutLeft">
            <div class="sidebar fixed-top" v-if="show">
                <img class="portrait" src="../assets/Kyle.jpg" alt="">
                <h3 class="nav-title">Kyle Koivukangas</h3>

                <div class="nav-links">
                    <ul>
                        <li>
                            <router-link class="link" to="/" exact>Home</router-link>
                        </li>
                        <li>
                            <router-link class="link"  to="/about">About</router-link>
                        </li>
                        <li>
                            <router-link class="link" to="/projects">Projects</router-link>
                        </li>
                        <li>
                            <router-link class="link" to="/blog">Blog</router-link>
                        </li>
                        <div class="special-btn">
                            <router-link tag="li" to="/hireme">Hire Me</router-link>    
                        </div>
                    </ul>
                </div>

                <div class="secondary-info">
                    <ul>
                        <li><a class="secondary-link" href="mailto:kyle.koivukangas@gmail.com"><icon class="ico" name="envelope" scale="1" label="Email"></icon> Email</a></li>
                        <li><a class="secondary-link" target="_blank" href="https://github.com/Kyle-Koivukangas"><icon class="ico" name="github" scale="1" label="github"></icon> Github</a></li>
                        <li><a class="secondary-link" target="_blank" href="https://stackoverflow.com/users/6900746/kyle"><icon class="ico" name="stack-overflow" scale="1" label="stack overflow"></icon> Stack Overflow</a></li>
                        <li><a class="secondary-link" target="_blank" href="https://www.linkedin.com/in/kyle-koivukangas/"><icon class="ico" name="linkedin-square" scale="1" label="linkedin"></icon> LinkedIn</a></li>
                        <li><a @click="alertPGP()" class="secondary-link" href="">PGP</a></li>
                        <li><a @click="alertBTC()" class="secondary-link" href="">BTC</a></li>
                    </ul>
                </div>
                <button @click="show = !show">close</button>
            </div>
        </transition>

        <transition name="fade">
            <div v-if="showBtn" class="nav-btn fixed-top" :class="{pushRight: show, pushLeft: !show}" @click="show = !show">
                <icon id="ico" name="bars" scale="3" label="Navigation" v-on:click="show = !show"></icon>
            </div>
        </transition>

        <transition enter-active-class="slideInLeft" leave-active-class="hide">
            <div v-if="!showBtn" class="nav-btn fixed-top test" :class="{pushRight: show, pushLeft: !show}" @click="show = !show">
                <icon class="times" scale="3" label="Close"></icon>
            </div>
        </transition>        

    </div>
</template> 

<script>
import "vue-awesome/icons/bars";
import "vue-awesome/icons/times";

export default {
  data() {
    return {
      show: false,
      showBtn: true
    };
  },
  watch: {
    show: function(show) {
      //this watcher is just meant to delay how long it takes for the navigation 'hamburger' button to reappear after closing the sidebar.
      if (show === true) {
        this.showBtn = false;
        this.$emit("show", true);
      } else {
        this.$emit("show", false);
        setTimeout(() => {
          this.showBtn = true;
        }, 250);
      }
    }
  },
  methods: {
    clickOutside(e) {
      if (!this.$el.contains(e.target) && this.show) {
        this.show = false;
      }
    },
    esc(e) {
      if (e.keyCode !== 27) return;

      this.show = false;
    },
    alertPGP() {
        // Prompt user instead of using alert, this automatically highlights the text for easy copying.        
        prompt("Please press ctrl+c to copy the PGP key.", "-----BEGIN PGP PUBLIC KEY BLOCK-----     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GRez    -----END PGP PUBLIC KEY BLOCK-----")
    },
    alertBTC(){
        prompt("Please press ctrl+c to copy the BTC receive address.", "1AXknQRS4CLYCLLuAd6UMsBkbbA9DM4XnW")        
    }
  },
  created() {
    // event listener to close on external click
    setTimeout(() => document.addEventListener("click", this.clickOutside));
    //event listener to close when escape key is pressed
    setTimeout(() => document.addEventListener("keydown", this.esc));
  },
  beforeDestroy() {
    //remove event listeners if component is closed
    document.removeEventListener("click", this.clickOutside);
    document.removeEventListener("keydown", this.esc);
  }
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Josefin+Slab|Ubuntu|Ubuntu+Condensed|Vollkorn|Lato");
$josefin: "Josefin Slab", serif;
$vollkorn: "Vollkorn", serif;
$ubuntu: "Ubuntu", sans-serif;
$ubuntucond: "Ubuntu Condensed", sans-serif;
$lato: "Lato", sans-serif;

$sidebarWidth: 300px;
.test {
  color: black;
  z-index: 20;
}
.highlight {
  color: $highlight;
}
.fixed-top {
  position: fixed;
  top: 0;
}
.navigation {
  display: inline;
  left: 0;
}
.nav-btn {
  width: 50px;
  z-index: 10;
  margin: 25px 0 0 25px;
  & #ico {
    -webkit-text-stroke: 1px white;
    color: $darkgrey;
    text-shadow: 0px 0px 3px #fff;
  }
  & :hover {
      cursor: pointer;
  }
}
.sidebar {
  background-color: $white;
  left: 0;
  width: $sidebarWidth;
  height: 100%;
  z-index: 11;
  border-right: $lightgrey solid 2px;
  & ul {
    list-style: none;
    padding: 0;
  }
}
.portrait {
  border-radius: 50%;
  max-width: 50%;
  max-height: 50%;
  margin-top: $sidebarWidth/4;
}
.nav-title {
  font-family: $lato;
  font-size: 1.3em;
}
.nav-links {
  font-family: $ubuntu;
  width: 100%;
  height: 100%;
  margin-top: 50px;
  line-height: 2.6em;
  font-size: 1.3em;
  font-weight: 100;
  & .link {
    cursor: pointer;
    color: $black;
  }
  & .link:hover {
    transition: 0.3s;
    color: $highlight2;
    text-decoration: none;
  }
  & a.router-link-active {
    transition: 0.5s;
    color: $highlight2;
    text-decoration: none;
  }
}
.special-btn {
  background-color: $highlight2;
  width: 120px;
  margin: auto;
  margin-top: 15px;
  border-radius: 40px;
  color: $white;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.4);
  font-size: 1.1em;
  cursor: pointer;
}
.secondary-info {
  position: fixed;
  bottom: 0;
  left: 0;
  width: $sidebarWidth;
  text-align: right;
  font-family: $ubuntucond;
  font-weight: 600;
  color: $lightgrey;
  & ul {
    margin: 10px;
  }
}
.hide {
  display: none;
}
.secondary-link {
  color: $lightgrey;
  text-decoration: none !important;
}

// Animations:
@keyframes slideInLeft {
  from {
    transform: translate3d(-100%, 0, 0);
    visibility: visible;
  }

  to {
    transform: translate3d(0, 0, 0);
  }
}

.slideInLeft {
  -webkit-animation-name: slideInLeft;
  animation-name: slideInLeft;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
}
@keyframes slideOutLeft {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    visibility: hidden;
    transform: translate3d(-100%, 0, 0);
  }
}

.slideOutLeft {
  -webkit-animation-name: slideOutLeft;
  animation-name: slideOutLeft;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
}
</style>
