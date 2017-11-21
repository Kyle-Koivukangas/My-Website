<template>
      <div>
        <div class="banner">
            <div class="header-container">
                <h1>Need a developer?</h1>
            </div>
        </div>
        <div class="content">
            <div class="section">
                <p>If you have a web application that you're interested in developing, I can help. I'm a full-stack developer, so I can build your project from concept to completion. I work primarily with Django for server side and Vue JS for front end work, but learning new technologies is not a problem.
                </p>
                <p>I'm currently looking for full-time employment but I am also available for hire on a freelance or contract basis. Send me an email at <a href="mailto:kyle.koivukangas@gmail.com">kyle.koivukangas@gmail.com</a> to discuss it further.</p>
                <br>
            </div>
        </div>
    </div>
</template>

<script>
export default {

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
.section{
    text-align: left;
}
</style>
