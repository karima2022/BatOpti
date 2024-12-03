<template>
    <div>
     
     
  
      <div class="kanban-board">
      <div
        v-for="column in columns"
        :key="column.status"
        class="kanban-column"
        @dragover.prevent
        @drop="handleDrop($event, column.status)"
      >
        <h2 class="column-title">{{ column.title }}</h2>
        <div
    v-for="ticket in tickets.filter(ticket => ticket.status === column.status)"
    :key="ticket.id"
    class="kanban-card"
    draggable="true"
    @dragstart="handleDragStart(ticket.id)"
  >
    <h3 class="card-title">{{ ticket.title }}</h3>
    <p class="card-description">{{ ticket.description }}</p>
  </div>
  
      </div>
    </div>
    </div>
  </template>
  
    
  <script>
  import axios from "axios";
  
  export default {
    name: "TicketsList",
    components: {
      
    },
    data() {
      return {
        username: "",
     
     
      columns: [
        { status: "created", title: "Créé" },
        { status: "open", title: "Ouvert" },
        { status: "in_progress", title: "En cours" },
        { status: "resolved", title: "Résolu" },
      ],
        tickets: [],
        draggedTicketId: null, 
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
    methods: {
      async fetchTickets() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/ticket/ticket/");
      this.tickets = response.data;
      console.log("Tickets chargés :", this.tickets);
    } catch (error) {
      console.error("Erreur lors de la récupération des tickets :", error);
    }
  },
  
  
  handleDragStart(ticketId) {
    this.draggedTicketId = ticketId;
  },
  
  
      async handleDrop(event, newStatus) {
    if (!this.draggedTicketId) {
      console.error("Aucun ticket en cours de glisser-déposer !");
      return;
    }
  
    const ticket = this.tickets.find(ticket => ticket.id === this.draggedTicketId);
  
    if (!ticket) {
      console.error("Ticket introuvable !");
      return;
    }
  
    const updatedData = {
      title: ticket.title,
      description: ticket.description,
      priority: ticket.priority || "medium", 
      ticket_type: ticket.ticket_type || "maintenance", 
      building: ticket.building || 1, 
      status: newStatus, 
    };
  
    try {
      await axios.put(`http://127.0.0.1:8000/api/ticket/ticket/${ticket.id}/`, updatedData);
  
      ticket.status = newStatus;
    } catch (error) {
      console.error("Erreur lors de la mise à jour du ticket :", error);
    }
  
    this.draggedTicketId = null;
  }
  
    },
    async mounted() {
      await this.fetchTickets();
    },
     
    
  };
  </script>
  