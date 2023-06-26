<script setup>
import { RouterView } from 'vue-router'
import Navigation from './components/NavBar.vue'
import Footer from './components/SiteFooter.vue'
</script>

<template>
  <Navigation></Navigation>
  <RouterView />
  <Footer></Footer>
</template>

<style>
@import './assets/main.css';
</style>
