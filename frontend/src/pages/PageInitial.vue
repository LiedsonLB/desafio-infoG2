<template>
  <div id="app">
    <div id="screen-page-login">
      <div id="container-right">
        <button @click="toggleForm('login')">Login</button>
        <button @click="toggleForm('cadastro')">Cadastro</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageInitialApp",
  data() {
    return {
      mostrarDiv: true,
    };
  },
  methods: {
    toggleForm(option) {
      if (option === "login") {
        console.log("Formulário de login exibido");
      } else if (option === "cadastro") {
        console.log("Formulário de cadastro exibido");
      }
    },
  },
};
</script>

<style scoped>
#screen-page-login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

#container-right button {
  margin: 5px;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}
</style>
