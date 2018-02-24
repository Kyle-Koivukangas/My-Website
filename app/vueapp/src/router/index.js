import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home';
import About from '../components/About';
import Projects from '../components/Projects';
import Blog from '../components/Blog';
import HireMe from '../components/HireMe';

Vue.use(Router);

export default new Router({
    // mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/about',
            name: 'about',
            component: About,
        },
        {
            path: '/projects',
            name: 'projects',
            component: Projects,
        },
        {
            path: '/blog',
            name: 'blog',
            component: Blog,
        },
        {
            path: '/blog/:slug',
            name: 'blog',
            component: Blog,
        },
        {
            path: '/hireme',
            name: 'hireme',
            component: HireMe,
        },
    ],
});
