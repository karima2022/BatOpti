<template>
  <div class="register-page">
    <div class="register-card">
      <div class="register-header">
        <h2>Créer un compte</h2>
        <p>Inscrivez-vous pour commencer à gérer vos bâtiments et projets</p>
      </div>
      <form @submit.prevent="register" class="register-form">
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
        <div class="form-group">
          <select v-model="profession_type" class="form-control">
            <option value="maintenance_manager">Responsable Maintenance</option>
            <option value="technician">Technicien</option>
            <option value="service_provider">Prestataire</option>
            <option value="user">Usager</option>
          </select>
        </div>
        <button type="submit" class="register-button">S'inscrire</button>
        <p v-if="error" class="error-message">{{ error }}</p>
      </form>
      <div class="register-footer">
        <router-link to="/login" class="link">Déjà inscrit ? Connectez-vous</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RegisterPage", 
  data() {
    return {
      username: '',
      password: '',
      profession_type: 'user',
      error: '',
    };
  },
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/api/auth/register/', {
          username: this.username,
          password: this.password,
          profession_type: this.profession_type,
        });
        this.$router.push('/login');
      } catch (err) {
        this.error = "L'inscription a échoué.";
      }
    },
  },
};
</script>

<style scoped lang="scss">
.register-page {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-image: url('@/assets/21560.jpg'); /* Utilise la même image de fond */
  background-size: cover;
  background-repeat: no-repeat;
  font-family: 'Roboto', sans-serif;
}

.register-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 400px;
}

.register-header {
  margin-bottom: 20px;
}

.register-form .form-group {
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

.register-button {
  width: 100%;
  padding: 12px;
  background-color: #ffcc00; /* Jaune vif pour le bouton */
  color: #333;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.register-button:hover {
  background-color: #e6b800; /* Couleur légèrement plus sombre au survol */
}

.error-message {
  color: red;
  margin-top: 10px;
}

.register-footer {
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
