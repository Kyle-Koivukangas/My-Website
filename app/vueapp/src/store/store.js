import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isLoggedIn: false,
        userName: '',
        AUTH_TOKEN: null,
    },
    getters: {
        isLoggedIn: state => {
            return state.isLoggedIn;
        },
        userName: state => {
            return state.userName;
        }.
        AUTH_TOKEN: state => {
            return state.AUTH_TOKEN;
        },
    },
    mutations: { 
        'SET_ISLOGGEDIN'(state, bool) {
            state.isLoggedIn = bool;
        },
        'SET_USERNAME'(state, userName) {
            state.userName = userName;
        },
        'SET_AUTH_TOKEN'(state, auth_token) {
            state.AUTH_TOKEN = auth_token;
        },
    },
    actions: {
        login( commit, { userName, authToken }) {
            commit('SET_USERNAME', userName)
            commit('SET_AUTH_TOKEN', authToken)
            commit('SET_ISLOGGEDIN', true)
        },
        logout({commit}) {
            commit('SET_USERNAME', null)
            commit('SET_AUTH_TOKEN', null)
            commit('SET_ISLOGGEDIN', false)
        }
    }
});
