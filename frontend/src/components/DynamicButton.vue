<script setup>
defineProps({
  type: String
})
</script>

<template>
  <button v-if="type == 'danger'" class="danger">
    <slot>Click Me!</slot>
  </button>
  <button v-else>
    <slot>Click Me!</slot>
  </button>
</template>

<style>
button {
  background: var(--secondary-color);
  color: #000;
  border-radius: 4px;
  padding: 9px 16px;
  border: none;
  font-weight: 700 !important;
  cursor: pointer;
}

.danger {
  background: #ff0000;
  color: #fff;
}
</style>
