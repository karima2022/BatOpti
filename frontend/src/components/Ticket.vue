<template>
  <div>
    <!-- Bouton pour ajouter un ticket -->
    <button class="action-button" @click="addTicket">+</button>

    <!-- Kanban Board -->
    <div class="kanban-board">
      <div
        v-for="column in columns"
        :key="column.status"
        class="kanban-column"
        @dragover.prevent
        @drop="handleDrop($event, column.status)"
      >
        <h2 class="column-title">{{ column.title }}</h2>

        <!-- Tickets dans la colonne -->
        <div
          v-for="ticket in filteredTickets(column.status)"
          :key="ticket.id"
          class="kanban-card"
          draggable="true"
          @dragstart="handleDragStart(ticket.id)"
        >
          <div class="card-header">
            <div class="building-bubble">
                  <div class="image-container">
          <img
  :src="getBuildingById(ticket.building)?.picture || 'http://127.0.0.1:8000/media/default.jpg'"
  alt="Photo du bâtiment"
  class="building-photo"
/>

        </div>
            </div>
            <h3 class="card-title">{{ ticket.title }}</h3>
          </div>
          <p class="card-description">{{ ticket.description }}</p>
          <div class="card-footer">
            <span class="assigned-to" v-if="ticket.assigned_to">
              Assigné à: {{ ticket.assigned_to.username }}
              ({{ ticket.assigned_to.profession_type }})
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Formulaire modal pour créer un ticket -->
    <FormModal
      :visible="formVisible"
      :title="formTitle"
      :fields="formFields"
      :initialData="formInitialData"
      @submit="handleFormSubmit"
      @cancel="closeForm"
    />

    <!-- Formulaire modal pour l'attribution -->
    <FormModal
      :visible="showAssignModal"
      title="Attribuer le ticket"
      :fields="assignmentFields"
      :initialData="assignmentInitialData"
      @submit="handleAssignmentSubmit"
      @cancel="closeAssignModal"
    />
  </div>
</template>

<script>
import axios from "axios";
import FormModal from "./FormModal.vue";

export default {
  name: "TicketsList",
  components: {
    FormModal,
  },
  data() {
    return {
      columns: [
        { status: "created", title: "Créé" },
        { status: "open", title: "Ouvert" },
        { status: "in_progress", title: "En cours" },
        { status: "resolved", title: "Résolu" },
      ],
      tickets: [],
      buildings: [],
      equipments: [],
      formTitle: "",
      formFields: {},
      formInitialData: {},
      formType: "",
      formVisible: false,
      draggedTicketId: null,
      showAssignModal: false,
      ticketToAssign: null,
      users: [],
      assignmentFields: {
        assigned_to: {
          label: "Assigner à",
          type: "select",
          placeholder: "Sélectionner un utilisateur",
          options: [],
          required: true,
        },
      },
      assignmentInitialData: {
        assigned_to: "",
      },
    };
  },
  methods: {
    async fetchTickets() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/ticket/ticket/");
        this.tickets = response.data;

      } catch (error) {
        console.error("Erreur lors de la récupération des tickets :", error);
      }
    },
   async fetchBuildings() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/building/building/");
    console.log("Bâtiments reçus :", response.data);
    this.buildings = response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération des bâtiments :", error);
  }
},
    getBuildingById(buildingId) {
  return this.buildings.find(building => building.id === buildingId) || null;
},

    async fetchEquipments() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/building/equipment/");
        this.equipments = response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des équipements :", error);
      }
    },
    async fetchUsers() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/user/users/");
        this.users = response.data;

        this.assignmentFields.assigned_to.options = this.users.map(user => ({
          value: user.id,
          label: `${user.username} (${user.profession_type})`,

        }));
      } catch (error) {
        console.error("Erreur lors de la récupération des utilisateurs:", error);
      }
    },
    addTicket() {
      this.formTitle = "Créer un ticket";
      this.formFields = {
        title: { label: "Titre", type: "text", placeholder: "Titre du ticket", required: true },
        description: { label: "Description", type: "textarea", placeholder: "Description", required: true },
        priority: {
          label: "Priorité",
          type: "select",
          placeholder: "Priorité",
          options: [
            { value: "low", label: "Faible" },
            { value: "medium", label: "Moyenne" },
            { value: "high", label: "Élevée" },
          ],
          required: true,
        },
        ticket_type: {
          label: "Type",
          type: "select",
          placeholder: "Type de ticket",
          options: [
            { value: "intervention", label: "Intervention" },
            { value: "maintenance", label: "Maintenance" },
          ],
          required: true,
        },
        building: {
          label: "Bâtiment",
          type: "select",
          placeholder: "Sélectionner un bâtiment",
          options: this.buildings.map(b => ({ value: b.id, label: b.name })),
          required: true,
        },
        equipment: {
          label: "Équipement",
          type: "select",
          placeholder: "Sélectionner un équipement",
          options: this.equipments.map(e => ({ value: e.id, label: e.name })),
          required: false,
        },
      };
      this.formInitialData = {
        title: "",
        description: "",
        priority: "medium",
        ticket_type: "maintenance",
        building: "",
        equipment: "",
      };
      this.formType = "ticket";
      this.formVisible = true;
    },
    handleFormSubmit(formData) {
      axios
        .post("http://127.0.0.1:8000/api/ticket/ticket/", formData)
        .then(() => {
          this.fetchTickets(); // Recharge les tickets après l'ajout
          this.formVisible = false;
        })
        .catch((error) => {
          console.error("Erreur lors de la création du ticket :", error);
        });
    },
    handleDragStart(ticketId) {
      this.draggedTicketId = ticketId; // Enregistre l'ID du ticket à déplacer
    },
    async handleDrop(event, newStatus) {
      if (!this.draggedTicketId) return;

      const ticket = this.tickets.find((t) => t.id === this.draggedTicketId);
      if (!ticket) return;

      if (ticket.status === 'created' && newStatus === 'open') {
        this.ticketToAssign = ticket;
        this.showAssignModal = true;
        return;
      }

      await this.updateTicketStatus(ticket, newStatus);
    },
    async handleAssignmentSubmit(formData) {
      if (this.ticketToAssign && formData.assigned_to) {
        await this.updateTicketStatus(this.ticketToAssign, 'open', formData.assigned_to);
        this.closeAssignModal();
      }
    },
    async updateTicketStatus(ticket, newStatus, assignedUserId = null) {
      const updatedData = {
        ...ticket,
        status: newStatus,
        assigned_to: assignedUserId,
      };

      try {
        await axios.put(
          `http://127.0.0.1:8000/api/ticket/ticket/${ticket.id}/`,
          updatedData
        );
        await this.fetchTickets();
      } catch (error) {
        console.error("Erreur lors de la mise à jour du ticket:", error);
      }
    },
    closeForm() {
      this.formVisible = false; // Ferme le formulaire
    },
    closeAssignModal() {
      this.showAssignModal = false;
      this.ticketToAssign = null;
      this.draggedTicketId = null;
      this.assignmentInitialData.assigned_to = "";
    },
    filteredTickets(status) {

      return this.tickets.filter((ticket) => ticket.status === status);
    },
  getBuildingImage(building) {
  if (building && building.picture && !building.picture.includes('default.jpg')) {
    return 'http://127.0.0.1:8000${building.picture}';
  }
  return 'http://127.0.0.1:8000/media/default.jpg';
}


  },
  async mounted() {
    await Promise.all([
      this.fetchTickets(),
      this.fetchBuildings(),
      this.fetchEquipments(),
      this.fetchUsers(),
    ]);
  },
};
</script>

<style scoped>
img{
  width: 30%;
  height: 30%;
  object-fit: cover;
}
.kanban-board {
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
  padding: 20px;
  gap: 20px;
}

.kanban-column {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  flex: 1;
}

.column-title {
  font-size: 1.5em;
  font-weight: bold;
  text-align: center;
  margin-bottom: 10px;
}

.kanban-card {
  background: #fff;
  padding: 15px;
  border-radius: 5px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: grab;
}

.card-title {
  font-size: 1.2em;
  font-weight: bold;
}

.card-description {
  font-size: 0.9em;
  color: #555;
}

.action-button {
  background-color: #ffcc00;
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 1.5em;
  width: 50px;
  height: 50px;
  cursor: pointer;
  position: fixed;
  margin-top:5px;
  right: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease;
}

.action-button:hover {
  background-color: #e6b800;
}
</style>
