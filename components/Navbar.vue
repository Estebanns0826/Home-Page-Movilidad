<template>
  <div>
    <div class="navbar-top bg-primary d-flex flex-column flex-md-row justify-content-between align-items-center px-3 py-1 shadow-sm">
      <div class="d-flex align-items-center flex-shrink-0">
        <a href="https://www.gov.co" target="_blank" class="d-flex align-items-center me-md-2">
          <img src="https://www.cali.gov.co/mod/Bloques/img/logo_gov_co.png" alt="Gobierno de Colombia" class="logo-gov" />
        </a>
      </div>

      <div class="d-flex justify-content-center align-items-center flex-grow-1">
        <span class="titulo-principal text-white text-center">
          Secretaría de Movilidad Sostenible y Seguridad Vial
        </span>
      </div>

      <div class="d-flex align-items-center gap-3 flex-shrink-0">
        <a href="https://www.cali.gov.co/participacion/publicaciones/43/oficina-de-atencin-al-ciudadano/" target="_blank" class="text-white text-decoration-none d-flex align-items-center">
          <i class="fa-solid fa-envelope me-2" style="font-size: 1rem;"></i>
          <span class="fw-semibold">PQRSD</span>
        </a>
        <div class="text-white text-end small d-none d-md-block">
          <div>{{ fecha }}</div>
          <div>{{ hora }}</div>
        </div>
      </div>
    </div>

    <div class="franja-blanca d-flex flex-column flex-md-row align-items-center justify-content-md-between px-3 py-2">
      <img src="public/imagenes/secretaria_movilidad.svg" alt="Alcaldía de Santiago de Cali" class="logo-alcaldia d-none d-md-block" />

      <div class="d-flex d-md-none flex-column align-items-center justify-content-center gap-3">
        <img src="public/imagenes/secretaria_movilidad.svg" alt="Alcaldía de Santiago de Cali" class="logo-alcaldia-movil" />
        <div class="search-box d-flex align-items-center">
          <input type="text" placeholder="Buscar..." class="search-input" />
          <i class="fa-solid fa-magnifying-glass search-icon"></i>
        </div>
        <span class="version-movil text-center">Versión Móvil</span>
      </div>

      <nav class="nav-links d-none d-md-flex align-items-center gap-4">
        <a href="/laboratorio" class="nav-link">Laboratorio</a>
        <a href="/planeamiento" class="nav-link">Planeamiento</a>
        <a href="/interconexion" class="nav-link">Interconexión</a>
        <a href="/semaforos" class="nav-link">Semáforos</a>
        <div class="search-box d-none d-lg-flex align-items-center">
          <input type="text" placeholder="Buscar..." class="search-input" />
          <i class="fa-solid fa-magnifying-glass search-icon"></i>
        </div>
      </nav>
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
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* Azul institucional */
.bg-primary {
  background-color: #3f6edc !important;
}

.navbar-top {
  border-bottom: 6px solid #2c57a0;
  min-height: 42px;
}

.logo-gov {
  height: 36px;
}

.titulo-principal {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.3px;
  line-height: 1.2;
}

/* Franja blanca con logo y navegación */
.franja-blanca {
  background-color: #ffffff;
  height: auto;
  min-height: 70px;
  border-bottom: 1px solid #ddd;
}

.logo-alcaldia {
  height: 56px;
  padding-left: 0;
}

.logo-alcaldia-movil {
  height: 48px;
  margin-bottom: 1rem;
}

/* Links institucionales */
.nav-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.9rem;
}

.nav-link:hover {
  text-decoration: underline;
}

/* Caja de búsqueda */
.search-box {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 2px 6px;
  background-color: #f9f9f9;
}

.search-input {
  border: none;
  outline: none;
  font-size: 0.85rem;
  background: transparent;
}

.search-icon {
  color: #666;
  margin-left: 4px;
}

/* Bandera de Cali */
.bandera-cali {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 16px;
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
  background-color: #3f6edc;
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

/* Media Queries para responsividad */
@media (max-width: 767px) {
  .navbar-top {
    flex-direction: column;
    text-align: center;
    padding: 1rem;
  }
  .logo-gov {
    height: 32px;
  }
  .titulo-principal {
    font-size: 0.8rem;
    line-height: 1.2;
  }
  .franja-blanca {
    flex-direction: column;
    padding: 1rem;
    height: auto;
    justify-content: center;
  }
  .logo-alcaldia-movil {
    height: 48px;
    margin-bottom: 1rem;
    padding-left: 0;
  }
  .nav-links {
    display: none !important;
  }
  .search-box {
    width: 80%;
    margin-top: 1rem;
  }
  .version-movil {
    font-size: 0.9rem;
    font-weight: 600;
    color: #333;
    margin-top: 1rem;
  }
}

@media (min-width: 768px) {
  .logo-alcaldia {
    padding-left: 250px;
  }
}
</style>