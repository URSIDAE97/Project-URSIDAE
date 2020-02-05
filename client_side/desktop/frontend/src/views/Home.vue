<template>
  <div class="home">
    <img alt="URSIDAE logo" src="../assets/logos/transparent_black.png" height="100px;">
    <TestComponent/>
  </div>
</template>


<script>
import TestComponent from '@/components/TestComponent.vue'

export default {
  name: 'home',
  components: {
    TestComponent
  }
}
</script>


<style scoped>

</style>