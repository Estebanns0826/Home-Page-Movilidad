<template>
  <div class="min-h-screen flex flex-col">
    <!-- Franja azul superior -->
    <div class="bg-[#003DA5] flex justify-between items-center px-4 py-2">
 
    </div>

    <!-- Franja blanca con enlaces desplegables -->
    <div class="bg-white shadow-md border-b">
      <ul class="flex flex-wrap justify-center py-2 text-sm font-medium text-black">
        <!-- ... tus botones desplegables como están ... -->
        <!-- No es necesario modificar esta sección -->
      </ul>
    </div>

    <!-- Contenido principal (flex-grow para empujar el footer abajo) -->
    <div class="flex-grow">
      <!-- Menú de accesos rápidos -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 p-4 text-center bg-gray-50">
        <!-- ... accesos rápidos ... -->
      </div>

      <!-- Carrusel de imágenes -->
      <div class="container mx-auto my-8">
        <!-- ... carrusel ... -->
      </div>

      <!-- Enlaces adicionales -->
       <div class="text-center mb-4">
  <div class="d-flex flex-column align-items-center gap-2">
    <img src="/imagenes/foto5.jpg" alt="Geonetwork" class="img-fluid mb-2" style="max-width: 150px;" />
    <a href="#" class="text-primary text-decoration-none">Geonetwork (Metadatos)</a>
  </div>
</div>
      <div class="text-center mb-4">
        <div class="d-flex justify-content-center flex-wrap gap-3">
          <a href="#" class="text-primary text-decoration-none">Geonetwork (Metadatos)</a>
          
        </div>
      </div>
    </div>

    <!-- Pie de página institucional -->
    <footer class="bg-primary text-white text-center py-4 mt-auto">
      <div class="container">
        <p class="mb-3 mb-md-2">&copy; 2025 Alcaldía de Santiago de Cali. Todos los derechos reservados.</p>
        <div class="d-flex flex-column flex-md-row justify-content-center align-items-center gap-2">
          <a href="#" class="text-white text-decoration-none">Mapa del sitio</a>
          <span class="d-none d-md-inline">|</span>
          <a href="#" class="text-white text-decoration-none">Política de privacidad</a>
          <span class="d-none d-md-inline">|</span>
          <a href="#" class="text-white text-decoration-none">Contáctenos</a>
        </div>
      </div>
    </footer>
  </div>
</template>