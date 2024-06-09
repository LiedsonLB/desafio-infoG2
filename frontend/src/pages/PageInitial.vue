<template>
  <div class="initial-page">
    <div class="container-initial">
      <div class="container-left-initial">
        <img id="background-initial" src="/img/backgroundImg.png" alt="" />
      </div>
      <div class="container-right-initial">
        <div class="container-form">
          <h1>ZSSN</h1>
          <h2>Sobrevivente, informe seus dados</h2>
          <FormSurvivor @formSubmitted="handleFormSubmission" />
        </div>
        <footer>
          Todos os direitos reservados © ZSSN - Liedson Barros 2024
        </footer>
      </div>
    </div>
    <NotificacaoPopup
      v-if="showPopup"
      :type="popupType"
      :title="popupTitle"
      :text="popupText"
      @close="handlePopupClose"
    />
    <ModalResources
      v-if="showModalResouces"
      @close="handleModalResourcesClose"
      :name="name"
    />
  </div>
</template>

<script>
import FormSurvivor from "@/components/formSurvivor.vue";
import ModalResources from "@/components/modalResources.vue";
import NotificacaoPopup from "@/components/NotificationPopup.vue";

export default {
  name: "PageInitialApp",
  components: {
    ModalResources,
    NotificacaoPopup,
    FormSurvivor,
  },
  data() {
    return {
      name: "",
      age: "",
      gender: "",
      location: "",
      showModalResouces: false,
      showPopup: false,
      popupType: "alert",
      popupTitle: "Atenção",
      popupText: "Por favor, preencha todos os campos.",
    };
  },
  methods: {
    handleFormSubmission(data) {
      if (!data.formValid) {
        this.showPopup = true;
        setTimeout(() => {
          this.showPopup = false;
        }, 3000);
        return;
      }
      this.showModalResouces = true;
    },
    handlePopupClose() {
      this.showPopup = false;
    },
    handleModalResourcesClose() {
      this.showModalResouces = false;
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
  height: calc(100% - 30px);
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

footer {
  width: 100%;
  text-align: center;
  font-family: var(--font-bebas);
  color: var(--color-white);
}
</style>
