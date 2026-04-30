<template>
  <div class="min-h-screen bg-light-pattern dark:bg-dark-pattern transition-colors duration-500">

    <Header />
    <Navbar />

    <main>
      <Presentation />
      <Formation />
      <HardSkills />
      <SoftSkills />
      <Projects />
      <Languages />
      <Certifications />
    </main>

    <Footer />

  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import Navbar from './components/Navbar.vue'
import Presentation from './components/Presentation.vue'
import Formation from './components/Formation.vue'
import HardSkills from './components/HardSkills.vue'
import SoftSkills from './components/SoftSkills.vue'
import Projects from './components/Projects.vue'
import Languages from './components/Languages.vue'
import Certifications from './components/Certifications.vue'
import Footer from './components/Footer.vue'
</script>
