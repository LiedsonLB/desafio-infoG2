<template>
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
    <div class="coordinates-container">
      <span>
        <label class="container-input-coordinates">
          <input
            v-model="latitude"
            type="text"
            class="input"
            placeholder="Latitude"
            autocomplete="off"
          />
        </label>
      </span>
      <span>
        <label class="container-input-coordinates">
          <input
            v-model="longitude"
            type="text"
            class="input"
            placeholder="Longitude"
            autocomplete="off"
          />
        </label>
      </span>
    </div>
    <div class="container-button-initial">
      <button type="submit" class="button-initial" @click="submitForm">
        Prosseguir
      </button>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "formSurvivor",
  components: {},
  data() {
    return {
      name: "",
      age: "",
      gender: "",
      latitude: "",
      longitude: "",
    };
  },
  methods: {
    async proceed() {
      if (this.isFormValid()) {
        try {
          // Convertendo latitude e longitude em numero
          const idade = parseFloat(this.age);
          const latitude = parseFloat(this.latitude);
          const longitude = parseFloat(this.longitude);

          const response = await axios.post(
            "http://127.0.0.1:8000/api/survivors/",
            {
              name: this.name,
              age: idade,
              gender: this.gender,
              last_location_latitude: latitude,
              last_location_longitude: longitude,
              infected: true,
              resources: [],
            }
          );
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      } else {
        alert("Por favor, preencha todos os campos.");
      }
    },
    isFormValid() {
      return (
        this.name && this.age && this.gender && this.latitude && this.longitude
      );
    },
  },
};
</script>
  
  <style scoped>
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
  border-radius: var(--radious-default);
  border: 2px solid #373737;
  padding: 15px 0px 15px 20px;
  text-align: left;
  background-color: var(--color-white);
}

.coordinates-container {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  max-width: 524px;
  margin: 0 auto !important;
  width: 100%;
}

.container-input-coordinates {
  position: relative;
  display: block;
  max-width: 500px;
  display: flex;
  border-radius: var(--radious-default);
  border: 2px solid #373737;
  padding: 15px 0px 15px 20px;
  text-align: left;
  background-color: var(--color-white);
}

.coordinates-container span {
  width: 50%;
}

.container-input .input,
.container-input-coordinates input {
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

.container-input:has(.input:focus),
.container-input-coordinates:has(input:focus) {
  border: 2px solid var(--color-black);
  box-shadow: 2px 4px 6px var(--color-red);
  transition: 0.2s;
}

.button-initial {
  background-color: #8a0303;
  color: #fff;
  padding: 15px 8px 15px 10px;
  font-size: 1.2rem;
  width: 100%;
  max-width: 524px;
  border-radius: var(--radious-default);
  font-weight: 500;
  font-family: var(--font-staatliches);
  text-decoration: none;
  cursor: pointer;
  line-height: 1;
  border: none;
  transition: 0.3s ease;
  text-align: center;
  margin: 1rem 0;
}

.button-initial:hover {
  background-color: var(--hover-btn);
}
</style>
  