<template>
  <div>
      <div class="banner">
          <div class="header-container">
              <h1>Projects</h1>
          </div>
      </div>

      <div class="content">
          <div class="hr"></div>
          <div v-for="project in apiProjects" :key="project.name" class="project">
              <div :style="{backgroundImage: 'url(' + project.image + ')' }" class="project-banner">
                  <h2>{{ project.name }}</h2>
              </div>
              <div class="project-description">
                  <p><span v-html="project.description"></span></p>
              </div>
          </div>
        <div v-if="apiFailed" v-for="project in projects" :key="project.name" class="project">
              <div :style="{backgroundImage: 'url(' + project.image + ')' }" class="project-banner">
                  <h2>{{ project.name }}</h2>
              </div>
              <div class="project-description">
                  <p><span v-html="project.description"></span></p>
              </div>
          </div>
      </div>
      <vue-footer/>
  </div>
</template>

<script>
import axios from "axios";

export default {
    components: {
        vueFooter: () => import("./Footer.vue"),
    },
    data() {
        return {
            projects: [
                {
                    id: 1,
                    name: "Eco Heart Card Reader App",
                    date: "01/09/2017",
                    description:
                        "This is a card/fortune reading app that I'm currently building for environmental artist - <a target='_blank' href='http://www.ingridkoivukangas.com'>Ingrid Koivukangas</a>. It's based on her Eco Heart Oracle deck, you can see a demo of it <a target='_blank' href='http://kyle-koivukangas.github.io/CardOracle'>here</a>.",
                    image: "https://www.kylekoivukangas.com/media/images/eco_heart_oracle.jpg",
                },
                {
                    id: 2,
                    name: "My personal website",
                    date: "01/10/2017",
                    description:
                        "My personal website, Django rest framework acts as the API for the Vue JS front end.",
                    image: "https://www.kylekoivukangas.com/media/images/my_website.jpg",
                },
            ],
            apiProjects: [],
            errors: [],
            apiFailed: false,
        };
    },
    created() {
        // check if dev environment or not, if dev then use allorigins CORS workaround to access api.
        if (window.location.origin == "http://localhost:8080") {
            axios
                .get(
                    "https://allorigins.me/get?method=raw&url=" +
                        encodeURIComponent("https://www.kylekoivukangas.com/api/projects/") +
                        "&callback=?"
                )
                .then(response => {
                    console.log("response received");
                    console.log(response);
                    this.apiProjects = response.data;
                })
                .catch(error => {
                    this.errors.push(error);
                });
        } else {
            axios
                .get("https://www.kylekoivukangas.com/api/projects/")
                .then(response => {
                    console.log("response received");
                    console.log(response);
                    this.apiProjects = response.data;
                })
                .catch(error => {
                    this.errors.push(error);
                    this.apiFailed = true;
                });
        }
    },
};
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
    & .header-container {
        text-align: center;
        width: 60%;
        margin: auto;
        & h1 {
            font-family: $lato;
            color: $white;
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
