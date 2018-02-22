<template>
<div class="postview collapsed">
    <slot name='head'></slot>
    <slot name='image'></slot>
    <slot name='description'></slot>
    <slot name='content'></slot>
    <slot name='foot'></slot>
    <div class="expand-btn" @click="isOpen = !isOpen">
        <p v-if="isOpen == false">Expand <icon class="ico" name="caret-down" scale="2" label="Expand"></icon></p>
        <p v-if="isOpen == true">Collapse <icon class="ico" name="caret-up" scale="2" label="Collapse"></icon></p>
    </div>
</div>
  
</template>

<script>
import "vue-awesome/icons/caret-down";
import "vue-awesome/icons/caret-up";

export default {
    props: ['postid'],
    data() {
        return {
            isOpen: false,
        };
    },
    watch: {
        isOpen: function () {
            document.getElementById("blogpost"+this.postid).classList.toggle("collapsed");
        },
    },
    methods: {
        expandCurrentPost() {

        }
    }
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
</style> 
