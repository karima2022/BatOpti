import { createRouter, createWebHistory } from 'vue-router';

import BuildingsList from '../components/Building.vue';
import TicketsList from '../components/Ticket.vue'
import LoginPage from '../views/login.vue';
import RegisterPage from '../views/register.vue';
import DashboardPage from '@/views/dashboard.vue';
import BuildingDetail from '../components/BuildingDetail.vue';

const routes = [
  
  {
    path: "/",
    redirect: "/login", 
  },
  {
    path: '/batiments',
    name: 'Building',
    component: BuildingsList,
    meta: { requiresAuth: true },
  },
  { path: '/batiments/:id', name: 'BuildingDetail', component: BuildingDetail,  meta: { requiresAuth: true },},
  {
    path: '/tickets',
    name: 'Ticket',
    component: TicketsList,
    meta: { requiresAuth: true },
  },
  { path: '/login', name: 'LoginPage', component: LoginPage },
  { path: '/register', name: 'RegisterPage', component: RegisterPage },
  { path: "/dashboard", name: "DashboardPage", component: DashboardPage },];


const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('access'); 

  if (to.meta.requiresAuth && !isAuthenticated) {
    
    next('/login'); 
  } else {
    next(); 
  }
});

export default router;
