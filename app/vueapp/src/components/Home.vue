<template>
    <div>
        <div class="main">
            <div class="main-banner">
                <div class="header-container">
                    <h1>Hi, I'm Kyle. I design 	&amp; build<br>full-stack web applications.</h1>
                </div>
            </div>

            <div class="content">
                <div>
                    <p>I'm an independent web developer on Salt Spring Island, BC. I work primarily with Vue JS and Django.</p>

                    <p>Take a look at my <router-link to="projects">projects</router-link> to see what I've built. Have a website or application you need help with? Contact me <router-link to="hireme">here</router-link>.</p>

                </div>

            </div>
        </div>
        <vue-footer/>
    </div>
</template>

<script>
export default {
    name: "Home",
    components: {
        vueFooter: () => import("./Footer.vue"),
    },
    data() {
        return {};
    },

};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Josefin+Slab|Ubuntu|Ubuntu+Condensed|Vollkorn|Lato");
$josefin: "Josefin Slab", serif;
$vollkorn: "Vollkorn", serif;
$ubuntu: "Ubuntu", sans-serif;
$ubuntucond: "Ubuntu Condensed", sans-serif;
$lato: "Lato", sans-serif;


.main-banner {
  background-color: $highlight2;
  height: 300px;
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
}
.header-container {
  // background-color: white;
  text-align: center;
  width: 60%;
  margin: auto;

  & h1 {
    font-family: $lato;
    color: $white;
    // text-shadow: 0px 0px 3px #000;
  }
}
.main {
  font-family: $ubuntu;
  background-color: $white;
}
.content {
  margin: auto;
  max-width: $contentSize;
}
</style>
