<template>
  <div class='slot-machine'>
    <button @click='start'>start</button>
    <div class="slot-wrapper" ref="slots">
      <div class='slot' v-for='slot in slots'>
        <h2>{{ slot.title }}</h2>
        <div class='slot__window'>
          <div class='slot__wrap'>
            <div class='slot__item' v-for='opt in slot.items'>{{ opt }}</div>
            <div class='slot__item slot__item--copy' >{{ slot.items[0] }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const next = window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.msRequestAnimationFrame ||
  window.oRequestAnimationFrame ||
  function(cb) { window.setTimeout(cb, 1000/60) }

export default {
  name: "SlotMachine",
  data () {
    return {
      slots: [{
        title: "When",
        items: [
          "today",
          "next week",
          "last year",
          "tomorrow",
          "yesterday",
        ]
      }, {
        title: "Where",
        items: [
          "at home",
          "at work",
          "at school",
          "at the gym",
          "at the park",
          "at the beach",
          "at the sidewalk",
          "at the city",
        ]
      }, {
        title: "How",
        items: [
          "cycling",
          "walking",
          "swimming",
          "flying",
        ]
      }],
      opts: null,
      startedAt: null,
    }
  },
  methods: {
    start: function() {

      if (this.opts) {
        return
      }
      console.log(this.slots);
      this.opts = this.slots.map((data, i) => {

        const slot = this.$refs.slots.getElementsByClassName('slot')[i]
        console.log(`Slot: ${slot}`);
        console.log(this.$refs);
        console.log(this.$refs.slots);
        const choice = Math.floor(Math.random() * data.items.length)
        console.log("choice", i, data.items[choice])

        return {
          el: slot.querySelector('.slot__wrap'),
          finalPos: choice * 180,
          startOffset: 2000 + Math.random() * 500 + i * 500,
          height: data.items.length * 180,
          duration: 3000 + i * 700, // milliseconds
          isFinished: false,
        }

      })

      next(this.animate)

    },

    animate: function(timestamp) {

      if (this.startedAt == null) {
        this.startedAt = timestamp
      }

      const timeDiff = timestamp - this.startedAt

      this.opts.forEach(opt => {

        if (opt.isFinished) {
          return
        }

        const timeRemaining = Math.max(opt.duration - timeDiff, 0)
        const power = 3
        const offset = (Math.pow(timeRemaining, power) / Math.pow(opt.duration, power)) * opt.startOffset

        // negative, such that slots move from top to bottom
        const pos = -1 * Math.floor((offset + opt.finalPos) % opt.height)

        opt.el.style.transform = "translateY(" + pos + "px)"

        if (timeDiff > opt.duration) {
          console.log('finished', opt, pos, opt.finalPost)
          opt.isFinished = true
        }

      })

      if (this.opts.every(o => o.isFinished)) {
        this.opts = null
        this.startedAt = null
        console.log('finished')
      } else {
        next(this.animate)
      }

    }
  }
};
</script>

<style scoped>
.slot {
  float: left;
  margin: 0.4em;
}

.slot__window {
  background-color: green;
  width: 200px;
  height: 200px;
  overflow: hidden;
}

.slot__wrap {

}

.slot__item {
  margin-top: 20px;
  height: 160px;
  width: 180px;
  padding: 0 10px;

  text-align: center;
  background-color: blue;
  color: white;

  line-height: 160px;
}

.slot__item--copy {
}
</style>

