<template>
<div>
    <div class="banner">
        <div class="header-container">
            <h1>Blog</h1>
        </div>
    </div>
    <div class="content">
        <vue-post-list :apiposts="apiBlogPosts" :baseroute="'/blog/'"></vue-post-list>
    </div>
    <vue-footer/>
</div>
  
</template>

<script>
import axios from "axios";

export default {
    components: {
        vueFooter: () => import("./Footer.vue"),
        vuePostList: () => import("./PostList.vue"),
    },
    data() {
        return {
            errors: [],
            apiBlogPosts: [
                {
                    id: 3,
                    title: "test blog post number TWO",
                    slug: "test-blog-post-number-two",
                    content:
                        "<p><em><strong>This is just a test, people.</strong></em></p>\n<p>Lorem ipsum dolor sit amet consectetur adisadas sasad asd asd asd asd asds ada sd d asd asd asd asdasd asd asd spisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus asdasdas dassad d asd asd asd aseaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>\n<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.</p>",
                    publish_date: "2018-02-19T00:07:50Z",
                    expiry_date: null,
                    related_posts: [],
                    featured_image: "",
                    status: 2,
                    _meta_title: "Test Blog Post2",
                    description:
                        "This is just a test, people. lorem ipsumLorem ipsum dolor sit amet consectetur adipisicing elit. Quam a sit iste voluptatibus eaque placeat inventore dicta cum repellat aperiam! Fuga quaerat eaque quisquam quo, voluptate necessitatibus assumenda. Debitis, rerum.",
                    keywords: [],
                    comments: [
                        {
                            id: 8,
                            user_name: "Kyle Koivukangas",
                            comment: "mmmyesss, very naice.",
                            replied_to: 0,
                            replied_to_content: "None",
                            submit_date: "2018-02-19T08:08:54.029360Z",
                            by_blog_author: true,
                        },
                        {
                            id: 10,
                            user_name: "Kyle Koivukangas",
                            comment: "Ju liek?",
                            replied_to: 8,
                            replied_to_content: "Kyle Koivukangas: mmmyesss, very naice....",
                            submit_date: "2018-02-19T08:09:48.698886Z",
                            by_blog_author: true,
                        },
                        {
                            id: 11,
                            user_name: "yoyoyo",
                            comment: "Yo.",
                            replied_to: 8,
                            replied_to_content: "Kyle Koivukangas: mmmyesss, very naice....",
                            submit_date: "2018-02-19T08:39:27.412591Z",
                            by_blog_author: false,
                        },
                        {
                            id: 12,
                            user_name: "Nameen",
                            comment: "nowa'ameen?",
                            replied_to: 11,
                            replied_to_content: "yoyoyo: Yo....",
                            submit_date: "2018-02-19T08:40:29.261436Z",
                            by_blog_author: false,
                        },
                    ],
                },
                {
                    id: 1,
                    title: "Test Blog Post",
                    slug: "test-blog-post",
                    content:
                        '<h1>This is <em>my</em> <strong>TEST BLOG POST</strong>!</h1>\n<p></p>\n<blockquote>\n<p>I\'m testing out block quotes like this:</p>\n<p>I\'m such a \'blocky\' quote,</p>\n</blockquote>\n<p>no?</p>\n<blockquote>\n<pre>I even have code blocks in the block quote!<br>see!<br>&lt;a href="www.kylekoivukangas.com"&gt;Awesome Website&lt;/a&gt;<br><br></pre>\n</blockquote>\n<p></p>\n<div>hmm, this is supposedly a div.</div>\n<div>idk I don\'t see anything.</div>\n<div><img alt="Chick Magnet, yah" height="148" src="/media/uploads/chick_magnet.jpg" width="148"></div>\n<div>theres a pic, inside a div!</div>\n<div></div>\n<div>\n<table border="2" cellpadding="10" cellspacing="2" height="43" style="" width="895">\n<tbody>\n<tr>\n<td></td>\n<td></td>\n<td></td>\n<td></td>\n<td></td>\n</tr>\n<tr>\n<td>And</td>\n<td>a</td>\n<td>table</td>\n<td>of</td>\n<td>900px</td>\n</tr>\n</tbody>\n</table>\n</div>\n<p></p>\n<ul style="list-style-type: disc;">\n<li>Well I think that\'s good for now</li>\n<li>tested a lot of shit..</li>\n</ul>\n<p>Cya!</p>\n<p></p>',
                    publish_date: "2018-02-18T18:46:27Z",
                    expiry_date: null,
                    related_posts: [],
                    featured_image: "",
                    status: 2,
                    _meta_title: "Test Blog Post",
                    description: "This is my TEST BLOG POST!\n",
                    keywords: ["test"],
                    comments: [
                        {
                            id: 2,
                            user_name: "Kyle Koivukangas",
                            comment: "Ahaaaahh. sahhh dude",
                            replied_to: 1,
                            replied_to_content: "Kyle Koivukangas: Suh dude....",
                            submit_date: "2018-02-19T06:18:40.342710Z",
                            by_blog_author: true,
                        },
                        {
                            id: 3,
                            user_name: "Kyle Koivukangas",
                            comment: "doink",
                            replied_to: 0,
                            replied_to_content: "None",
                            submit_date: "2018-02-19T06:18:55.826037Z",
                            by_blog_author: true,
                        },
                        {
                            id: 4,
                            user_name: "Kyle Koivukangas",
                            comment: "uhhh",
                            replied_to: 0,
                            replied_to_content: "None",
                            submit_date: "2018-02-19T06:19:10.066722Z",
                            by_blog_author: true,
                        },
                        {
                            id: 5,
                            user_name: "Kyle Koivukangas",
                            comment: "the sky, man. the sky.",
                            replied_to: 2,
                            replied_to_content: "Kyle Koivukangas: Ahaaaahh. sahhh dude...",
                            submit_date: "2018-02-19T06:19:45.034055Z",
                            by_blog_author: true,
                        },
                        {
                            id: 6,
                            user_name: "Kyle Koivukangas",
                            comment: "niice",
                            replied_to: 2,
                            replied_to_content: "Kyle Koivukangas: Ahaaaahh. sahhh dude...",
                            submit_date: "2018-02-19T06:26:58.203487Z",
                            by_blog_author: true,
                        },
                        {
                            id: 7,
                            user_name: "Kyle Koivukangas",
                            comment: "gud on u m8",
                            replied_to: 6,
                            replied_to_content: "Kyle Koivukangas: niice...",
                            submit_date: "2018-02-19T06:27:27.347492Z",
                            by_blog_author: true,
                        },
                        {
                            id: 14,
                            user_name: "",
                            comment: "yoyoyo",
                            replied_to: 0,
                            replied_to_content: "None",
                            submit_date: "2018-02-19T09:12:51.720230Z",
                            by_blog_author: false,
                        },
                    ],
                },
            ],
            expanded: false,
        };
    },
    created() {
        // check if dev environment or not, if dev then use dev or staging API.
        if (window.location.origin === "http://localhost:8080") {
            axios
                .get(
                    // Use all access CORS workaround to access staging API.
                    "https://allorigins.me/get?method=raw&url=" +
                        encodeURIComponent("https://staging.kylekoivukangas.com/api/blogposts/") +
                        "&callback=?"
                    // Use django dev server API.
                    // "http://127.0.0.1:8000/api/blogposts/"
                )
                .then(response => {
                    console.log("response received");
                    console.log(response);
                    this.apiBlogPosts = response.data;
                })
                .catch(error => {
                    this.errors.push(error);
                });
        } else if (window.location.origin === "https://staging.kylekoivukangas.com") {
            axios
                .get("https://staging.kylekoivukangas.com/api/blogposts/")
                .then(response => {
                    console.log("response received");
                    console.log(response);
                    this.apiBlogPosts = response.data;
                })
                .catch(error => {
                    this.errors.push(error);
                    this.apiFailed = true;
                });
        } else {
            axios
                .get("https://kylekoivukangas.com/api/blogposts/")
                .then(response => {
                    console.log("response received");
                    console.log(response);
                    this.apiBlogPosts = response.data;
                })
                .catch(error => {
                    this.errors.push(error);
                    this.apiFailed = true;
                });
        }
    },
};
</script>

<style lang="scss" scoped>
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
            // text-shadow: 0px 0px 3px #000;
        }
    }
}

</style>
