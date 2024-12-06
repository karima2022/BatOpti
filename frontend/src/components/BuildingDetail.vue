<template>
  <div class="building-detail">
    <div class="building-header">
      <div class="building-info">
        <h1>{{ building.name }}</h1>
        <p class="building-address">{{ building.address }}</p>
        <p class="building-type">Type : {{ building.building_type }}</p>
        <p class="building-description">Description : {{ building.description }}</p>
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

    <div class="action-buttons">
    </div>

    <div class="building-sections">
      <div class="section">
        
        <h2>Équipements associés</h2>       
        <button class="action-button" @click="addEquipment">+</button>
        
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
        <button class="action-button" @click="createTicket">+</button>

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


    <FormModal
      :visible="formVisible"
      :title="formTitle"
      :fields="formFields"
      :initialData="formInitialData"
      @submit="handleFormSubmit"
      @cancel="closeForm"
    />
  </div>
</template>



<script>
import axios from 'axios';
import FormModal from './FormModal.vue';

export default {
  components: {
    FormModal,
  },
  data() {
    return {
      building: {},
      equipments: [],
      tickets: [],
      formVisible: false, 
      formTitle: '',
      formFields: {},
      formInitialData: {},
      formType: '', 
    };
  },
  methods: {
    fetchBuildingDetails() {
  const buildingId = this.$route.params.id;


  axios.get(`http://127.0.0.1:8000/api/building/building/${buildingId}/`)
    .then(response => {
      this.building = response.data;
    });


  axios.get(`http://127.0.0.1:8000/api/building/equipment/?building_id=${buildingId}`)
    .then(response => {
      this.equipments = response.data;
    });

  axios.get(`http://127.0.0.1:8000/api/ticket/ticket/?building=${buildingId}`)
    .then(response => {
      this.tickets = response.data;
    });
},

    addEquipment() {
      this.formTitle = 'Ajouter un équipement';
      this.formFields = { 
        name: { label: 'Nom', type: 'text', placeholder: 'Nom de l\'équipement', required: true },
        equipment_type: {
          label: 'Type',
          type: 'select',
          placeholder: 'Type d\'équipement',
          options: [
            { value: 'elevator', label: 'Ascenseur' },
            { value: 'hvac', label: 'Climatisation' },
            { value: 'fire_alarm', label: 'Alarme incendie' },
          ],
          required: true,
        },
      };
      this.formInitialData = {};
      this.formType = 'equipment';
      this.formVisible = true;
    },
    createTicket() {
      this.formTitle = 'Créer un ticket';
      this.formFields = {
        title: { label: 'Titre', type: 'text', placeholder: 'Titre du ticket', required: true },
        description: { label: 'Description', type: 'textarea', placeholder: 'Description', required: true },
        priority: {
          label: 'Priorité',
          type: 'select',
          placeholder: 'Priorité',
          options: [
            { value: 'low', label: 'Faible' },
            { value: 'medium', label: 'Moyenne' },
            { value: 'high', label: 'Élevée' },
          ],
          required: true,
        },
        ticket_type: {
          label: 'Type',
          type: 'select',
          placeholder: 'Type de ticket',
          options: [
            { value: 'intervention', label: 'Intervention' },
            { value: 'maintenance', label: 'Maintenance' },
          ],
          required: true,
        },
      };
      this.formInitialData = {};
      this.formType = 'ticket';
      this.formVisible = true;
    },
    handleFormSubmit(formData) {
  const buildingId = this.building.id;
  if (this.formType === 'equipment') {
    axios.post('http://127.0.0.1:8000/api/building/equipment/', {
      ...formData,
      building: buildingId,
    })
    .then(() => {
      this.fetchBuildingDetails();
      this.formVisible = false;
    })
    .catch(error => {
      console.error('Erreur lors de la création de l\'équipement :', error.response?.data || error.message);
    });
  } else if (this.formType === 'ticket') {
    axios.post('http://127.0.0.1:8000/api/ticket/ticket/', {
      ...formData,
      building: buildingId,
    })
    .then(() => {
      this.fetchBuildingDetails();
      this.formVisible = false;
    })
    .catch(error => {
      console.error('Erreur lors de la création du ticket :', error.response?.data || error.message);
    });
  }
}
,
    closeForm() {
      this.formVisible = false;
    },
  },
  mounted() {
    this.fetchBuildingDetails();
  },
};

</script>

<style scoped lang="scss">
.building-detail {
  margin: 20px auto;
  padding: 20px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.building-header {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.building-photo {
  max-width: 300px;
  border-radius: 8px;
  object-fit: cover;
  margin: 0 auto;
}

.building-sections .section {
  margin-bottom: 20px;
}

.section ul {
  padding: 0;
  list-style: none;
}

.section li {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
  transition: box-shadow 0.3s;
}

.section li:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.building-detail {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  background: linear-gradient(135deg, #f8f8f8, #e8e8e8); /* Gradient clair et moderne */
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}


.building-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 20px;
  margin-bottom: 30px;
}

.building-info {
  flex: 1; 
  text-align: left; 
  padding-right: 20px; 
}

.building-info h1 {
  font-size: 2.5em;
  color: #333;
  margin-bottom: 15px;
  text-transform: capitalize;
}

.building-info p {
  font-size: 1.2em;
  color: #555;
  margin-bottom: 10px;
}

.building-photo-container {
  flex-shrink: 0; 
  max-width: 40%;
  text-align: center;
}

.building-photo {
  width: 100%;
  max-width: 300px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}


.action-buttons {
  display: flex;
  gap: 20px;
  justify-content: flex-start; 
  margin-bottom: 30px;
}

.action-button {
  background-color: #ffcc00;
  color: #333;
  border: none;
  border-radius: 8px;
  font-size: 1.2em;
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


.building-sections {
  margin-top: 30px;
}

.section h2 {
  font-size: 2em;
  color: #333;
  margin-bottom: 20px;
  border-bottom: 2px solid #ffcc00;
  padding-bottom: 5px;
}

.section ul {
  list-style-type: none;
  padding: 0;
}

.section li {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 10px;
  margin-bottom: 10px;
  padding: 15px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.section li:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.equipment-item, .ticket-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2em;
}

.equipment-name, .ticket-title {
  font-weight: bold;
}

.equipment-type, .ticket-type {
  font-style: italic;
  color: #777;
}
</style>


