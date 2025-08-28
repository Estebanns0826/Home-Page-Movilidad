<template>
  <div class="page-wrapper">
    <Navbar />
    <NuxtPage />
    <Footer />
  </div>
</template>

<style>
.page-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.main-bg {
  flex: 1 0 auto;
}
</style>
