import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isLoggedIn: false,
        AUTH_TOKEN: null,
    },
    getters: {
        isLoggedIn: state => {
            return state.isLoggedIn;
        },
        AUTH_TOKEN: state => {
            return state.AUTH_TOKEN;
        },
    },
    mutations: {
        'SET_ISLOGGEDIN'(state, bool) {
            state.isLoggedIn = bool;
        },
        'SET_AUTH_TOKEN'(state, auth_token) {
            state.AUTH_TOKEN = auth_token;
        },
    },
    actions: {
        
    }
});
