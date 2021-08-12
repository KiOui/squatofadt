<template>
  <h2>
    <slot name="title"></slot>
  </h2>
  <div class='slot-window'>
    <div class='slot-wrapper' ref="slotWrapper">
      <div class='slot-item' v-for='item in items'>{{ item }}</div>
      <div class='slot-item slot-item__copy' >{{ items[0] }}</div>
    </div>
  </div>
</template>

<script>
const height = 200;

const next = window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.msRequestAnimationFrame ||
  window.oRequestAnimationFrame ||
  function(cb) { window.setTimeout(cb, 1000/60) }

export default {
  name: "SingleSlot",
  data() {
    return {
      startedAt: null,
      isFinished: true,
      duration: 0,
      startOffset: 0,
      height: 200,
      finalPos: 0,
    }
  },
  props: ["items", "offsetAmount"],
  methods: {
    start: function() {
      if (!this.isFinished) {
        return;
      }

      const choice = Math.floor(Math.random() * this.items.length);

      this.finalPos = choice * height;
      this.startOffset = 2000 + Math.random() * 500 + this.offsetAmount * 500;
      this.height = this.items.length * height;
      this.duration = 3000 + this.offsetAmount * 500;
      this.isFinished = false;

      next(this.animate);
    },
    animate: function(timestamp) {
      if (this.startedAt == null) {
        this.startedAt = timestamp;
      }
      const timeDiff = timestamp - this.startedAt;


      if (this.isFinished) {
        return;
      }

      const timeRemaining = Math.max(this.duration - timeDiff, 0);
      const offset = (Math.pow(timeRemaining, 3) / Math.pow(this.duration, 3)) * this.startOffset;

      // negative, such that slots move from top to bottom
      const pos = -1 * Math.floor((offset + this.finalPos) % this.height);

      this.$refs.slotWrapper.style.transform = "translateY(" + pos + "px)";

      if (timeDiff > this.duration) {
        this.isFinished = true;
      }

      if (this.isFinished) {
        this.startedAt = null;
      } else {
        next(this.animate);
      }

    }
  }
};
</script>

<style scoped>
.slot-window {
  background-color: green;
  width: 200px;
  height: 200px;
  overflow: hidden;
}

.slot-item {
  margin-top: 20px;
  height: 180px;
  width: 180px;
  padding: 0 10px;

  text-align: center;
  background-color: blue;
  color: white;

  line-height: 160px;
}
</style>