<template>
  <section class="container my-5">
    <h2 class="mb-4">Últimas Noticias</h2>
    <div class="row">
      <article v-for="noticia in noticias" :key="noticia.id" class="col-md-4 mb-4">
        <div class="card h-100 shadow-sm">
          <img :src="noticia.imagen" class="card-img-top" :alt="noticia.titulo" />
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">{{ noticia.titulo }}</h5>
            <p class="card-text flex-grow-1">{{ noticia.resumen }}</p>
            <a :href="noticia.link" target="_blank" class="btn btn-primary mt-auto">Leer más</a>
          </div>
          <div class="card-footer text-muted">
            {{ new Date(noticia.fecha).toLocaleDateString() }}
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
const noticias = [
  {
    id: 1,
    titulo: "Nueva iniciativa de desarrollo sostenible",
    resumen: "El gobierno local lanza un programa para impulsar proyectos ecológicos en la ciudad.",
    imagen: "https://via.placeholder.com/400x200?text=Noticia+1",
    link: "#",
    fecha: "2025-05-01"
  },
  {
    id: 2,
    titulo: "Mejoras en infraestructura vial",
    resumen: "Se inician las obras para modernizar las principales avenidas de la capital.",
    imagen: "https://via.placeholder.com/400x200?text=Noticia+2",
    link: "#",
    fecha: "2025-05-15"
  },
  {
    id: 3,
    titulo: "Eventos culturales para el verano",
    resumen: "Agenda completa de conciertos, ferias y exposiciones para disfrutar en la ciudad.",
    imagen: "https://via.placeholder.com/400x200?text=Noticia+3",
    link: "#",
    fecha: "2025-05-20"
  }
]
</script>

<style scoped>
.card {
  transition: transform 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}
</style>
