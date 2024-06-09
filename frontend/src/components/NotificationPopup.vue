<template>
  <div v-if="isOpen" :id="'popup'" :class="type ? type : ''">
    <div id="text-popup">
      <h3 :class="['title-popup', type ? type : '']">{{ title }}</h3>
      <p class="mensagem-popup">{{ text }}</p>
    </div>
    <span id="closePopup" @click="handleClose">&times;</span>
  </div>
</template>

<script>
export default {
  name: "NotificacaoPopup",
  props: {
    type: {
      type: String,
      default: null,
    },
    title: {
      type: String,
      default: null,
    },
    text: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      isOpen: true,
    };
  },
  methods: {
    handleClose() {
      this.isOpen = false;
      this.$emit('close');
    },
  },
  mounted() {
    // this.startTimer(); // Remova esta linha
  },
};
</script>

<style scoped>
#popup {
  position: fixed;
  right: 1rem;
  top: 2rem;
  z-index: 10;
  border-radius: 5px;
  padding: 0.5rem;
  transition: 0.5s;
  animation: animatedPopup 0.5s ease-in;
  display: flex;
  gap: 10px;
  min-width: 250px;
  color: var(--color-white);
  background-color: var(--color-brown);
  font-family: var(--font-bebas);
  padding-left: 1rem;
}

#text-popup {
  color: var(--color-white);
  font-weight: 400;
  letter-spacing: 0.1rem;
}

#text-popup h3{
  font-family: var(--font-creepster);
  color: var(--color-red);
}

.mensagem-popup {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  max-width: 250px;
  max-height: 50px;
  overflow-x: auto;
}

.alert {
  background-color: var(--color-brown);
}

.warning {
  background-color: var(--color-brown);
}

.sucess {
  background-color: var(--color-brown);
}

.help {
  background-color: var(--color-brown);
}

#closePopup {
  font-family: var(--font-bebas);
  cursor: pointer;
  font-size: 32px;
  position: absolute;
  top: 0;
  right: 0.5rem;
  color: var(--color-white);
}

@keyframes animatedPopup {
  0% {
    opacity: 0;
    transform: translateX(200px);
  }

  100% {
    opacity: 1;
    transform: translateX(0px);
  }
}
</style>