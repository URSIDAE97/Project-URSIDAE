<template>
  <div style="height: 100%; width: 100%; display: flex;">
    <div style="margin: auto;">
      <breeding-rhombus-spinner
        :animation-duration="2000"
        :size="80"
        color="#f0f0f0" />
      <div class="uk-margin-xmedium-top">Loading ...</div>
    </div>
  </div>
</template>

<script>
import { BreedingRhombusSpinner } from 'epic-spinners'

export default {
  name: 'loading',

  components: {
    BreedingRhombusSpinner
  }
}
</script>