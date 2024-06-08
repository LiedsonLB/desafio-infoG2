import App from '../App.vue';
import { createRouter, createWebHistory  } from 'vue-router';
import { createApp } from 'vue';

import initialPage from '../pages/PageInitial.vue';
import formSurvivor from '../components/formSurvivor.vue';
import ModalResources from '../components/modalResources.vue';

const routes = [
  {
    path: '/',
    name: 'initialPage',
    component: initialPage,
  },
  {
    path: '/modal',
    name: 'model',
    component: ModalResources,
  },
  {
    path: '/test',
    name: 'test',
    component: formSurvivor,
  },
];
const router = createRouter({
  history: createWebHistory (),
  routes
});

const app = createApp(App);
app.use(router);
app.mount('#app');

export default router;