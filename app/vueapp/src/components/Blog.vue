<template>
<div>
    <div class="banner">
        <div class="header-container">
            <h1>Blog</h1>
        </div>
    </div>
    <div class="content">
        <h3>In development...</h3>
    </div>
    <vue-footer/>
</div>
  
</template>

<script>
export default {
    components: {
        vueFooter: () => import("./Footer.vue"),
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
</style>
