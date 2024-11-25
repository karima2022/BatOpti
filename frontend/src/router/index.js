import { createRouter, createWebHistory } from 'vue-router';

import BuildingsList from '../components/Building.vue';
import LoginPage from '../views/login.vue';
import RegisterPage from '../views/register.vue';
import DashboardPage from '@/views/dashboard.vue';

const routes = [
  
  {
    path: '/batiments',
    name: 'Building',
    component: BuildingsList
  },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  { path: "/dashboard", name: "DashboardPage", component: DashboardPage },];


const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
