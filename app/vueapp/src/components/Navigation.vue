<template>
    <div class="navigation">

        <vue-sidebar v-model="show" :width="300" :duration=".5" effect="ease-in-out" @sidebarWasClosed="show = $event">
                <h1>SIDEBAR</h1>
                <!-- <div class="portrait-wrapper"> -->
                    <img class="portrait" src="../assets/Kyle.jpg" alt="">
                <!-- </div> -->
                <h3>Kyle Koivukangas</h3>


                <ul>
                    <li>About</li>
                    <li>Projects</li>
                    <li>Blog</li>
                    <li>Hire Me</li>
                </ul>

                <div class="secondary-info">
                    <ul >
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
            <div v-if="showBtn" class="nav-btn fixed-top" @click="show = !show">
                <icon name="bars" scale="3" label="Navigation" v-on:click="show = !show"></icon>
            </div>
        </transition>

        <div>
            <button @click="show = !show">Toggle</button><button @click="show = false">Close</button>
            <p>{{ show }}</p>
        </div>

        <p>show = {{ show }}</p>


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

<style>
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
  display: inline;
  left: 0;
}
.nav-btn {
  left: 0;
  width: 50px;
}
.sidebar {
  background-color: #555;
  left: 0;
  width: 300px;
  height: 100%;
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
.secondary-info {
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: right;
}
</style>
