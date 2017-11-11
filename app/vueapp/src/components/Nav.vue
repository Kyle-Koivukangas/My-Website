<template>
    <div class="navigation">

        <transition name="slideLeft">
            <div class="sidebar fixed-top" v-if="show">
                <h1>SIDEBAR</h1>
                <ul>
                    <li>LINK1</li>
                    <li>LINK2</li>
                    <li>LINK3</li>
                </ul>
                <button @click="show = !show">close</button>
            </div>
        </transition>

        <transition name="fade">
            <div v-if="showBtn" class="nav-btn fixed-top" @click="show = !show">
                <icon name="bars" scale="3" label="Navigation" v-on:click="show = !show"></icon>
            </div>
        </transition>

        <button @click="show = !show">test</button>
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
    watch: {
        show: function (show) {
            //this watcher is just meant to delay how long it takes for the navigation 'hamburger' button to reappear after closing the sidebar.
            if (show === true) {
                this.showBtn = false;
            } else {
                setTimeout(() => this.showBtn = true, 650)
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

<style>
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
</style>
