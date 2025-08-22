<template>
  <div class="main-bg min-vh-100">
    <div class="d-flex">
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

      <nav class="d-md-none bg-white shadow-sm py-2 px-3 mb-3 rounded-3 w-100">
        <div class="d-flex justify-content-around flex-wrap">
          <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede a bodega de semaforización">Bodega de Semaforización</button>
          <a href="http://38.50.50.116:5000/login" class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede al laboratorio de movilidad">Laboratorio</a>
          <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Consulta planeamiento estratégico">Planeamiento</button>
          <a href="http://38.50.50.166/tickets-app/" class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Gestiona tus tickets">Tickets</a>
          <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede a interconexión de servicios">Interconexión</button>
          <button class="btn btn-outline-primary sidebar-btn" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Accede al módulo de señalización">Señalización</button>
        </div>
      </nav>

      <div class="content-area flex-grow-1 px-4 py-4">
        <div class="row g-4">
          <div class="col-md-6 col-lg-4">
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
</template>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  if (typeof window !== 'undefined' && window.bootstrap) {
    // Inicializar Tooltips
    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
      new window.bootstrap.Tooltip(el, {
        placement: el.dataset.bsPlacement || 'right',
        trigger: 'hover',
        animation: true,
        delay: { show: 150, hide: 100 }
      });
    });

    // Inicializar Popovers
    document.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => {
      new window.bootstrap.Popover(el, {
        placement: el.dataset.bsPlacement || 'bottom',
        trigger: el.dataset.bsTrigger || 'hover',
        animation: true,
        html: true,
      });
    });
  }
})
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

.main-bg {
  background: linear-gradient(135deg, #f8fafc 0%, #e3e9f7 100%);
}

/* Sidebar */
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
  box-shadow: 0 2px 8px rgba(44, 62, 80, 0.10);
}

.content-area {
  margin-left: 230px;
  width: 100%;
  min-height: calc(100vh - 70px);
  transition: margin-left 0.2s;
}

/* Estilo para el Popover tipo diálogo */
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

@media (max-width: 991px) {
  .sidebar {
    width: 160px;
  }
  .content-area {
    margin-left: 0;
  }
}

@media (max-width: 767px) {
  .sidebar {
    display: none !important;
  }
  .content-area {
    margin-left: 0;
    padding: 1rem 0.5rem;
  }
}
</style>