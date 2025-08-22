<template>
  <div>
    <!-- Contenido principal -->
    <div v-if="!loading">
      <Navbar />
      <transition name="fade-scale">
        <NuxtPage class="page-content" />
      </transition>
      <Footer />
    </div>

    <!-- Pantalla de carga con transición -->
    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-container">
          <!-- Logo arriba del semáforo -->
          <img 
            src="/imagenes/logo_gov_co (1).png" 
            alt="Logo Gobierno" 
            class="loading-logo"
          />

          <div class="traffic-light-container">
            <div :class="['traffic-light-circle', 'red', { active: redActive }]"></div>
            <div :class="['traffic-light-circle', 'yellow', { active: yellowActive }]"></div>
            <div :class="['traffic-light-circle', 'green', { active: greenActive }]"></div>
          </div>
          <p class="loading-text">Cargando contenido...</p>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const loading = ref(true);
const redActive = ref(true);
const yellowActive = ref(false);
const greenActive = ref(false);

const cycleLights = () => {
  setTimeout(() => {
    redActive.value = false;
    yellowActive.value = true;
    setTimeout(() => {
      yellowActive.value = false;
      greenActive.value = true;
    }, 100);
  }, 100);
};

onMounted(() => {
  cycleLights();
  setTimeout(() => {
    loading.value = false;
  }, 400);
});
</script>

<style scoped>
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 123, 255, 0.8); /* Azul transparente */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Logo más grande */
.loading-logo {
  width: 300px; /* tamaño aumentado */
  margin-bottom: 20px;
}

.traffic-light-container {
  display: flex;
  flex-direction: column;
  background-color: #000;
  padding: 12px;
  border-radius: 12px;
  border: 2px solid #000;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.2);
}

.traffic-light-circle {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  margin: 8px;
  opacity: 0.2;
  transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out;
}

.traffic-light-circle.active {
  opacity: 1;
  animation: pulse 0.4s ease-in-out;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.red { background-color: red; }
.yellow { background-color: yellow; }
.green { background-color: limegreen; }

.loading-text {
  color: white;
  margin-top: 20px;
  font-size: 1.5rem;
  font-family: sans-serif;
  font-weight: bold;
}

.fade-scale-enter-active {
  transition: all 0.5s ease;
}
.fade-scale-leave-active {
  transition: all 0.5s ease;
}
.fade-scale-enter-from {
  opacity: 0;
  transform: scale(0.95);
}
.fade-scale-enter-to {
  opacity: 1;
  transform: scale(1);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
