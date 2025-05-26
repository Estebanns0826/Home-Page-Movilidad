<template>
  <div class="container py-5 bg-light">
    <div class="row g-4 text-center">
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
          <img src="/imagenes/foto2.jpg" class="card-img-top" style="height: 200px; object-fit: cover;" alt="Tableros">
          <div class="card-body">
            <a href="#" class="stretched-link fw-bold text-decoration-none text-primary">Tableros (Locker Studio)</a>
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
import '~/assets/login.css'
</script>

