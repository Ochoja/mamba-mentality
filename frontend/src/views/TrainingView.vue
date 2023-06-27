<script setup>
import { ref } from 'vue'
import { useRoute } from "vue-router";
const route = useRoute()
const query = ref((route.params.query).replaceAll('+', " "))
console.log(query)
</script>

<template>
  <div class="about">
    <h1>{{ query }}</h1>
  </div>
</template>

<style>

</style>
