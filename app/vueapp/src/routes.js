const Home = () => import('./components/Home.vue')
const About = () => import('./components/About.vue')
const Projects = () => import('./components/projects/Projects.vue')
const Blog = () => import('./components/blog/Blog.vue')

export const routes = [
    { path: '/', component: Home },
    { path: '/projects', component: Projects },
    { path: '/about', component: About },
    { path: '/blog', component: Blog }
]
