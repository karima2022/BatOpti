<template>
  <div>
    <h1>Bienvenue sur le tableau de bord</h1>
    <p>Vous êtes connecté en tant que <strong>{{ username }}</strong>.</p>
   
  </div>
</template>

  
<script>
import axios from "axios";

export default {
  name: "DashboardPage",
  components: {
    
  },
  data() {
    return {
      username: "",
   
   
   
    };
    
  },
  async created() {
    const token = localStorage.getItem("access");
    if (!token) {
      this.$router.push("/login"); 
    } else {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/auth/user-info/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        this.username = response.data.username;
      } catch (error) {
        console.error("Erreur lors de la récupération des données utilisateur :", error);
        
      }
    }
  },
 
  
};
</script>

  