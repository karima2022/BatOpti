<template>
    <div>
      <h2>Inscription</h2>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Nom d'utilisateur" required />
        <input type="password" v-model="password" placeholder="Mot de passe" required />
        <select v-model="profession_type">
          <option value="maintenance_manager">Responsable Maintenance</option>
          <option value="technician">Technicien</option>
          <option value="service_provider">Prestataire</option>
          <option value="user">Usager</option>
        </select>
        <button type="submit">S'inscrire</button>
      </form>
      <p v-if="error">{{ error }}</p>
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
  