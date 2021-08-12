<template>
  <div class='slot-machine'>
    <button @click='start'>start</button>
    <div class="slot-wrapper">
      <SingleSlot v-for='(slot, i) in slots' :items="slot.items" :ref="setSlotRef" :offset-amount="i">
        <template v-slot:title>{{ slot.title }}</template>
      </SingleSlot>
    </div>
  </div>
</template>

<script>
import SingleSlot from "@/components/SingleSlot";

export default {
  name: "SlotMachine",
  components: { SingleSlot },
  props: ["slots"],
  data () {
    return {
      slotRefs: [],
    }
  },
  methods: {
    start: function() {
      this.slotRefs.forEach((slotRef) => {
        slotRef.start();
      })
    },
    setSlotRef(slotRef) {
      if (slotRef) {
        this.slotRefs.push(slotRef);
      }
    }
  },
  beforeUpdate() {
    this.slotRefs = [];
  },
};
</script>

<style scoped>
.slot-machine {
  width: 100%;
}

.slot-wrapper {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: center;
  align-items: center;
}
</style>

