<template>
  <footer>
    <div class="container inner-container">
      <div class="row">
        <div class="col-lg-2 col-md-3 mb-4 mb-md-0 d-flex align-items-center justify-content-center justify-content-md-start">
          <img src="https://www.cali.gov.co/info/caligovco_se/media/bloque4439.png" alt="Logo Alcaldía de Cali" class="img-fluid">
        </div>
        <div class="col-lg-5 col-md-5 mb-4 mb-md-0">
          <h5>Alcaldía de Santiago de Cali</h5>
          <p>Dirección: Centro Administrativo Municipal (CAM)<br>
            Avenida 2 Norte #10 - 70. Santiago de Cali - Valle del Cauca - Colombia.</p>
          <p>Código postal: 760045</p>
          <p>Horario de atención: Lunes a viernes de 8:00 a.m. a 11:30 a.m. y de 2:00 p.m. a 4:30 p.m.</p>
          <a href="https://archivo.cali.gov.co" target="_blank" class="btn btn-light btn-sm">Ver portal anterior</a>
          <div class="mt-3">
            <a href="https://www.facebook.com/AlcaldiaDeCali/" class="text-white me-3"><i class="fab fa-facebook fa-lg"></i> AlcaldiaDeCali</a>
            <br>
            <a href="https://x.com/alcaldiadecali?lang=es" class="text-white me-3"><i class="fab fa-twitter fa-lg"></i> @alcaldiadecali</a>
            <br>
            <a href="https://www.instagram.com/alcaldiadecali/" class="text-white me-3"><i class="fab fa-instagram fa-lg"></i> @alcaldiadecali</a>
            <br>
            <a href="https://www.youtube.com/@AlcaldiaDeSantiagoDeCali" class="text-white"><i class="fab fa-youtube fa-lg"></i> AlcaldiadeCaliTV</a>
          </div>
        </div>
        <div class="col-lg-5 col-md-4">
          <h5>Contacto</h5>
          <p>Línea nacional: 01 8000 222 195<br>
            Líneas locales: 195 - +57 6028879020<br>
            Líneas gratuitas: 01 8000 512 734</p>
          <p>Correo institucional: <a href="mailto:contactenos@cali.gov.co" class="text-white">contactenos@cali.gov.co</a></p>
          <p>Recepción de facturas electrónicas: <a href="mailto:facturaselectronicas@cali.gov.co" class="text-white">facturaselectronicas@cali.gov.co</a></p>
          <p>Notificaciones judiciales: <a href="mailto:notificacionesjudiciales@cali.gov.co" class="text-white">notificacionesjudiciales@cali.gov.co</a></p>
          <p>Notificaciones tutelas e incidentes: <a href="mailto:notificacion.tutelas@cali.gov.co" class="text-white">notificacion.tutelas@cali.gov.co</a></p>
          <div>
            <a href="https://sig.cali.gov.co/app.php/staff/document/viewPublic/index/1195" class="text-white me-3">Políticas</a>
            <a href="https://www.cali.gov.co/mapa-del-sitio" class="text-white me-3">Mapa del sitio</a>
            <a href="https://www.cali.gov.co/publicaciones/171816/politica-de-derecho-de-autor-y-autorizacion-de-uso-sobre-los-contenidos/" class="text-white">Términos y condiciones</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style>
footer {
  background-color: #023773;
  color: white;
  margin-left: 220px; /* Deja espacio para el sidebar */
}

@media (max-width: 991px) {
  footer {
    margin-left: 0;
  }
}

footer .inner-container {
  background-color: #3366cc; /* azul claro interno */
  padding: 2rem 1rem;
  border-radius: 8px;
}

/* Para el botón volver arriba */
#btnTopPage {
  background-color: #3366cc;
  border: none;
}
#btnTopPage:hover {
  background-color: #023773;
}
</style>
<script setup lang="ts">
</script>
