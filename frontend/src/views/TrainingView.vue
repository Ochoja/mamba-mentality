<script setup>
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
const route = useRoute()
const query = ref(route.params.query.replaceAll('+', " "))

watch(route, () => {
  query.value = route.params.query.replaceAll('+', ' ')
})
</script>

<template>
  <div class="trainings">
    <h1>{{ query }}</h1>
  </div>
</template>

<style lang="scss" scoped>
  h1{
    text-align: center;
    margin-top: 30px;
  }
</style>
