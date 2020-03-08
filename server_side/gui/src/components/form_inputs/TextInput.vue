<template>
  <span class="text-input">
    <span
      v-if="icon !== ''"
      :uk-icon="'icon: ' + icon + '; ratio: 0.9;'"
      class="uk-margin-small-right uk-margin-xmedium-top"
    ></span>
    <md-field :class="{ 'md-invalid' : error }" autocomplete="off">
      <label>{{ label }}</label>
      <md-input
        v-model="text"
        :maxlength="maxlength"
        :type="type"
        @keypress.enter="$emit('enter')"
      ></md-input>
    </md-field>
  </span>
</template>

<script>
export default {
  name: 'text-input',

  props: {
    // label of the text input
    label: {
      type: String,
      default: 'Label'
    },
    // icon displayed before the text input
    // (if empty no icon is displayed)
    icon: {
      type: String,
      default: ''
    },
    // mark the text input as invalid
    error: {
      type: Boolean,
      default: false
    },
    // value of the text input
    value: {
      type: String,
      required: true
    },
    // maximal length of the text input
    // (if null no limit is applied)
    maxlength: {
      type: Number,
      default: null
    },
    type: {
      type: String,
      default: 'text',
      validator: function (value) {
        return ['text', 'password'].indexOf(value) !== -1
      }
    }
  },

  data () {
    return {
      text: this.value
    }
  },

  watch: {
    text: function () {
      this.$emit('input', this.text)
    }
  }
}
</script>

<style scoped>
.text-input {
  display: flex;
}
</style>