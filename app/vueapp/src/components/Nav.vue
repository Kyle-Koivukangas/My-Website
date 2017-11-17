<template>
    <div class="navigation">
        <transition enter-active-class="slideInLeft" leave-active-class="slideOutLeft">
            <div class="sidebar fixed-top" v-if="show">
                <!-- <div class="portrait-wrapper"> -->
                <img class="portrait" src="../assets/Kyle.jpg" alt="">
                <!-- </div> -->
                <h3 class="nav-title">Kyle Koivukangas</h3>

                <div class="nav-links">
                    <ul>
                        <router-link class="link" tag="li" to="/">Home</router-link>
                        <router-link class="link" tag="li" to="/about">About</router-link>
                        <router-link class="link" tag="li" to="/projects">Projects</router-link>
                        <router-link class="link" tag="li" to="/blog">Blog</router-link>
                        <div class="special-btn">
                            <router-link tag="li" to="/hireme">Hire Me</router-link>    
                        </div>
                    </ul>
                </div>

                <div class="secondary-info">
                    <ul>
                        <li>Email</li>
                        <li>Github</li>
                        <li>StackOverflow</li>
                        <li>Quora</li>
                        <li>PGP</li>
                        <li>BTC</li>
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

        <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
        <!-- <button @click="show = !show">test</button>
        <p>show = {{ show }}</p> -->

        

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
        }
    },
    watch: {
        show: function (show) {
            //this watcher is just meant to delay how long it takes for the navigation 'hamburger' button to reappear after closing the sidebar.
            if (show === true) {
                this.showBtn = false;
                this.$emit('show', true);
            } else {
                this.$emit('show', false)
                setTimeout(() => {
                    this.showBtn = true;
                }, 250);
            }
        },
    },
    methods: {
        clickOutside(e) {
            if (!this.$el.contains(e.target) && this.show) {
                this.show = false;
            }
        },
        esc(e) {
            if (e.keyCode !== 27)
                return

            this.show = false;
        },

    },
    created() {
        // event listener to close on external click
        setTimeout(() => document.addEventListener('click', this.clickOutside))
        //event listener to close when escape key is pressed
        setTimeout(() => document.addEventListener('keydown', this.esc))
    },
    beforeDestroy() {
        //remove event listeners if component is closed
        document.removeEventListener('click', this.clickOutside)
        document.removeEventListener('keydown', this.esc)
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
  margin: 10px;
  & #ico {
    //stroke doesn't seem to work on font awesome icons..
    -webkit-text-stroke: 1px white;
    color: $black;
    text-shadow: 0px 0px 3px #fff;
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
  }
  & .link:hover {
    color: $highlight2;
  }
}
.special-btn {
  background-color: $highlight2;
  width: 100px;
  margin: auto;
  border-radius: 25px;
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
