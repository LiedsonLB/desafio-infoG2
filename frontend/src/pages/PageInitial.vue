<template>
  <div class="initial-page">
    <div class="container-initial">
      <div class="container-left-initial">
        <img id="background-initial" src="/img/backgroundImg.png" alt="" />
      </div>
      <div class="container-right-initial">
        <div class="container-form">
          <h1>ZSSN</h1>
          <h2>Sobrevivente Informe seus dados</h2>
          <form @submit.prevent="proceed">
            <span>
              <label class="container-input">
                <input
                  v-model="name"
                  type="text"
                  class="input"
                  placeholder="Nome"
                  autocomplete="off"
                />
              </label>
            </span>
            <span>
              <label class="container-input">
                <input
                  v-model="age"
                  type="text"
                  class="input"
                  placeholder="Idade"
                  autocomplete="off"
                />
              </label>
            </span>
            <span>
              <label class="container-input">
                <input
                  v-model="gender"
                  type="text"
                  class="input"
                  placeholder="Sexo"
                  autocomplete="off"
                />
              </label>
            </span>
            <span>
              <label class="container-input">
                <input
                  v-model="location"
                  type="text"
                  class="input"
                  placeholder="Última Localização"
                  autocomplete="off"
                />
              </label>
            </span>
            <div class="container-button-initial">
              <button type="submit" class="button-initial">Prosseguir</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <modal-resources v-if="showModal" :name="name" />
  </div>
</template>

<script>
import ModalResources from "@/components/modalResources.vue";

export default {
  name: "PageInitialApp",
  components: {
    ModalResources,
  },
  data() {
    return {
      name: "",
      age: "",
      gender: "",
      location: "",
      showModal: false,
    };
  },
  methods: {
    proceed() {
      if (this.name && this.age && this.gender && this.location) {
        this.showModal = true;
      } else {
        alert("Por favor, preencha todos os campos.");
      }
    },
  },
};
</script>
<style scoped>
.screen {
  height: 100%;
  min-height: 100vh;
}

.initial-page {
  min-height: 100vh;
}

.container-initial {
  display: flex;
  width: 100%;
  min-height: 100vh;
  flex-wrap: wrap;
  margin: 0 auto;
}

.container-left-initial {
  height: 100%;
  min-height: 100vh;
  position: relative;
  width: 50%;
}

.container-left-initial img {
  filter: brightness(0) drop-shadow(2px 4px 6px var(--color-black));
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.container-right-initial {
  width: 50%;
}

.container-form {
  width: 90%;
  height: 100%;
  margin: 0 auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.container-form h1 {
  color: var(--color-red);
  font-size: 6rem;
  padding: 0;
  margin: 1rem;
  filter: drop-shadow(2px 4px 6px var(--color-black));
}

.container-form h2 {
  font-family: var(--font-staatliches);
  color: var(--color-light-green);
  letter-spacing: 0.1rem;
  margin-bottom: 2rem;
  filter: drop-shadow(2px 4px 6px var(--color-black));
}

form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

form span label {
  margin: 0 auto;
}

.container-button-initial {
  width: 100%;
}

.container {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container-input {
  position: relative;
  display: block;
  min-width: 250px;
  max-width: 500px;
  display: flex;
  border-radius: var(--radious-defalt);
  border: 2px solid #373737;
  padding: 15px 0px 15px 20px;
  text-align: left;
  background-color: var(--color-white);
}

.container-input .input {
  outline: none;
  border: none;
  color: var(--color-light-gray);
  font-size: 16px;
  background-color: transparent;
  width: 100%;
}

.container-input .input:focus {
  border: none;
}

.container-input:has(.input:focus) {
  border: 2px solid var(--color-black);
  transition: 0.2s;
}

.button-initial {
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

.button-initial:hover {
  background-color: var(--hover-btn);
}
</style>
