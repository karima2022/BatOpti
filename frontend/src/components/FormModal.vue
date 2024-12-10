<template>
  <div v-if="visible" class="form-modal">
    <div class="form-container">
      <h2>{{ title }}</h2>
      <form @submit.prevent="handleSubmit">
        <div v-for="(field, key) in fields" :key="key" class="form-group">
          <label :for="key">{{ field.label }}</label>
          <template v-if="field.type === 'text' || field.type === 'number' || field.type === 'email'">
            <input :type="field.type" :id="key" v-model="formData[key]" :placeholder="field.placeholder"
                   class="form-control" :required="field.required"/>
          </template>
          <template v-if="field.type === 'textarea'">
            <textarea :id="key" v-model="formData[key]" :placeholder="field.placeholder" class="form-control"
                      :required="field.required"></textarea>
          </template>
          <template v-if="field.type === 'file'">
            <input type="file" :id="key" @change="handleFileChange($event, key)" class="form-control"
                   :placeholder="field.placeholder" :required="field.required"/>
          </template>

          <template v-if="field.type === 'select'">
            <select
                :id="key"
                v-model="formData[key]"
                class="form-control"
                :required="field.required"
                @change="handleSelectChange(key, $event)">
              <option disabled value="">-- {{ field.placeholder }} --</option>
              <option
                  v-for="option in field.options"
                  :key="option.value"
                  :value="option.value">
                {{ option.label }}
              </option>
            </select>
          </template>


        </div>
        <button type="submit" class="form-button">Créer</button>
        <button type="button" class="form-button cancel" @click="handleCancel">Annuler</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    visible: {
      type: Boolean,
      required: true,
    },
    title: {
      type: String,
      default: 'Formulaire',
    },
    fields: {
      type: Object,
      required: true,
    },
    initialData: {
      type: Object,
      default: () => ({}),
    },
  },
  data() {
    return {
      formData: {...this.initialData},
    };
  },
  methods: {
    handleSelectChange(key, event) {
      if (key === 'building') {
        const buildingId = event.target.value;
        this.$emit('building-changed', buildingId); // Émet l'événement vers le composant parent
      }
    },

    handleFileChange(event, key) {
      const file = event.target.files[0];
      if (file) {
        this.formData[key] = file;
      }
    },
    handleSubmit() {

      console.log('Formulaire soumis avec les données :', this.formData);
      this.$emit('submit', this.formData);
    },
    handleCancel() {
      this.$emit('cancel');
    },
  },
};
</script>


<style scoped>
.form-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.form-container {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  width: 400px;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form-button {
  background-color: #ffcc00;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  margin-right: 10px;
}

.form-button:hover {
  background-color: #e6b800;
}

.form-button.cancel {
  background-color: #aaa;
}

.form-button.cancel:hover {
  background-color: #888;
}
</style>
