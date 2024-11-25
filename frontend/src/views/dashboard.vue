<template>
    <div>
      <h1>Bienvenue sur le tableau de bord</h1>
      <p>Vous êtes connecté en tant que <strong>{{ username }}</strong>.</p>
      <button @click="logout">Se déconnecter</button>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "DashboardPage", 
    data() {
      return {
        username: "",
      };
    },
    async created() {
      // Vérifie le token pour récupérer les infos utilisateur
      const token = localStorage.getItem("access");
      if (!token) {
        this.$router.push("/login"); // Redirige si non connecté
      } else {
        try {
          const response = await axios.get("http://127.0.0.1:8000/api/auth/user-info/", {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          this.username = response.data.username; // Stocke le nom d'utilisateur
        } catch (error) {
          console.error("Erreur lors de la récupération des données utilisateur :", error);
          this.logout(); // Déconnecte si le token est invalide
        }
      }
    },
    methods: {
      logout() {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        this.$router.push("/login"); // Redirige vers la page de connexion
      },
    },
  };
  </script>
  