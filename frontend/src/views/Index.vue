<template>
  <Bubbles style="z-index: -1;" class="fixed"></Bubbles>
  <div v-if="loading" class="fixed h-screen w-screen flex justify-center items-center flex-row">

  </div>
  <div class="flex justify-center items-center min-h-screen w-screen flex-row p-2 xl:p-10">
    <SlotMachine ref="slot-machine"></SlotMachine>
  </div>
  <footer v-if="true" class="fixed bottom-0 my-2 w-full block flex justify-center">
    <a href="https://github.com/KiOui/squatofadt" class="underline opacity-80 mx-auto text-black">Check the source code on GitHub</a>
  </footer>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Bubbles from "@/components/Bubbles.vue";
import SlotMachine from "@/components/SlotMachine.vue";
import ExerciseApiService from "@/common/exercise.api.service";
import shuffle from "@/util/shuffle";

@Options({
  name: "Index",
  data () {
    return {
      exercises: [],
      players: [],
      loadingExercises: true,
      loadingPlayers: true,
    }
  },
  components: {
    Bubbles,
    SlotMachine,
  },
  mounted() {
    ExerciseApiService.getGames().then((result) => {
      this.exercises = result;
      this.loadingExercises = false;
    }).catch(() => {
      window.alert("An error occurred while getting available games, please " +
        "refresh this page.");
    });
    ExerciseApiService.getPlayers().then((result) => {
      this.players = result;
      this.loadingPlayers = false;
    }).catch(() => {
      window.alert("An error occurred while getting available players, please " +
      "refresh this page.");
    })
  },
  computed: {
    loading: function() {
      return this.loadingPlayers && this.loadingExercises;
    }
  },
  methods: {
    start(event: Event) {
      if (this.games.length > 0) {
        this.nextGame();
        this.playing = true;
        this.startWheel();
        if (event) {
          event.stopPropagation();
        }
      }
      else {
        window.alert("There are no registered games, please refresh this page.")
      }
    },
    stop() {
      this.currentGame = this.games[this.currentGameIndex];
      this.stopWheel();
    },
    dismiss() {
      this.currentGame = null;
      this.showExplanation = false;
    },
    nextGame() {
      let nextGameIndex = this.currentGameIndex + 1;
      if (nextGameIndex >= this.games.length) {
        nextGameIndex = 0;
      }
      this.currentGameIndex = nextGameIndex;
    },
    startWheel() {
      this.games = shuffle(this.games);
      this.currentGameIndex = 0;
      this.intervalId = window.setInterval(this.nextGame, 250);
    },
    stopWheel() {
      clearInterval(this.intervalId);
      this.intervalId = null;
      this.playing = false;
    },
    getExplanationHeight() {
      return `${this.$refs.explanation.scrollHeight}px`;
    }
  }
})
export default class Index extends Vue {}
</script>

<style>

.jittery {
  animation: jittery 4s infinite;
}

.game-title {
  display: inline-block;
  transition: min-width 1s ease-in-out;
}

.toggle-explanation {
  position: relative;
  bottom: 0;
  overflow: hidden;
  transition: max-height .5s ease-in-out;
}

.explanation-container {
  overflow: hidden;
  transition: max-height 1s ease-in-out;
}

.explanation-container h1 {
  font-size: 2.25rem;
  line-height: 2.5rem;
  text-transform: uppercase;
  font-weight: bold;
}

.explanation-container h2 {
  font-size: 1.5rem;
  line-height: 2rem;
  text-transform: uppercase;
  font-weight: bold;
}

.explanation-container h3 {
  font-size: 1.125rem;
  line-height: 1.75rem;
  text-transform: uppercase;
}

.explanation-container h4, .explanation-container h5, .explanation-container h6 {
  font-weight: bold;
}

.explanation-container p {
  margin-bottom: 1rem;
}

.explanation-container ul, .explanation-container ol {
  margin-bottom: 1rem;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0;
  margin-inline-end: 0;
  padding-inline-start: 40px;
  display: block;
}

.explanation-container ul li {
  list-style-type: '\1F37A';
}

.explanation-container ul li, .explanation-container ol li {
  display: list-item;
  text-align: match-parent;
}

.explanation-container a {
  text-decoration: underline;
}

@keyframes jittery {
  5%,
  50% {
    transform: scale(1);
  }
  10% {
    transform: scale(0.9);
  }
  15% {
    transform: scale(1.15);
  }
  20% {
    transform: scale(1.15) rotate(-5deg);
  }
  25% {
    transform: scale(1.15) rotate(5deg);
  }
  30% {
    transform: scale(1.15) rotate(-3deg);
  }
  35% {
    transform: scale(1.15) rotate(2deg);
  }
  40% {
    transform: scale(1.15) rotate(0);
  }
}

</style>