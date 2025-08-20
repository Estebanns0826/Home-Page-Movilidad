<template>
  <div>
    <!-- 🔷 Franja azul superior con logos -->
    <div class="bg-primary d-flex justify-content-between align-items-center px-3 py-2">
      <a href="https://www.gov.co" title="Gobierno de Colombia" target="_blank">
        <img class="img-responsive" src="https://www.cali.gov.co/mod/Bloques/img/logo_gov_co.png" id="bloqueImg"
             alt="Gobierno de Colombia"
             title="Gobierno de Colombia">
      </a>
      <div class="d-flex justify-content-center align-items-center vh-10">
        <img
            src="/imagenes/LogoSecretariaMovilidad.jpeg"
            alt="GOV.CO"
            class="img-fluid me-5"
            style="height: 40px;"
        />
        <p class="text-white" style="font-size: 24px;">
          Subsecretaría de Movilidad Sostenible y Seguridad Vial
        </p>
      </div>
      <a
          href="https://www.cali.gov.co/participacion/publicaciones/43/oficina-de-atencin-al-ciudadano/"
          target="_blank"
          rel="noopener"
          class="text-white d-flex align-items-center text-decoration-none"
      >
        <fa-icon icon="fa-solid fa-envelope" class="me-2" style="font-size: 1.2rem;" />
        <span class="fw-semibold">PQRSD</span>
      </a>
    </div>

    <!-- ⚪ Franja blanca con enlaces desplegables -->
    <nav class="bg-white shadow-sm border-bottom">
      <ul class="nav justify-content-center py-2 fw-medium text-black small">
        <!-- Tickets -->
        <li class="nav-item dropdown px-2">
          <a href="http://38.50.50.166/tickets" class="d-block mt-2 text-primary fw-bold text-decoration-underline">Tickets</a>


          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Planeación institucional</a></li>
            <li><a class="dropdown-item" href="#">Control interno</a></li>
            <li><a class="dropdown-item" href="#">Rendición de cuentas</a></li>
            <li><a class="dropdown-item" href="#">Normatividad</a></li>
          </ul>
        </li>

        <!-- Servicios -->
        
        <li class="nav-item dropdown">

          <a href="http://38.50.50.166:9090/geoserver"
             class="d-block mt-2 text-primary fw-bold text-decoration-underline">Geoserver</a>

          <ul class="dropdown-menu" aria-labelledby="serviciosDropdown">
            <li>
              <a class="dropdown-item" href="https://www.cali.gov.co/tramites_servicios/" target="_blank"
                 rel="noopener">
                Trámites y servicios
              </a>
            </li>
            <li>
              <a class="dropdown-item"
                 href="https://www.cali.gov.co/participacion/publicaciones/136949/canales-de-atencion-al-ciudadano/"
                 target="_blank" rel="noopener">
                Canales de atención
              </a>
            </li>
            <li>
              <a class="dropdown-item"
                 href="https://www.cali.gov.co/participacion/publicaciones/183914/menu-atencion-y-servicios-a-la-ciudadania/"
                 target="_blank" rel="noopener">
                Información de interés
              </a>
            </li>
          </ul>
        </li>
        <!-- Participa -->
        
      </ul>
    </nav>
  </div>
</template>

<script setup>
// No hay lógica específica para este navbar
</script>

<style scoped>
.bg-primary {
  background-color: #36c !important;
}
</style>
