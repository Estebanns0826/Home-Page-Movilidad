<template>
  <div class="container-fluid">
    <div class="row">
      <!-- Menú lateral izquierdo -->
      <nav class="col-2 bg-light vh-50 d-flex flex-column p-3 border-end">
        <h5 class="mb-4">Menú</h5>
        <a href="http://38.50.50.116:5000/login" class="btn btn-outline-primary mb-2 w-100">Laboratorio</a>
        <button class="btn btn-outline-primary mb-2 w-100">Planeamiento</button>
        <a href="http://38.50.50.166/tickets-app/" class="btn btn-outline-primary mb-2 w-100">Tickets</a>
        <button class="btn btn-outline-primary mb-2 w-100">Interconexión</button>
      </nav>
      
      <div class="col-md-4">
        <div class="card h-100 shadow-sm border-0 hover-shadow transition">
          <img src="/imagenes/foto1.jpg" class="card-img-top" style="height: 200px; object-fit: cover;" alt="Tickets">
          <div class="card-body">
            <a href="http://38.50.50.166/tickets" class="stretched-link fw-bold text-decoration-none text-primary">Tickets</a>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card h-100 shadow-sm border-0 hover-shadow transition">
          <img src="/imagenes/foto3.jpg" class="card-img-top" style="height: 200px; object-fit: cover;" alt="Geoserver">
          <div class="card-body">
            <a href="http://38.50.50.166:9090/geoserver" class="stretched-link fw-bold text-decoration-none text-primary">Geoserver</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <News />
</template>

<script setup>
// Aquí puedes añadir lógica de Vue/Nuxt si necesitas
</script>

<style>
/* Ajustes opcionales */
body {
  margin: 0;
}
</style>

