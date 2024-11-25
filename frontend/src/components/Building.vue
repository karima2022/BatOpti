<template>
    <div class="batiments-list">
      <h1>Liste des Bâtiments</h1>
      <div class="cards-container">
        <div v-for="building in buildings" :key="building.id" class="card">
          <h2>{{ building.name }}</h2>
          <p>{{ building.address }}</p>
          <p>{{ building.building_type }}</p>
          <img v-if="building.picture" :src="building.picture" alt="Photo du bâtiment" class="building-photo" />
          
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
      name: 'BuildingsList', 
      data() {
          return {
              buildings: [],
          };
      },
      mounted() {
          fetch("http://127.0.0.1:8000/api/building/building/")
              .then((response) => response.json())
              .then((data) => {
                  this.buildings = data;
              });
      },
  };
  </script>
  
  <style scoped>
  .batiments-list {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  .cards-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  .card {
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 250px;
    text-align: left;
    transition: transform 0.2s;
  }
  
  .card:hover {
    transform: scale(1.05);
  }
  
  .card h2 {
    font-size: 1.5em;
    color: #333;
    margin: 0 0 10px;
  }
  
  .card p {
    color: #555;
    font-size: 1em;
  }
  .building-photo {
  width: 100%; /* Adapte la largeur à celle du conteneur */
  max-width: 200px; /* Largeur maximale */
  height: 200px; /* Maintient le ratio de l'image */
  border-radius: 8px; /* Coins arrondis pour un effet esthétique */
  object-fit: cover; /* Coupe l'image si nécessaire pour la remplir */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Ombre pour un meilleur style */
  margin: 10px auto; /* Centrage et marges */
}

  </style>
  