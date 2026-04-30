<template>
  <header class="box-border w-full max-w-[99%] 
          mx-auto border border-gray-800
          dark:border-white p-4 rounded-3xl mb-5
          bg-[#234A7A] dark:bg-[#0C203A]
          transition-colors duration-300">
    <div class="max-w-9xl mx-auto 
              grid grid-cols-1 md:grid-cols-3 
              items-center gap-4">

      <!-- Logo -->
      <div class="flex justify-center md:justify-start">
        <img src="../assets/logo.png" alt="Logo" class="h-20 object-contain rounded-3xl" />
      </div>

      <!-- Nom + phrase -->
      <div class="flex flex-col justify-center items-center md:items-start text-center md:text-left">
        <h1 class="text-3xl font-bold text-gray-900 dark:text-gray-100">
          Enzo Bavigne
        </h1>
        <p class="text-sm text-gray-800 dark:text-gray-300">
          Bachelor's student at Epitec
        </p>
      </div>

      <!-- Portfolio -->
      <div class="flex justify-center md:justify-end">
        <h2 class="text-2xl font-semibold text-gray-800 dark:text-gray-300">
          Portfolio
        </h2>
      </div>

    </div>
  </header>
</template>
