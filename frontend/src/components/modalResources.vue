<template>
  <div class="modal">
    <div class="container-modal">
      <div class="header-modal">
        <button type="button" class="close-btn" @click="closeModal">×</button>
      </div>
      <div class="container-survivor-resource">
        <h2>
          <span>{{ name }}</span> Informe seu inventário de recursos:
        </h2>

        <section id="resource-list">
          <div class="resource" v-for="(count, resource) in resources" :key="resource">
            <h3>{{ resourceNames[resource] }}</h3>

            <svg v-html="icons[resource]"></svg>

            <div class="count-resource">
              <span class="prev-count" @click="updateCount(resource, false)"
                >&#10094;</span
              >
              <p>{{ count }}</p>
              <span class="next-count" @click="updateCount(resource, true)"
                >&#10095;</span
              >
            </div>
          </div>
        </section>

        <button type="button" class="send-resources" @click="sendResources">
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, defineComponent } from "vue";

export default defineComponent({
  props: {
    name: {
      type: String,
      required: true,
    },
  },
  setup() {
    const resources = ref({
      water: 0,
      food: 0,
      medicine: 0,
      ammo: 0,
    });

    const resourceNames = {
      water: "Água",
      food: "Alimentação",
      medicine: "Medicação",
      ammo: "Munição",
    };

    const icons = {
      water: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
                <path d="M120 0l80 0c13.3 0 24 10.7 24 24l0 40L96 64l0-40c0-13.3 10.7-24 24-24zM32 167.5c0-19.5 10-37.6 26.6-47.9l15.8-9.9C88.7 100.7 105.2 96 122.1 96l75.8 0c16.9 0 33.4 4.7 47.7 13.7l15.8 9.9C278 129.9 288 148 288 167.5c0 17-7.5 32.3-19.4 42.6C280.6 221.7 288 238 288 256c0 19.1-8.4 36.3-21.7 48c13.3 11.7 21.7 28.9 21.7 48s-8.4 36.3-21.7 48c13.3 11.7 21.7 28.9 21.7 48c0 35.3-28.7 64-64 64L96 512c-35.3 0-64-28.7-64-64c0-19.1 8.4-36.3 21.7-48C40.4 388.3 32 371.1 32 352s8.4-36.3 21.7-48C40.4 292.3 32 275.1 32 256c0-18 7.4-34.3 19.4-45.9C39.5 199.7 32 184.5 32 167.5zM96 240c0 8.8 7.2 16 16 16l96 0c8.8 0 16-7.2 16-16s-7.2-16-16-16l-96 0c-8.8 0-16 7.2-16 16zm16 112c-8.8 0-16 7.2-16 16s7.2 16 16 16l96 0c8.8 0 16-7.2 16-16s-7.2-16-16-16l-96 0z" />
              </svg>`,
      food: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                <path d="M416 0C400 0 288 32 288 176V288c0 35.3 28.7 64 64 64h32V480c0 17.7 14.3 32 32 32s32-14.3 32-32V352 240 32c0-17.7-14.3-32-32-32zM64 16C64 7.8 57.9 1 49.7 .1S34.2 4.6 32.4 12.5L2.1 148.8C.7 155.1 0 161.5 0 167.9c0 45.9 35.1 83.6 80 87.7V480c0 17.7 14.3 32 32 32s32-14.3 32-32V255.6c44.9-4.1 80-41.8 80-87.7c0-6.4-.7-12.8-2.1-19.1L191.6 12.5c-1.8-8-9.3-13.3-17.4-12.4S160 7.8 160 16V150.2c0 5.4-4.4 9.8-9.8 9.8c-5.1 0-9.3-3.9-9.8-9L127.9 14.6C127.2 6.3 120.3 0 112 0s-15.2 6.3-15.9 14.6L83.7 151c-.5 5.1-4.7 9-9.8 9c-5.4 0-9.8-4.4-9.8-9.8V16zm48.3 152l-.3 0-.3 0 .3-.7 .3 .7z" />
              </svg>`,
      medicine: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                    <path d="M64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H96V32H64zm64 0V480H448V32H128zM512 480c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H480V480h32zM256 176c0-8.8 7.2-16 16-16h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H272v48h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H272v48h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H272v48h32c8.8 0 16 7.2 16 16s-7.2 16-16 16H272c-8.8 0-16-7.2-16-16V240V192V144V96V48c0-8.8 7.2-16 16-16z" />
                  </svg>`,
      ammo: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M528 56c0-13.3-10.7-24-24-24s-24 10.7-24 24v8H32C14.3 64 0 78.3 0 96V208c0 17.7 14.3 32 32 32H42c20.8 0 36.1 19.6 31 39.8L33 440.2c-2.4 9.6-.2 19.7 5.8 27.5S54.1 480 64 480h96c14.7 0 27.5-10 31-24.2L217 352H321.4c23.7 0 44.8-14.9 52.7-37.2L400.9 240H432c8.5 0 16.6-3.4 22.6-9.4L477.3 208H544c17.7 0 32-14.3 32-32V96c0-17.7-14.3-32-32-32H528V56zM321.4 304H229l16-64h105l-21 58.7c-1.1 3.2-4.2 5.3-7.5 5.3zM80 128H464c8.8 0 16 7.2 16 16s-7.2 16-16 16H80c-8.8 0-16-7.2-16-16s7.2-16 16-16z"/></svg>`,
    };

    const updateCount = (resource, increment) => {
      if (increment) {
        resources.value[resource]++;
      } else {
        resources.value[resource] = Math.max(0, resources.value[resource] - 1);
      }
    };

    const sendResources = () => {
      console.log("Resources sent:", resources.value);
      // logic to send the resources
    };

    const closeModal = () => {
      // logic to close the modal
    };

    return {
      resources,
      resourceNames,
      icons,
      updateCount,
      sendResources,
      closeModal,
    };
  },
});
</script>

<style scoped>
.modal {
  -webkit-backdrop-filter: brightness(0.5);
  backdrop-filter: brightness(0.5);
  height: 100%;
  overflow: auto;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container-modal {
  animation: downAcess 0.3s ease-in-out;
  background: var(--color-dark-gray);
  border: none;
  border-radius: 20px;
  box-shadow: 20px 20px 50px #00000080;
  display: flex;
  flex-direction: column;
  height: auto;
  min-width: 30%;
  overflow-y: auto;
  padding: 20px;
  width: 60%;
  z-index: 3;
  margin: 0 auto;
  max-height: 80%;
  overflow: auto;
}

.header-modal {
  align-items: center;
  display: flex;
  justify-content: end;
  min-width: 200px;
  width: 100%;
  position: sticky;
  top: 0;
}

.close-btn {
  background-color: var(--color-red);
  border: none;
  border-radius: 5px;
  color: var(--color-white);
  cursor: pointer;
  font-family: sans-serif;
  font-size: 2rem;
  padding: 0.2rem 0.8rem;
  text-decoration: none;
}

.container-survivor-resource {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 0.5rem;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.container-survivor-resource h2 {
  font-family: var(--font-staatliches);
  color: var(--color-light-green);
  letter-spacing: 0.1rem;
  filter: drop-shadow(2px 4px 6px var(--color-black));
  max-width: 450px;
  text-align: center;
}

.container-survivor-resource span {
  color: var(--color-red);
}

#resource-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  justify-content: space-around;
  margin: 1rem 0;
  gap: 1rem;
  width: 70%;
}

.resource {
  background-color: var(--color-white);
  text-align: center;
  height: 200px;
  width: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  margin: 0 auto;
}

.resource h3 {
  color: var(--color-light-gray);
  font-family: var(--font-staatliches);
  font-weight: 500;
  font-size: 1.8rem;
}

.resource svg {
  max-height: 70px;
}

.count-resource {
  display: flex;
  width: 60%;
  justify-content: center;
}

.count-resource span {
  background-color: var(--color-red);
  color: var(--color-white);
  padding: 0.5rem 0.8rem;
  font-size: 1rem;
  cursor: pointer;
  user-select: none;
}

.count-resource span:hover {
  background-color: var(--hover-btn);
}

.count-resource p {
  background-color: var(--color-brown);
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
}

.prev-count {
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
}

.next-count {
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
}
.send-resources {
  background-color: #8a0303;
  color: #fff;
  padding: 15px 8px 15px 10px;
  font-size: 1.2rem;
  width: 100%;
  border-radius: var(--radious-defalt);
  font-weight: 500;
  font-family: var(--font-staatliches);
  text-decoration: none;
  cursor: pointer;
  line-height: 1;
  border: none;
  transition: 0.3s ease;
  text-align: center;
  margin: 1rem 0;
  min-width: 250px;
  max-width: 522px;
}

.send-resources:hover {
  background-color: var(--hover-btn);
}
</style>
