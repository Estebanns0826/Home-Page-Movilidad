<template>
  <div>
    <div v-if="!loading">
      <Navbar />
      <transition name="fade-scale">
        <NuxtPage class="page-content" />
      </transition>
      <Footer />
    </div>

    <transition name="fade">
      <div v-if="loading" class="loading-overlay">
        <div class="loading-container">
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
  const lightDuration = 200; // Duración en milisegundos para cada luz

  setTimeout(() => {
    redActive.value = false;
    yellowActive.value = true;
    setTimeout(() => {
      yellowActive.value = false;
      greenActive.value = true;
      setTimeout(() => {
        // Al final del ciclo, si loading sigue activo, reiniciar
        if (loading.value) {
          greenActive.value = false;
          redActive.value = true;
          cycleLights();
        }
      }, lightDuration);
    }, lightDuration);
  }, lightDuration);
};

onMounted(() => {
  cycleLights();
  setTimeout(() => {
    loading.value = false;
  }, 1000); // Duración total de la pantalla de carga
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

.loading-logo {
  width: 200px; /* Tamaño más grande */
  margin-bottom: 30px; /* Mayor espacio inferior */
}

.traffic-light-container {
  display: flex;
  flex-direction: column;
  background-color: #1a1a1a; /* Color más oscuro */
  padding: 12px; /* Relleno más grande */
  border-radius: 12px; /* Bordes más redondeados */
  border: 2px solid #333; /* Borde sutil */
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
}

.traffic-light-circle {
  width: 30px; /* Tamaño del círculo más grande */
  height: 30px; /* Tamaño del círculo más grande */
  border-radius: 50%;
  margin: 6px; /* Margen más grande */
  opacity: 0.2;
  transition: opacity 0.2s ease-in-out;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.traffic-light-circle.active {
  opacity: 1;
  box-shadow: 0 0 10px var(--light-color), inset 0 0 5px var(--light-color);
  animation: pulse 0.6s infinite alternate;
}

.red {
  background-color: #ff0000;
  --light-color: #ff0000;
}
.yellow {
  background-color: #ffc107;
  --light-color: #ffc107;
}
.green {
  background-color: #28a745;
  --light-color: #28a745;
}

@keyframes pulse {
  0% { transform: scale(1); }
  100% { transform: scale(1.1); }
}

.loading-text {
  color: white;
  margin-top: 15px;
  font-size: 1rem; /* Tamaño de fuente más pequeño */
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