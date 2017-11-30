<template>
  <div>
      <div class="banner">
          <div class="header-container">
              <h1>Projects</h1>
          </div>
      </div>

      <div class="content">
          <div class="hr"></div>
          <div v-for="project in apiProjects" :key="project" class="project">
              <div class="project-banner">
                  <h2>{{ project.name }}</h2>
              </div>
              <div class="project-description">
                  <!-- <p>{{ project.date }}</p> -->
                  <p><span v-html="project.description"></span></p>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios';
 
export default {
    data() {
        return {
            projects: [
                {
                    id: 1,
                    name: "Eco Heart Card Reader App",
                    date: "01/09/2017",
                    description: "This is a tarrot card reader app that I'm building for my my aunt (<a href='http://ingridkoivukangas.com/'>Ingrid Koivukangas</a>). I've made it with the Quasar mobile framework for Vue JS, this made it relatively easy to build it as a progressive web app with service workers to allow offline functionality. Being a progressive web app, it will function similar to a native app in that it can be run with or without an internet connection even though it's built using web techonologies; building it this way lets you circumvent the app store and allows you to build for every device."
                },
                {
                    id: 2,
                    name: "My personal website",
                    date: "01/10/2017",
                    description: "My personal website; Django rest framework acts as the API for the Vue JS front end. I'm currently building the back end CMS with Django CMS. "
                }
            ],
            apiProjects: [],
            errors: [],
        }
    },
    created() {
        axios.get('projects/')
        .then(response => {
            console.log("response recieved")
            console.log(response)
            this.apiProjects = response.data
        })
        .catch( error => {
            this.errors.push(error)
        })
    },
}
</script>

<style lang="scss">
.banner {
  background-color: $highlight2;
  height: 250px;
  max-width: $contentSize;
  margin: 30px auto;
  border-radius: 5px;
  display: flex;
  justify-content: left;
  align-items: center;
  //   background-image: url("../assets/webdevbanner.jpg");
  //   background-image: url("../assets/stocklaptop.jpg");
  // background-size: 1920px 1080px;
  // background-position-y: -250px;
  & .header-container {
    text-align: center;
    width: 60%;
    margin: auto;
    & h1 {
      font-family: $lato;
      color: $white;
      // text-shadow: 0px 0px 3px #000;
    }
  }
}

.content {
  max-width: $contentSize;
  margin: 0 auto;
}
.project {
  margin: 100px 0;
  text-align: left;
}

.project-banner {
  height: 175px;
  width: 100%;
  background-color: $highlight;
  border-radius: 4px;
  display: flex;
  justify-content: left;
  align-items: center;
  & h2 {
    text-align: center;
    margin: auto;
    color: $white;
    font-family: $lato;
  }
}
</style>
