<script setup>
import { Icon } from '@iconify/vue'
</script>

<template>
  <footer>
    <div class="logo">Mamba Mentality</div>

    <div class="icons">
      <a href="https://github.com/Ochoja"><Icon icon="mdi:github" /></a>
      <a href="https://www.instagram.com/daniel_ochoja/"><Icon icon="ri:instagram-fill" /></a>
      <a href="https://www.linkedin.com/in/daniel-ochoja-951b03232/"
        ><Icon icon="mdi:linkedin"
      /></a>
      <a href="https://www.upwork.com/freelancers/~0168a779cdf58e1da2"
        ><Icon icon="bxl:upwork"
      /></a>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  background: #000;
  margin-top: 150px;
  padding: 15px 30px;

  .logo {
    font-size: 1.1em;
    font-weight: 600;
  }

  .icons {
    display: flex;
    gap: 5px;

    a {
      color: #fff;
      font-size: 2em;
    }

    a:hover {
      color: var(--secondary-color);
    }
  }
}
</style>
