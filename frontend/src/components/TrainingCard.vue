<script setup>
import Button from './DynamicButton.vue'

defineProps({
  level: String,
  cta: String,
  description: String,
  background: String
})
</script>

<template>
  <div
    class="card"
    :style="{
      background: `linear-gradient(0deg, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.6)), url(${background})`
    }"
  >
    <div class="level">
      {{ level }}
    </div>
    <div class="description">
      {{ description }}
    </div>
    <Button :route="`/trainings/${level}+basketball+drills`">{{ cta }}</Button>
  </div>
</template>

<style lang="scss" scoped>
.card {
  max-width: 300px;
  padding: 35px;
  background-size: cover !important;
  background-position: center !important;
  background-repeat: no-repeat !important;
  color: #fff;
  border-radius: 4px;
  text-align: center;

  .level {
    font-size: 1.15em;
    font-weight: 700;
    margin-bottom: 20px;
  }

  .description {
    font-weight: 400;
    font-size: 1.05em;
    margin-bottom: 20px;
  }
}
</style>
