<script setup>
import { onMounted, ref, watch } from "vue";
import { useRoute } from "vue-router";
import axios from 'axios'

const route = useRoute()
const query = route.params.query
const title = ref(query.replaceAll('+', ' ')) //page title
const videos = ref({})

// change title when route is updated
watch(route, () => {
  title.value = query.replaceAll('+', ' ')
  getTraining()
})

async function getTraining() {
  try {
    const response = await axios.get(`http://127.0.0.1:5000/api/search/${query}`)
    console.log(response)
    videos.value = response.data
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  getTraining()
})

</script>

<template>
  <div class="trainings">
    <h1>{{ title }}</h1>
  </div>

  <div class="videos">
    {{ videos }}
  </div>
</template>

<style lang="scss" scoped>
  h1{
    text-align: center;
    margin-top: 30px;
  }
</style>
