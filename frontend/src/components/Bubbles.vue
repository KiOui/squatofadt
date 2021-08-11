<template>
  <canvas ref="canvas" :width="width" :height="height" style="position: fixed; top: 0; left: 0"></canvas>
</template>
<script>

import cloneDeep from "lodash";

export default {
  name: "Bubbles",
  data() {
    return {
      circles: [],
      requestAniId: null,
      width: window.innerWidth,
      height: window.innerHeight,
    }
  },
  props: {
    options: {
      type: Object,
      default: () => {
        return {}
      }
    }
  },
  computed: {
    opts() {
      let optionsClone = cloneDeep(
        this.options
      );
      return Object.assign({
        color: "rgba(255, 255, 255, 0.3)",
        radius: 30,
        density: 0.3,
        clearOffset: 0.8,
      }, optionsClone);
    },
  },
  methods: {
    randomColor () {
      let r = Math.floor(Math.random() * 255)
      let g = Math.floor(Math.random() * 255)
      let b = Math.floor(Math.random() * 255)
      let alpha = Math.random().toPrecision(2)
      return `rgba(${r}, ${g}, ${b}, ${alpha})`
    },
    resize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
    },
    animate() {
      let ctx = this.$refs.canvas.getContext("2d");
      cancelAnimationFrame(this.requestAniId)
      ctx.clearRect(0, 0, this.width, this.height)
      for (let i = 0; i < this.circles.length; i++) {
        this.circles[i].draw()
      }
      self.requestAniId = requestAnimationFrame(this.animate)
    }
  },
  mounted () {
    let ctx = this.$refs.canvas.getContext("2d"), settings = this.opts, that = this;
    for (let x = 0; x < this.width * settings.density; x++) {
      let c = new Circle()
      this.circles.push(c)
    }
    this.animate();
    function Circle () {
      let self = this
      this.pos = {}
      init()
      function init () {
        self.pos.x = Math.random() * that.width;
        self.pos.y = that.height + Math.random() * 100;
        self.alpha = 0.1 + Math.random() * settings.clearOffset;
        self.scale = 0.1 + Math.random() * 0.3;
        self.speed = Math.random();
        self.color = settings.color === 'random' ? that.randomColor() : settings.color
      }
      this.draw = function () {
        if (self.alpha <= 0) {
          init();
        }
        self.pos.y -= self.speed
        self.alpha -= 0.0005
        ctx.beginPath()
        ctx.arc(self.pos.x, self.pos.y, self.scale * settings.radius, 0, 2 * Math.PI, false)
        ctx.fillStyle = self.color
        ctx.fill()
        ctx.closePath()
      };
    }
  },
  beforeUnmount () {
    cancelAnimationFrame(this.requestAniId)
  },
  created() {
    window.addEventListener("resize", this.resize);
  },
  unmounted() {
    window.removeEventListener("resize", this.resize);
  },
};
</script>
