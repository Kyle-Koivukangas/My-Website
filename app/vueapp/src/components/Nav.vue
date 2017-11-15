<template>
    <div class="navigation">

        <transition name="slideLeft">
            <div class="sidebar fixed-top" v-if="show">
                <!-- <div class="portrait-wrapper"> -->
                <img class="portrait" src="../assets/Kyle.jpg" alt="">
                <!-- </div> -->
                <h3>Kyle Koivukangas</h3>

                <div class="nav-links">
                    <ul>
                        <li>About</li>
                        <li>Projects</li>
                        <li>Blog</li>
                        <li>Hire Me</li>
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
            <div v-if="showBtn" class="nav-btn fixed-top" @click="show = !show">
                <icon name="bars" scale="3" label="Navigation" v-on:click="show = !show"></icon>
            </div>
        </transition>

        <!-- debug stuff (REMOVE BEFORE DEPLOY) -->
        <!-- <button @click="show = !show">test</button>
        <p>show = {{ show }}</p> -->


    </div>
</template> 

<script>
import "vue-awesome/icons/bars";

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
                }, 650);
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
$sidebarWidth: 300px;

.fixed-top {
  position: fixed;
  top: 0;
}
.navigation {
  display: inline;
  left: 0;
}
.nav-btn {
  left: 0;
  width: 50px;
  z-index: 10;
}
.sidebar {
  background-color: $white;
  left: 0;
  width: $sidebarWidth;
  height: 100%;
  z-index: 11;
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
.nav-links {
  font-family: $lato;
  width: 100%;
  height: 100%;
  margin-top: 50px;
  line-height: 2.6em;
  font-size: 1.1em;
  font-weight: 100;
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
}
</style>
