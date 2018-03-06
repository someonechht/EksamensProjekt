<template>
  <div class="terminal">
    <ul>
      <div class="output">
      <li v-for="(line, index) in lines" :key="index">{{ line }}</li>
      </div>
      <li>
      <input class="input" v-model="input" type="text" @keyup.enter="exec()">
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Terminal',
  data: () => {
    return {
      lines: [],
      input: ''
    }
  },
  methods: {
    exec () {
      var args = this.input.split(' ')
      if (args.lenght === 0) {
        return
      }

      this.lines.push(this.input)

      if (args[0] === 'clear') {
        this.lines = []
      }

      this.input = ''
    }
  }
}
</script>

<style lang="stylus" scoped>
.terminal
  width: 30rem
  margin: 0 auto
  border: 1px solid black
  text-align: left
  ul
    padding: .5em
    list-style-type: none
    margin: 0
  .output
    height: 15em
    overflow: scroll
.input
  list-style-type: none
  width: 100%
  abox-sizing: border-box
  border: none
  outline: none
  position: relative
  bottom: 0
</style>
