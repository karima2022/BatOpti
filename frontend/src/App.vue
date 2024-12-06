<template>
  <NavBar v-if="!isAuthPage" />

  <div id="app">
    <router-view />
  </div>
</template>

<script>
import './assets/tailwind.css'; 
import NavBar from './components/Navbar.vue'; 

export default {
  name: 'App',
  components: {
    NavBar,
  },
  computed: {
    isAuthPage() {
      const authPages = ['/login', '/register'];
      return authPages.includes(this.$route.path);
    },
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  color: #333;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@media (prefers-color-scheme: light) {
  .logo {
    filter: invert(1) hue-rotate(180deg); 
  }
}

.kanban-board {
  display: flex;
  justify-content: space-around;
  padding: 20px;
  min-height: 100vh;
}

.kanban-column {
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  width: 30%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 2px solid transparent;
  transition: border 0.2s ease;
}

.kanban-column:hover {
  border: 2px solid #007bff;
}

.column-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 15px;
  text-align: center;
  color: #444;
  border-bottom: 2px solid #e4e4e4;
  padding-bottom: 5px;
}

.kanban-card {
  background: #f9f9f9;
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.kanban-card:active {
  transform: scale(1.05);
}

.card-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.card-description {
  font-size: 14px;
  color: #666;
}

.kanban-card:hover {
  background: #eaf6ff;
  cursor: pointer;
}

</style>

