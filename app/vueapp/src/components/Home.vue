<template>
    <div>
        <vue-nav></vue-nav>
    </div>
</template>

<script>
export default {
    name: "Home",
    data() {
        return {};
    },
    components: {
        vueNav: () => import("./Nav.vue")
    }
};
</script>

<style>

</style>
