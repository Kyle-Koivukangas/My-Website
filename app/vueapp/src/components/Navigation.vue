<template>
    <div class="navigation">

        <vue-sidebar class="sidebar" v-model="show" :width="sidebarWidth" :duration=".5" effect="ease-in-out" @sidebarWasClosed="show = $event">
                <!-- <div class="portrait-wrapper"> -->
                    <img :style="{marginTop: sidebarWidth/4 + 'px'}" class="portrait" src="../assets/Kyle.jpg" alt="">
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
        </vue-sidebar>

        <transition name="fade">
            <div v-if="showBtn" class="nav-btn" @click="show = !show">
                <icon name="bars" scale="3" label="Navigation" v-on:click="show = !show"></icon>
            </div>
        </transition>

        <!-- debug info (REMOVE THIS BEFORE DEPLOYMENT) -->
        <!-- <div>
            <button @click="show = !show">Toggle</button><button @click="show = false">Close</button>
            <p>{{ show }}</p>
        </div>
        <p>show = {{ show }}</p> -->


    </div>
</template> 

<script>
import "vue-awesome/icons/bars";

export default {
    data() {
        return {
            show: false,
            showBtn: true,
            sidebarWidth: 300,
        }
    },
    components: {
        vueSidebar: () => import("./Sidebar.vue"),
    },
    watch: {
        show: function (show) {
            //this watcher is just meant to delay how long it takes for the navigation 'hamburger' button to reappear after closing the sidebar.
            if (show === true) {
                this.showBtn = false;
            } else {
                setTimeout(() => this.showBtn = true, 350)
            }
        },
    },

};
</script>

<style lang="scss">
// * {position: relative}
ul {
  /* list-style-type: none; */
  list-style: none;
  /* text-align: center; */
  padding: 0;
}
.fixed-top {
  position: fixed;
  top: 0;
}
.navigation {
  position: fixed;
  display: inline;
  left: 0;
  top: 0;
  z-index: 10;
}
.nav-btn {
  left: 0;
  width: 50px;
}
.sidebar {
  background-color: $white;
  left: 0;
  position: fixed;
  width: 100%;
}
.sidebar h3 {
    font-family: $ubuntu;
}
.portrait-wrapper {
  width: 100%;
  height: 100%;
}
.portrait {
  border-radius: 50%;
  max-width: 50%;
  max-height: 50%;  
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
  width: 100%;
  text-align: right;
  font-family: $ubuntucond;
  font-weight: 600;
  color: $lightgrey;
}
</style>
