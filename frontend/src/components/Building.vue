<template>
  <div class="batiments-list">

    <button class="action-button" @click="addBuilding">+</button>

    <div class="cards-container">
      <div
        v-for="building in buildings"
        :key="building.id"
        class="card"
        @click="goToDetails(building.id)"
      >
        <h2 class="building-name">{{ building.name }}</h2>
        <p class="building-address">{{ building.address }}</p>
        <p class="building-type">{{ formatBuildingType(building.building_type) }}</p>

        <div class="image-container">
          <img
            :src="building.picture"
            alt="Photo du bâtiment"
            class="building-photo"
          />
        </div>
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
import axios from "axios";
import FormModal from "./FormModal.vue";


export default {
  name: "BuildingsList",
  components: {
    FormModal,
  },
  data() {
    return {
      buildings: [],
      formTitle: "",
      formFields: {},
      formInitialData: {},
      formType: "",
      formVisible: false,
      
    };
  },
  methods: {
  


    formatBuildingType(type) {
      const types = {
        school: "École",
        admin: "Administration",
        bank: "Banque",
        theater: "Théâtre",
      };
      return types[type] || "Inconnu";
    },

    goToDetails(buildingId) {
      this.$router.push(`/batiments/${buildingId}`);
    },

    addBuilding() {
      this.formTitle = "Ajouter un bâtiment";
      this.formFields = {
        name: {
          label: "Nom",
          type: "text",
          placeholder: "Nom du bâtiment",
          required: true,
        },
        building_type: {
          label: "Type",
          type: "select",
          placeholder: "Type de bâtiment",
          options: [
            { value: "school", label: "École" },
            { value: "admin", label: "Administration" },
            { value: "bank", label: "Banque" },
            { value: "theater", label: "Théâtre" },
          ],
          required: true,
        },
        address: {
          label: "Adresse",
          type: "text",
          placeholder: "Adresse du bâtiment",
          required: true,
        },
        description: {
          label: "Description",
          type: "textarea",
          placeholder: "Description du bâtiment",
          required: true,
        },
        picture: {
          label: "Photo",
          type: "file",
          placeholder: "Photo du bâtiment",
        },
      };

      this.formInitialData = {
        name: "",
        building_type: "",
        address: "",
        description: "",
        picture: null,
      };

      this.formType = "building";
      this.formVisible = true;
    },

    handleFormSubmit(formData) {
  const data = new FormData();
  

  for (const key in formData) {
    data.append(key, formData[key]);
  }


  axios
    .post("http://127.0.0.1:8000/api/building/building/", data, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then(() => {
      this.fetchBuildings();
      this.formVisible = false;
    })
    .catch((error) => {
      console.error(
        "Erreur lors de la création du bâtiment :",
        error.response?.data || error.message
      );
    });
}
,

    fetchBuildings() {
      axios
        .get("http://127.0.0.1:8000/api/building/building/")
        .then((response) => {
          this.buildings = response.data;
        })
        .catch((error) => {
          console.error(
            "Erreur lors de la récupération des bâtiments :",
            error.response?.data || error.message
          );
        });
    },
  },

  mounted() {
    this.fetchBuildings();
  },
};
</script>

<style scoped>
.batiments-list {
  max-width: 1200px;
  margin: 0 auto;
  text-align: right;
  padding: 20px;
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
  margin-bottom: 20px;
justify-content: right;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.action-button:hover {
  background-color: #e6b800;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.card {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  text-align: left;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.building-name {
  font-size: 1.5rem;
  color: #333;
  margin: 0 0 10px;
}

.building-address,
.building-type {
  color: #555;
  font-size: 1rem;
  margin: 5px 0;
}

.image-container {
  margin: 10px 0;
  text-align: center;
}

.building-photo {
  width: 100%;
  max-width: 200px;
  height: auto;
  border-radius: 8px;
  object-fit: cover;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
