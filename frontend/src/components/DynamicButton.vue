<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

const props = defineProps({
  type: String, //changes style of button (eg danger)
  route: String //changes route eg <Button to="/training"></Button>
})

function goToPage(){
  router.push(`${props.route}`)
  console.log(props.route)
}
</script>

<template>
  <button v-if="type == 'danger'" class="danger">
    <slot>Click Me!</slot>
  </button>
  <button v-else-if="props.route" @click="goToPage()">
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
