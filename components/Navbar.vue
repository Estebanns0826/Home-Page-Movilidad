<template>
  <div>
    <div class="navbar-top bg-primary d-flex flex-column flex-md-row justify-content-between align-items-center px-4 py-2 shadow-sm">
      <a href="https://www.gov.co" target="_blank" class="d-flex align-items-center me-3">
        <img src="https://www.cali.gov.co/mod/Bloques/img/logo_gov_co.png" alt="Gobierno de Colombia" style="height: 48px;" />
      </a>

      <div class="text-center flex-grow-1">
        <span class="titulo-principal text-white">
          Subsecretaría de Movilidad Sostenible y Seguridad Vial
        </span>
      </div>

      <div class="d-flex align-items-center gap-3">
        <a
          href="https://www.cali.gov.co/participacion/publicaciones/43/oficina-de-atencin-al-ciudadano/"
          target="_blank"
          class="text-white text-decoration-none d-flex align-items-center"
        >
          <i class="fa-solid fa-envelope me-2" style="font-size: 1.2rem;"></i>
          <span class="fw-semibold">PQRSD</span>
        </a>
        <div class="text-white text-end small">
          <div>{{ fecha }}</div>
          <div>{{ hora }}</div>
        </div>
      </div>
    </div>

    <div class="bandera-cali">
      <div class="franja azul"></div>
      <div class="franja rojo"></div>
      <div class="franja blanco"></div>
      <div class="franja rojo"></div>
      <div class="franja verde"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const hora = ref('');
const fecha = ref('');

const actualizarHora = () => {
  const ahora = new Date();
  hora.value = ahora.toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  fecha.value = ahora.toLocaleDateString('es-CO', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
};

onMounted(() => {
  actualizarHora();
  setInterval(actualizarHora, 1000);
});
</script>

<style scoped>
.bg-primary {
  background-color: #2a4fa0 !important;
}

.titulo-principal {
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.navbar-top {
  border-bottom: 10px solid #1d3c7a;
}

/* Franja tipo bandera de Cali con efecto de onda */
.bandera-cali {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 20px;
  position: relative;
  overflow: hidden;
}

.bandera-cali::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to right,
    transparent,
    rgba(42, 79, 160, 0.5) 20%,
    rgba(42, 79, 160, 0.8) 50%,
    rgba(42, 79, 160, 0.5) 80%,
    transparent
  );
  animation: onda-azul 4s linear infinite;
}

.franja {
  flex-grow: 1;
  width: 100%;
}

.azul {
  background-color: #2a4fa0;
}

.rojo {
  background-color: #c8102e;
}

.blanco {
  background-color: #ffffff;
}

.verde {
  background-color: #007a33;
}

@keyframes onda-azul {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}
</style>