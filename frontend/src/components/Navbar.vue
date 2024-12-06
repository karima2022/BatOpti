<template>
  <nav class="nav-menu">
    <!-- Icône de menu pour le mobile -->
    <i class="fas fa-bars menu-icon" v-if="isAuthenticated" @click="toggleMenu"></i>

    <!-- Contenu principal de la navigation -->
    <div class="nav-content" :class="{ 'open-menu': showMobileMenu }">
      <!-- Logo -->
      <div class="logo">
        <img src="../assets/logo.png" alt="Logo" />
      </div>

      <!-- Navigation pour utilisateurs connectés -->
      <ul v-if="isAuthenticated" class="nav-items">
        <li><router-link to="/batiments">Bâtiments</router-link></li>
        <li><router-link to="/tickets">Tickets</router-link></li>
        <li><router-link to="/audits">Audits</router-link></li>
        <li><router-link to="/projets">Projets</router-link></li>
      </ul>

      <!-- Boutons connexion/déconnexion -->
      <div v-if="isAuthenticated">
        <button class="action-button" @click="logout">Logout</button>
      </div>
      <div v-else class="auth-buttons">
        <router-link to="/login" class="action-button">Login</router-link>
        <router-link to="/register" class="action-button outlined">Register</router-link>
      </div>
    </div>
  </nav>
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
      return !!localStorage.getItem("access");
    },
  },
  methods: {
    toggleMenu() {
      this.showMobileMenu = !this.showMobileMenu;
    },
    logout() {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      this.$router.push("/login");
    },
  },
};
</script>


<style lang="scss" scoped>
.nav-menu {
  background: white; /* Fond blanc */
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Ombre légère */
  position: relative;
  z-index: 10;
}

.logo img {
  width: 120px;
  transition: transform 0.3s ease;
}

.logo img:hover {
  transform: scale(1.1);
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
  text-align: center;
}

.nav-items li a {
  text-decoration: none;
  color: #333; /* Couleur principale */
  font-weight: bold;
  font-size: 1rem;
  padding: 8px 15px;
  border-radius: 5px; /* Ajout d'arrondi pour les liens */
  transition: all 0.3s ease;
}

.nav-items li a:hover {
  color: white; /* Texte devient blanc */
  background: #2196f3; /* Fond bleu sur survol */
  transform: translateY(-2px); /* Animation légère */
}

.action-button {
  background-color: #ffcc00;
  color: #333;
  border: none;
  border-radius: 8px;
  font-size: 1em;
  padding: 10px 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: bold;
}

.action-button:hover {
  background-color: #e6b800;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}


.action-button.outlined {
  background: none;
  color: #4caf50;
  border: 2px solid #4caf50;
}

.action-button.outlined:hover {
  background: #4caf50;
  color: white;
}

/* Icône de menu pour le mobile */
.menu-icon {
  font-size: 1.8rem;
  color: #333; /* Icône devient gris foncé */
  cursor: pointer;
  display: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-content {
    flex-direction: column;
    align-items: flex-start;
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background: white; /* Fond blanc pour le menu mobile */
    transition: max-height 0.3s ease;
    overflow: hidden;
    max-height: 0;
    z-index: 1000;
  }

  .nav-content.open-menu {
    max-height: 300px; /* Ajustez selon le contenu */
  }

  .nav-items {
    flex-direction: column;
    width: 100%;
    text-align: center;
  }

  .nav-items li {
    width: 100%;
    padding: 10px 0;
  }

  .menu-icon {
    display: block;
  }

  .action-button {
    margin: 10px 0;
    width: calc(100% - 20px);
  }
}


</style>