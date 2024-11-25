<template>
    <div>
      <h2>Connexion</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Nom d'utilisateur" required />
        <input type="password" v-model="password" placeholder="Mot de passe" required />
        <button type="submit">Se connecter</button>
      </form>
      <p v-if="error">{{ error }}</p>
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
  