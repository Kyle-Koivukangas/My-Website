import Vue from 'vue'
import Router from 'vue-router'

import Home from '../components/Home'
import Projects from '../components/projects/Projects'
import About from '../components/About'
import Blog from '../components/blog/Blog'

// const Home = () => import('@/components/Home.vue')
// const About = () => import('@/components/About.vue')
// const Projects = () => import('@/components/projects/Projects.vue')
// const Blog = () => import('@/components/blog/Blog.vue')

Vue.use(Router)

export default new Router({
    routes: [
        { path: '/', component: Home },
        { path: '/projects', component: Projects },
        { path: '/about', component: About },
        { path: '/blog', component: Blog }
    ],
    mode: 'history',
    scrollBehaviour(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else if (to.hash) {
            return {selector: to.hash}
        } else {
            return {X: 0, Y: 0}
        }
    }
})
