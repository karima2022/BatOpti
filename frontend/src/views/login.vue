<template>
  <div class="login-page">
    <div class="login-card">
      <div class="login-header">
<!--        <img src="../assets/bat.webp" alt="Illustration du bâtiment" class="login-image" />-->
        <h2>Bienvenue sur BatOpti</h2>
        <p>Connectez-vous pour gérer vos bâtiments lol et projets</p>
      </div>
      <form @submit.prevent="login" class="login-form">
        <div class="form-group">
          <input
              type="text"
              v-model="username"
              placeholder="Nom d'utilisateur"
              required
              class="form-control"
          />
        </div>
        <div class="form-group">
          <input
              type="password"
              v-model="password"
              placeholder="Mot de passe"
              required
              class="form-control"
          />
        </div>
        <button type="submit" class="login-button">Se connecter</button>
        <p v-if="error" class="error-message">{{ error }}</p>
      </form>
      <div class="login-footer">
        <router-link to="/forgot-password" class="link">Mot de passe oublié ?</router-link>
        <router-link to="/register" class="link">Créer un compte</router-link>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: "LoginPage",
  data() {
    return {
      username: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/auth/login/', {
          username: this.username,
          password: this.password,
        });
        localStorage.setItem('access', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);
        this.$router.push('/dashboard');
      } catch (err) {
        this.error = 'Connexion échouée. Vérifiez vos identifiants.';
      }
    },
  },
};
</script>
<style scoped lang="scss">
.login-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-image: url('@/assets/21560.jpg');
  background-size: cover;

  background-repeat: no-repeat;

  font-family: 'Roboto', sans-serif;
}

.login-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 380px;
}

.login-header {
  margin-bottom: 20px;
}

.login-image {
  max-width: 100%;
  height: auto;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}

.login-form .form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 14px;
  outline: none;
  transition: border 0.3s;
}

.form-control:focus {
  border: 1px solid #ffcc00; /* Couleur inspirée des équipements de sécurité */
}

.login-button {
  width: 100%;
  padding: 12px;
  background-color: #ffcc00; /* Couleur vive rappelant les chantiers */
  color: #333;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #e6b800;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.login-footer {
  margin-top: 20px;
}

.link {
  display: block;
  color: #ffcc00;
  margin: 5px 0;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s;
}

.link:hover {
  color: #e6b800;
}
</style>


