<template>
  <div class="building-detail">
    <div class="building-header">
      <div class="building-info">
        <h1>{{ building.name }}</h1>
        <p class="building-address">{{ building.address }}</p>
        <p class="building-type">Type: {{ building.building_type }}</p>
        <p class="building-type">Description: {{ building.description }}</p>
      </div>
      <div class="building-photo-container">
        <img 
          v-if="building.picture" 
          :src="building.picture" 
          alt="Photo du bâtiment" 
          class="building-photo" 
        />
        <img 
          v-else 
          src="http://127.0.0.1:8000/media/building_photos/default.jpg" 
          alt="Photo par défaut" 
          class="building-photo" 
        />
      </div>
    </div>

    <div class="building-sections">
      <div class="section">
        <h2>Équipements associés</h2>
        <ul>
          <li v-for="equipment in equipments" :key="equipment.id">
            <div class="equipment-item">
              <span class="equipment-name">{{ equipment.name }}</span>
              <span class="equipment-type">({{ equipment.equipment_type }})</span>
            </div>
          </li>
        </ul>
      </div>

      <div class="section">
        <h2>Tickets associés</h2>
        <ul>
          <li v-for="ticket in tickets" :key="ticket.id">
            <div class="ticket-item">
              <span class="ticket-title">{{ ticket.title }}</span>
              <span class="ticket-type">({{ ticket.ticket_type }})</span>
              <p class="ticket-description">{{ ticket.description }}</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      building: {},
      equipments: [],
      tickets: [],
    };
  },
  methods: {
    fetchBuildingDetails() {
      const buildingId = this.$route.params.id;
      axios.get(`http://127.0.0.1:8000/api/building/building/${buildingId}/`)
        .then(response => {
          this.building = response.data;
        });

      axios.get(`http://127.0.0.1:8000/api/building/equipment/?building=${buildingId}`)
        .then(response => {
          this.equipments = response.data;
        });

      axios.get(`http://127.0.0.1:8000/api/ticket/?building=${buildingId}`)
        .then(response => {
          this.tickets = response.data;
        });
    },
  },
  mounted() {
    this.fetchBuildingDetails();
  },
};
</script>

<style scoped>

.building-detail {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}


.building-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 30px;
}


.building-info {
  max-width: 60%;
}

.building-info h1 {
  font-size: 2em;
  color: #333;
  margin: 0 0 10px;
}

.building-address, .building-type {
  font-size: 1.2em;
  color: #555;
  margin: 5px 0;
}


.building-photo-container {
  max-width: 35%;
  text-align: center;
}

.building-photo {
  width: 100%;
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.building-sections {
  margin-top: 30px;
}


.section h2 {
  font-size: 1.8em;
  color: #333;
  border-bottom: 2px solid #007bff;
  padding-bottom: 5px;
  margin-bottom: 15px;
}


.section ul {
  list-style-type: none;
  padding: 0;
}

.section li {
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 10px;
  padding: 15px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.section li:hover {
  transform: scale(1.02);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* Équipements */
.equipment-item {
  display: flex;
  justify-content: space-between;
  font-size: 1.2em;
}

.equipment-name {
  font-weight: bold;
}

.equipment-type {
  font-style: italic;
  color: #777;
}

/* Tickets */
.ticket-item {
  margin-top: 10px;
}

.ticket-title {
  font-weight: bold;
  font-size: 1.2em;
}

.ticket-type {
  font-style: italic;
  color: #777;
}

.ticket-description {
  margin-top: 5px;
  font-size: 1em;
  color: #555;
}
</style>
