<template>
<div class="post-child">
    <slot name='head'></slot>
    <slot name='image'></slot>
    <slot name='description'></slot>
    <slot name='content'></slot>
    <slot name='foot'></slot>
    <div class="expand-btn" @click="selectPost()">
        <p v-if="selected == false">Expand <icon class="ico" name="caret-down" scale="2" label="Expand"></icon></p>
        <p v-if="selected == true">Collapse <icon class="ico" name="caret-up" scale="2" label="Collapse"></icon></p>
    </div>
</div>

</template>

<script>
import "vue-awesome/icons/caret-down";
import "vue-awesome/icons/caret-up";

export default {
    props: ["postid", "slug", "baseroute", "collapse"],
    data() {
        return {
            selected: false,
        };
    },
    watch: {
        $route(to, from) {
            this.checkRouteForMatch()
        },
    },
    methods: {
        selectPost() {
            this.selected = !this.selected;
            if (this.selected === true) {
                this.$emit("expand", { id: this.postid, slug: this.slug });
            } else {
                this.$emit("collapse");
            }
        },
        checkRouteForMatch() {
            // Just to check if post has been selected via back/forward control and expand accordingly.
            if (this.$route.params.slug === this.slug) {
                this.selected = true;
            } else {
                this.selected = false;
            }
        },
    },
    created() {
        this.checkRouteForMatch()
    },
};
</script>

<style lang="scss">
.post-child {
    // margin: 10px;
    height: 100%;
    width: 100%;
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
        padding: 0px !important;
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

// Blog Post Formatting (using tags that mezzanine uses)
pre {
    border-radius: 3px;
    background-color: #ddd;
    border: solid 1px #ccc;
    padding: 5px;
}
blockquote {
    border-radius: 3px;
    background-color: #ddd;
    padding: 3px;
}
code {
    border-radius: 3px;
    background-color: #ddd;
    padding: 3px;
}
p {
    border-radius: 3px;
    padding: 5px;
}
.block-header {
    border-radius: 3px 3px 0 0;
    background-color: #ccc;
    text-align: center;
    padding: 5px
}
</style>
