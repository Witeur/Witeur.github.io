<template>
  <nav class="sticky top-0 z-50 w-full max-w-[99%] mx-auto 
           border border-gray-700 dark:border-gray-300
           bg-[#2A8FA3] dark:bg-[#186774]
           text-black dark:text-white
           backdrop-blur-md shadow-md
           rounded-3xl px-4 py-2 mb-5 transition-colors duration-300">
    <div class="flex items-center justify-between lg:hidden">
      <span class="font-semibold">Menu</span>
      <button type="button"
        class="inline-flex items-center justify-center rounded-lg p-2 border border-black/20 dark:border-white/20"
        :aria-expanded="isMenuOpen" aria-controls="mobile-nav-menu" aria-label="Toggle navigation menu"
        @click="isMenuOpen = !isMenuOpen">
        <span class="text-sm font-semibold leading-none">
          {{ isMenuOpen ? 'Fermer' : 'Ouvrir' }}
        </span>
      </button>
    </div>

    <ul id="mobile-nav-menu" class="mt-3 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-7 
               gap-4 text-center font-medium items-center justify-center"
      :class="isMenuOpen ? 'grid' : 'hidden lg:grid'">

      <li><a href="#presentation" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Presentation</a></li>
      <li><a href="#formation" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Education</a></li>
      <li><a href="#hardskills" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Hard Skills</a></li>
      <li><a href="#softskills" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Soft Skills</a></li>
      <li><a href="#projects" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Projects</a></li>
      <li><a href="#languages" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Languages</a></li>
      <li><a href="#certifications" class="px-2 py-1 hover:text-[#F29F32] dark:hover:text-[#B87422]"
          @click="isMenuOpen = false">Certifications</a></li>

    </ul>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)
</script>
