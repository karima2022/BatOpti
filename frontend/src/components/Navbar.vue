<template>
  <div class="nav-menu">
    <i class="fas fa-bars" v-if="isAuthenticated" @click="toggleMenu"></i>
    <div class="nav-content" :class="showMobileMenu ? 'open-menu' : 'closed-menu'">
      <div class="logo">
        <img src="../assets/logo.png" alt="Logo">
      </div>
      <!-- Menu pour les utilisateurs connectés -->
      <ul v-if="isAuthenticated" class="nav-items">
        <li><router-link to="/batiments">Bâtiments</router-link></li>
        <li><router-link to="/tickets">Tickets</router-link></li>
        <li><router-link to="/audits">Audits</router-link></li>
        <li><router-link to="/projets">Projets</router-link></li>
      </ul>
      <button v-if="isAuthenticated" class="login-button" @click="logout">Logout</button>

      <!-- Boutons pour les utilisateurs non connectés -->
      <div v-else class="auth-buttons">

        <router-link to="/register" class="login-button">S'enregistrer</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      showMobileMenu: false,
    };
  },
  computed: {
    // Vérifie si l'utilisateur est connecté
    isAuthenticated() {
      return !!localStorage.getItem("access"); // Retourne true si "access" existe
    },
  },
  methods: {
    toggleMenu() {
      this.showMobileMenu = !this.showMobileMenu;
    },
    logout() {
      // Supprime les tokens pour déconnecter l'utilisateur
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      this.$router.push("/login"); // Redirige vers la page de connexion
    },
  },
};
</script>

<style lang="scss" scoped>
.nav-menu {
  background-color: #333;
  color: white;
  position: relative;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.logo img {
  width: 120px;
  filter: brightness(1) invert(1);
}

.nav-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.nav-items {
  display: flex;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-items li {
  padding: 10px 0;
}

.nav-items li a {
  color: white;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-items li a:hover {
  color: #1e90ff;
}

.login-button {
  background-color: #1e90ff;
  padding: 8px 15px;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
  text-decoration: none; /* Pour les liens */
}

.login-button:hover {
  background-color: #145ba1;
}

i {
  font-size: 1.5rem;
  cursor: pointer;
  display: none;
}

/* Styles pour la version mobile */
@media screen and (max-width: 768px) {
  .nav-menu {
    padding-top: 10px;
  }

  .nav-content {
    flex-direction: column;
    align-items: flex-start;
    background-color: #333;
    position: absolute;
    top: 50px;
    left: 0;
    width: 100%;
    transition: max-height 0.3s ease;
    overflow: hidden;
    max-height: 0;
  }

  .open-menu {
    max-height: 200px; /* Ajuste la hauteur selon la taille du contenu */
  }

  .nav-items {
    flex-direction: column;
    width: 100%;
    text-align: center;
  }

  .nav-items li {
    padding: 10px;
    width: 100%;
  }

  i {
    display: block;
    color: white;
  }
}
</style>
