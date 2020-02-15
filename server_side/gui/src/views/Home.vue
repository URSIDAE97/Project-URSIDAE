<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/img/logo_transparent_white.png">
    <HelloWorld msg="Welcome to URSIDAE!!!"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
