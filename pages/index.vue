<template>
  <div class="main-bg min-vh-100">
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
          <p class="loading-text">{{ loadingText }}</p>
        </div>
      </div>
    </transition>

    <div v-if="!loading">
      <div class="d-flex flex-column flex-md-row">
        <nav class="sidebar d-none d-md-flex flex-column align-items-center py-4 px-3">
          <div class="sidebar-header mb-4 w-100 text-center">
            <h5 class="fw-bold text-primary mb-0">Menú</h5>
          </div>
          <div class="sidebar-divider mb-3"></div>
          <a href="http://38.50.50.116:5000/report_lab" class="sidebar-btn mb-2 w-100" data-bs-toggle="tooltip" data-bs-placement="right" title="Accede al laboratorio de movilidad">
            <i class="fa fa-flask me-2 text-primary"></i> Laboratorio
          </a>
          <button class="sidebar-btn mb-2 w-100" data-bs-toggle="tooltip" data-bs-placement="right" title="Consulta planeamiento estratégico">
            <i class="fa fa-map me-2 text-primary"></i> Planeamiento
          </button>
          <a href="http://38.50.50.166/tickets-app/" class="sidebar-btn mb-2 w-100" data-bs-toggle="tooltip" data-bs-placement="right" title="Gestiona tus tickets">
            <i class="fa fa-ticket-alt me-2 text-primary"></i> Tickets
          </a>
          <button class="sidebar-btn mb-2 w-100" data-bs-toggle="tooltip" data-bs-placement="right" title="Accede a interconexión de servicios">
            <i class="fa fa-link me-2 text-primary"></i> Interconexión
          </button>
          <button class="sidebar-btn mb-2 w-100" data-bs-toggle="tooltip" data-bs-placement="right" title="Accede al módulo de señalización">
            <i class="fa fa-road me-2 text-primary"></i> Señalización
          </button>
        </nav>
        <nav class="top-nav d-md-none bg-white shadow-sm py-2 px-3 mb-3 rounded-3 w-100">
          <div class="d-flex justify-content-around flex-wrap">
            <a href="http://38.50.50.116:5000/report_lab" class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede al laboratorio de movilidad">
              <i class="fa fa-flask"></i> <span class="d-none d-sm-inline ms-1">Laboratorio</span>
            </a>
            <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Consulta planeamiento estratégico">
              <i class="fa fa-map"></i> <span class="d-none d-sm-inline ms-1">Planeamiento</span>
            </button>
            <a href="http://38.50.50.166/tickets-app/" class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Gestiona tus tickets">
              <i class="fa fa-ticket-alt"></i> <span class="d-none d-sm-inline ms-1">Tickets</span>
            </a>
            <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede a interconexión de servicios">
              <i class="fa fa-link"></i> <span class="d-none d-sm-inline ms-1">Interconexión</span>
            </button>
            <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede al módulo de señalización">
              <i class="fa fa-road"></i> <span class="d-none d-sm-inline ms-1">Señalización</span>
            </button>
          </div>
        </nav>
        <div class="content-area flex-grow-1 px-4 py-4">
          <div class="row g-4">
            <div class="col-12 col-sm-6 col-lg-4">
              <div class="card h-100 shadow-lg border-0 hover-shadow transition">
                <img src="/imagenes/foto3.jpg" class="card-img-top img-fluid" style="height: 220px; object-fit: cover;" alt="Tickets">
                <div class="card-body"
                     data-bs-toggle="popover"
                     data-bs-trigger="hover"
                     data-bs-placement="bottom"
                     data-bs-title="Tickets Semaforos"
                     data-bs-content="Este módulo permite la gestión y seguimiento de fallas en semáforos, incluyendo reportes, asignación de técnicos y solución de problemas.">
                  <a href="http://38.50.50.166/tickets" class="stretched-link fw-bold text-decoration-none text-primary">Tickets Semaforos</a>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-4">
            <News />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';

const loading = ref(true);
const redActive = ref(true);
const yellowActive = ref(false);
const greenActive = ref(false);
const loadingText = ref('Cargando contenido...');
let cycleInterval: ReturnType<typeof setInterval> | null = null;

const isMobile = () => {
  if (typeof window === 'undefined') {
    return false;
  }
  const userAgent = navigator.userAgent || navigator.vendor || (window as any).opera;
  return /android|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(userAgent);
};

const cycleLights = () => {
  const lightDuration = 200;
  cycleInterval = setInterval(() => {
    redActive.value = false;
    yellowActive.value = true;
    setTimeout(() => {
      yellowActive.value = false;
      greenActive.value = true;
      setTimeout(() => {
        greenActive.value = false;
        redActive.value = true;
      }, lightDuration);
    }, lightDuration);
  }, lightDuration * 3);
};

onMounted(() => {
  const isMobileDevice = isMobile();
  const delay = isMobileDevice ? 2000 : 1000;
  
  if (isMobileDevice) {
    loadingText.value = 'Cargando vista móvil, espere un momento...';
  } else {
    loadingText.value = 'Cargando contenido...';
  }

  cycleLights();

  setTimeout(() => {
    loading.value = false;
    if (cycleInterval) {
      clearInterval(cycleInterval);
    }
  }, delay);
});

onBeforeUnmount(() => {
  if (cycleInterval) {
    clearInterval(cycleInterval);
  }
});
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.main-bg {
  background: linear-gradient(135deg, #f8fafc 0%, #e3e9f7 100%);
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 123, 255, 0.8);
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
  width: 200px;
  margin-bottom: 30px;
}

.traffic-light-container {
  display: flex;
  flex-direction: column;
  background-color: #1a1a1a;
  padding: 12px;
  border-radius: 12px;
  border: 2px solid #333;
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5);
}

.traffic-light-circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin: 6px;
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
  font-size: 1rem;
  font-family: sans-serif;
  font-weight: bold;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.sidebar {
  position: fixed;
  top: 70px;
  left: 0;
  width: 230px;
  height: calc(100vh - 70px);
  background: #fff;
  border-right: 4px solid #2a4fa0;
  box-shadow: 2px 0 16px rgba(44, 62, 80, 0.10);
  z-index: 1030;
  justify-content: flex-start;
  border-top-right-radius: 1.5rem;
  border-bottom-right-radius: 1.5rem;
  padding-top: 2rem;
  transition: box-shadow 0.2s;
}

.sidebar-divider {
  width: 80%;
  height: 3px;
  background: linear-gradient(90deg, #2a4fa0 60%, #e3e9f7 100%);
  border-radius: 2px;
  margin: 0 auto 1rem auto;
}

.sidebar-btn {
  background: #f4f8ff;
  color: #2a4fa0;
  border: none;
  font-size: 1.07rem;
  font-weight: 500;
  border-radius: 0.75rem;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  text-align: left;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s;
  box-shadow: 0 1px 4px rgba(44, 62, 80, 0.04);
  display: flex;
  align-items: center;
}

.sidebar-btn:hover,
.sidebar-btn:focus {
  background: #2a4fa0;
  color: #fff;
  box-shadow: 2px 4px 12px rgba(44, 62, 80, 0.15);
}

.content-area {
  flex-grow: 1;
  padding: 1.5rem 1rem;
}

.top-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
}

.top-nav .btn {
  font-size: 0.8rem;
  padding: 0.5rem 0.75rem;
  flex: 1 1 auto;
  text-align: center;
}

.top-nav .btn i {
  font-size: 1rem;
}

.popover {
  border: none;
  border-radius: 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  font-family: inherit;
  transition: opacity 0.3s ease, transform 0.3s ease;
  transform: translateY(10px);
  opacity: 0;
}

.popover.bs-popover-auto[data-popper-placement^=bottom],
.popover.bs-popover-bottom {
  transform: translateY(0px);
  opacity: 1;
}

.popover-header {
  background-color: #2a4fa0;
  color: #fff;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-bottom: none;
  border-top-left-radius: 1rem;
  border-top-right-radius: 1rem;
}

.popover-body {
  background-color: #f4f8ff;
  color: #333;
  padding: 1rem;
  font-size: 0.95rem;
  border-bottom-left-radius: 1rem;
  border-bottom-right-radius: 1rem;
}

.popover .popover-arrow::before,
.popover .popover-arrow::after {
  display: none;
}

@media (min-width: 768px) {
  .content-area {
    margin-left: 230px;
  }
}

@media (max-width: 767px) {
  .content-area {
    margin-left: 0;
    padding-top: 0;
  }
  .top-nav .btn span {
    display: none !important;
  }
}

@media (min-width: 576px) {
  .top-nav .btn span {
    display: inline !important;
  }
}
</style>