<template>
<div :id="postid"  class="postview collapsed" v-if="!hide">
    <slot name='head'></slot>
    <slot name='image'></slot>
    <slot name='description'></slot>
    <slot name='content'></slot>
    <slot name='foot'></slot>
    <div class="expand-btn" @click="togglePost()">
        <p v-if="expanded == false">Expand <icon class="ico" name="caret-down" scale="2" label="Expand"></icon></p>
        <p v-if="expanded == true">Collapse <icon class="ico" name="caret-up" scale="2" label="Collapse"></icon></p>
    </div>
</div>
  
</template>

<script>
import "vue-awesome/icons/caret-down";
import "vue-awesome/icons/caret-up";

export default {
    props: ["postid", "slug", "baseroute", "hideall"],
    data() {
        return {
            expanded: false,
            hide: false,
        };
    },
    watch: {
        $route(to, from) {
            // console.log('to: ', to)
            // console.log('from:', from)
            if (to.params.slug === this.slug) {
                this.expanded = true;
                this.hide = false;
                document.getElementById(this.postid).classList.remove("collapsed");                        
            } else {
                this.expanded = false;
                console.log(to.params.slug);
                if (to.params.slug === undefined ) {
                    this.hide = false;    
                } else {
                    this.hide = true;
                }
            }
        },
        expanded(value) {
            if (value) {
                this.$emit("expanded")
                // this.hideAllByClass("collapsed");
            } else {
                this.$emit("collapsed")                
                // this.showAllByClass("collapsed")
            }
        },
        // hideall(value) {
        //     console.log(this.$route.params.slug);
        //     if ((value === true) && (this.$route.params.slug === this.slug)) {
        //         this.hide = true;
        //     } else if (value === true) {
        //         this.hide = false;
        //     } else {
        //         this.hide = true;
        //     }
        // }
    },
    methods: {
        togglePost() {
            this.expanded = !this.expanded;
            // document.getElementById(this.postid).classList.toggle("collapsed");

            if (this.expanded) {
                document.getElementById(this.postid).classList.remove("collapsed");
                this.$router.push(this.baseroute + this.slug);
                // history.pushState({}, null, "/#baseRoute" + this.slug);
            } else {
                document.getElementById(this.postid).classList.add("collapsed");
                this.$router.push(this.baseroute);
                // this.$router.go(-1)
            }
            // console.log("params");
            // console.log(this.$route.params);
        },
        hideAllByClass(postClass="collapsed") {
            var posts = document.getElementsByClassName(postClass);
            console.log(posts)
            for (var i = 0; i < posts.length; i++) {
                posts[i].style.display = "none";
            }
        },
        showAllByClass(postClass="collapsed") {
            var posts = document.getElementsByClassName(postClass);
            for (var i = 0; i < posts.length; i++) {
                posts[i].style.display = 'block';
            }
        }
    },
    mounted() {
        console.log(`mounted ${this.postid}`)
        // //check route to see if post is already specified and if it matches this instance
        // if (this.$route.params.slug == this.slug) {
        //     // this.togglePost()
        //     this.expanded = !this.expanded;
        //     document.getElementById(this.postid).classList.remove("collapsed");            
        // } else if (this.$route.params.slug) {
        //     this.hide = true;
        // } else {
        //     this.hide = false;
        // }
        
    }
    // beforeRouteUpdate(to, from, next) {
    //     // react to route changes...
    //     // don't forget to call next()
    //     console.log('to:', to)
    //     console.log('from:', from)
    //     next()
    // },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Josefin+Slab|Ubuntu|Ubuntu+Condensed|Vollkorn|Lato");
$josefin: "Josefin Slab", serif;
$vollkorn: "Vollkorn", serif;
$ubuntu: "Ubuntu", sans-serif;
$ubuntucond: "Ubuntu Condensed", sans-serif;
$lato: "Lato", sans-serif;

.postview {
    margin: auto;
    margin-top: 25px;
    min-height: 250px;
    max-height: 550px;
    max-width: $contentSize;
    background-color: #eee;
    border-radius: 5px;
    position: relative;
    overflow: hidden;

    -webkit-transition: max-height 0.8s;
    -moz-transition: max-height 0.8s;
    -ms-transition: max-height 0.8s;
    -o-transition: max-height 0.8s;
    transition: max-height 0.8s;
}

.expand-btn {
    height: 25px;
    width: 100%;
    background-color: #ddd;
    border-radius: 0 0 5px 5px;
    position: absolute;
    bottom: 0;
    p {
        font-size: 0.9em;
        margin: 2px 0 2px 25px;
        // text-align: left;
    }
    p:hover {
        cursor: pointer;
    }
    .ico {
        vertical-align: -12%;
        // font-size: 32px;
        @media (max-width: $mediaSmall) {
            vertical-align: -20%;
        }
    }
    svg {
        height: 22px;
    }
}

.collapsed {
    max-height: 250px !important;
    height: 550px;
}
.hidden {
    display: none;
}
</style> 
