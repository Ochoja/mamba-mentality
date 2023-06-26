<script setup>
import { ref } from 'vue'
import Button from './DynamicButton.vue'
import TrainingModal from './TrainingModal.vue'

const isModalOpen = ref(false)

const closeModal = () => (isModalOpen.value = false)
</script>

<template>
  <nav>
    <div class="logo">Mamba Mentality</div>
    <Button @click="isModalOpen = true">Improve My Game</Button>
  </nav>

  <Teleport to="body" v-if="isModalOpen">
    <TrainingModal @closeModal="closeModal"></TrainingModal>
  </Teleport>
</template>

<style lang="scss" scoped>
nav {
  background-color: black;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;

  .logo {
    color: #fff;
    font-size: 1.3em;
    font-weight: 600;
  }
}
</style>
