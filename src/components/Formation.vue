<template>
  <section id="formation" class="mt-10 px-4">
    <div class="box-border w-full max-w-[99%] mx-auto 
           border border-gray-800 dark:border-gray-300 
           p-10 rounded-3xl mb-5 shadow-lg dark:shadow-xl
           bg-[#234A7A]/90 dark:bg-[#0C203A]/90
           transition-colors duration-300">

      <!-- Title -->
      <h2 class="text-4xl font-bold text-center text-gray-900 dark:text-white mb-6">
        Education
      </h2>

      <div class="w-24 h-1 bg-[#F29F32] rounded-full mx-auto mb-8"></div>

      <!-- Education Grid -->
      <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

        <!-- Bac STMG -->
        <div class="flex flex-col items-center space-y-3">
          <img src="../assets/bac-stmg.webp" alt="Bac STMG" class="h-48 w-48 object-cover rounded-full shadow-lg 
                 border border-gray-300 dark:border-gray-700
                 transition-transform duration-300 hover:scale-105" />
          <p class="text-xl font-semibold text-gray-900 dark:text-white">Bac STMG</p>
          <p class="text-gray-200 dark:text-gray-400 text-sm">2024 – 2025</p>
        </div>

        <!-- Bachelor Epitech -->
        <div class="flex flex-col items-center space-y-3">
          <img src="../assets/bachelor.jpeg" alt="Bachelor Epitech" class="h-48 w-48 object-cover rounded-2xl shadow-lg 
                 border border-gray-300 dark:border-gray-700
                 transition-transform duration-300 hover:scale-105" />
          <p class="text-xl font-semibold text-gray-900 dark:text-white">Epitech Bachelor</p>
          <p class="text-gray-200 dark:text-gray-400 text-sm">2025 – Present</p>
        </div>

      </div>
    </div>

  </section>
</template>
