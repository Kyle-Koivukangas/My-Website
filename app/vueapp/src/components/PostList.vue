<template>
  <!-- <div class="postlist"> -->
        <transition-group mode="out-in"  
        tag="div" 
        class="postlist" 
        name="postlist" appear>
            <div    v-for="post in apiposts" :key="post.id" 
                    :id="convertID(post.id)"
                    class="post collapsed"
                    v-if="postShow[post.id] === true">
                <vue-post   
                            :postid="post.id" 
                            :slug="post.slug" 
                            :baseroute="'/blog/'"
                            @expand="postSelected($event)"
                            @collapse="reset()">

                    <div slot="head" class="post-head">
                        <h3>{{ post.title }}</h3>
                        <p>Date published: {{post.publish_date.split('T')[0]}}</p>
                    </div>

                    <div slot="content" class="post-content" v-html="post.content">
                    </div>
                             
                </vue-post>
            </div>
        </transition-group>
      
  <!-- </div> -->
</template>

<script>
export default {
    components: {
        vuePost: () => import("./Post.vue"),
    },
    props: ["apiposts", "baseroute"],
    data() {
        return {
            currentPost: {
                // currentPost just holds info about the current Post
            },
            postShow: {
                // PostShow object holds generated list of posts and
                // corresponding bool for whether they're visible.
            },
        };
    },
    computed: {},
    watch: {
        apiposts(newPosts, oldPosts) {
            // If the blog post info changes then this watcher will
            // generate a fresh postShow object.
            var postList = {};
            for (let i = 0; i < newPosts.length; i++) {
                postList[newPosts[i].id] = true;
            }
            this.postShow = postList;
            console.log("postShow updated.");

            // If api info or page is refreshed, this watcher will trigger
            // This is just a check to see if an article is selected, if it is it will run postSelected()
            const vm = this;
            if (this.$route.params.slug) {
                var post = this.getPostBySlug(this.$route.params.slug);
                this.currentPost = { id: post.id, slug: post.slug };
                setTimeout(function() {
                    console.log("apipostwatcher, running post selected");
                    vm.postSelected(post, true);
                    document.getElementById(vm.convertID(post.id)).classList.remove("collapsed");
                }, 50);
            }
        },
        $route(to, from) {
            console.log("route change detected");
            // console.log(to)

            if (to.params.slug === this.currentPost.slug) {
                console.log("slugs match");
                this.postSelected(this.currentPost, true);
            } else if (to.params.slug) {
                console.log("Slugged but not match with previous article..");
                var post = this.getPostBySlug(this.$route.params.slug);
                console.log(post);
                this.currentPost = { id: post.id, slug: post.slug };
                this.postSelected(this.currentPost, true);
            } else {
                console.log("slugs dont match");
                this.reset(true);
            }
        },
    },
    methods: {
        postSelected(postInfo, noLoop = false) {
            // Takes an object containing info about the post that was selected
            // then handles the procedure to display post
            // (hide other posts, expand post, push to router).
            this.currentPost = postInfo;
            // noLoop stops infinite looping, use when called from watchers
            this.hideOtherPosts(postInfo.id);
            if (noLoop === false) {
                this.$router.push(this.baseroute + postInfo.slug);
            }
            // Timeout is to circumvent some issues when running all at once..
            const vm = this;
            setTimeout(function() {
                document.getElementById(vm.convertID(postInfo.id)).classList.remove("collapsed");
            }, 1);
        },
        hideOtherPosts(postID) {
            // Sets postShow values to false except for selected postID that is passed in.
            for (let post in this.postShow) {
                if (post == postID) {
                    this.postShow[post] = true;
                } else {
                    this.postShow[post] = false;
                }
            }
        },
        reset(noLoop = false) {
            // Resets the  router route, postShow values, and collapses posts.
            // this.currentPost = {};
            // noLoop stops infinite looping, use when called from watchers
            if (noLoop === false) {
                this.$router.push(this.baseroute);
            }

            for (let post in this.postShow) {
                this.postShow[post] = true;
            }

            var posts = document.getElementsByClassName("post");
            for (let i = 0; i < posts.length; i++) {
                posts[i].classList.add("collapsed");
            }
            console.log("RESET");
        },
        getPostBySlug(slug) {
            var result = this.apiposts.filter(function(obj) {
                return obj.slug == slug;
            });
            console.log("getPostBySlug:");
            console.log(result[0]);
            return result[0];
        },
        convertID(postID) {
            return "post-" + postID;
        },
    },
    mounted() {
        console.log(`Mounted PostList`);
        // console.log(this.$route.params);
        if (this.$route.params.slug) {
            console.log("slug detected");
        }
    },
    created() {
        console.log("Created PostList");
    },
    // enter: function(el, done) {
    //     var delay = el.dataset.index * 150;
    //     setTimeout(function() {
    //         Velocity(el, { opacity: 1 }, { complete: done });
    //     }, delay);
    // },
    // leave: function(el, done) {
    //     var delay = el.dataset.index * 150;
    //     setTimeout(function() {
    //         Velocity(el, { opacity: 0, height: 0 }, { complete: done });
    //     }, delay);
    // },
    // move: function(el, done) {
    //     velocity(el, { transition: '1s ease' }, { complete: done});
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

.postlist {
    margin: auto;
    // height: 500px;
    width: $contentSize;
    // background-color: blue;
    // overflow: auto;
}

.post {
    margin: auto;
    margin-top: 25px;
    min-height: 250px;
    max-height: 1550px;
    max-width: $contentSize;
    background-color: #eee;
    border-radius: 5px;
    position: relative;
    overflow: hidden;
    // padding: 10px;

    $transitionTime: 1s;
    -webkit-transition: max-height $transitionTime;
    -moz-transition: max-height $transitionTime;
    -ms-transition: max-height $transitionTime;
    -o-transition: max-height $transitionTime;
    transition: max-height $transitionTime;
}
.post-head {
    text-align: left;
    display: flex;
    justify-content: space-between;
    background-color: #ddd;
    border-bottom: 1px dotted $grey;
    h3 {
        margin: 10px 0 8px 10px;
    }
    p {
        margin: 10px 10px 0 0;
        text-align: right;
        font-size: 0.7em;
        color: grey;
    }
}
.post-description {
    margin: auto 1em;
    text-align: left;
}
.post-content {
    margin: auto 1em;
    text-align: left;
}

.collapsed {
    max-height: 250px !important;
    // height: 550px;
}
// .list-enter-active {
//     transition: 1s ease;
// }

// .list-leave-active {
//     transition: opacity 1s ease;
//     position: absolute;
// }

// .list-enter {
//     transition: opacity 1s ease;
// }
// .list-leave-to {
//     opacity: 0;
//     background-color: #eee;
//     transform: translateY(10px);
// }

// .list-move {
//     transition: 1s ease-out;
// }

// .postlist-item {
//   display: inline-block;
//   margin-right: 10px;
// }
.post {
    transition: all 1s;
    display: block;
    // margin-right: 10px;
}
.postlist-enter-active,
.list-leave-active {
    transition: all 1s;
}
.postlist-move {
    transition: all 1s ease;
}
.postlist-enter,
.postlist-leave-to {
    opacity: 0;
    transform: translateZ(30px);
}
.postlist-leave-active {
    position: absolute;
}
</style>
