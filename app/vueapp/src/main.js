// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Icon from 'vue-awesome/components/Icon';

import Vue from 'vue';
import App from './App';
import router from './router';
import Vuex from 'vuex';
import axios from 'axios';
import VueAxios from 'vue-axios';

require('vue2-animate/dist/vue2-animate.min.css')

Vue.component('icon', Icon);

Vue.use(Vuex)

Vue.use(VueAxios, axios)
//defining Axios instance for API calls to the back end
//and checking to see what environment it's run in (dev environment would be localhost:8000)
if (window.location.origin == "http://localhost:8080") {
    console.log("DEV ENVIRONMENT DETECTED (Vue + Django simoultaneously [CORS])");
    axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
    axios.defaults.headers = {
        // "Access-Control-Allow-Origin": "*",
        "Accept": "application/json",
        "Content-Type": "application/json",
        // 'X-Requested-With': 'XMLHttpRequest',
    }
    // axios.defaults.headers.common['Access-Control-Allow-Origin'] = "*";
} else if (window.location.origin == "http://127.0.0.1:8000") {
    console.log("DEV ENVIRONMENT DETECTED (all django build)");
    axios.defaults.baseURL = 'http://127.0.0.1:8000/api'
    axios.defaults.headers = {
        // "Access-Control-Allow-Origin": "*",
        "Accept": "application/json",
        "Content-Type": "application/json",
        // 'X-Requested-With': 'XMLHttpRequest',
    }
} else {
    axios.defaults.baseURL = 'http://kylekoivukangas.com/api'
}


Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    template: '<App/>',
    components: {
        App,
    },
});
