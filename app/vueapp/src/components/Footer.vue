<template>
  <div class="footer">
      <div class="hr"></div>

      <div class="footlinks">
          <ul>
              <li><icon class="ico" name="envelope" scale="1" label="Email"></icon> Email</li>
              <li><icon class="ico" name="skype" scale="1" label="skype"></icon> Skype</li>
              <li><icon class="ico" name="github" scale="1" label="github"></icon> Github</li>
              <li><icon class="ico" name="linkedin-square" scale="1" label="linkedin"></icon> LinkedIn</li>
              <li><icon class="ico" name="stack-overflow" scale="1" label="stack overflow"></icon> Stack Overflow</li>
          </ul>
      </div>
      
  </div>
</template>

<script>
import "vue-awesome/icons/envelope";
import "vue-awesome/icons/github";
import "vue-awesome/icons/linkedin-square";
import "vue-awesome/icons/stack-overflow";
import "vue-awesome/icons/skype";

export default {

}
</script>

<style lang="scss">
$contentwidth: 900px;
.footer {
  width: $contentwidth;
  margin: 50px auto;
}
.hr {
  background-color: $lightgrey;
  opacity: 0.6;
  height: 2px;
  width: 100%;
  border-radius: 3px;
}
.footlinks {
  //   display: grid;
  width: 60%;
  margin: 30px auto;
  & ul {
    columns: 3;
    margin: 0 auto;
    text-align: center;
  }
  & li {
    display: inline-block;
    vertical-align: top;
    width: 150px;
    min-height: 30px;
    // border: 1px solid #000;
    margin: 5px;
  }
}
.ico {
    margin: auto;
    display: inline-block
}
</style>
