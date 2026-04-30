<template>
  <section id="languages" class="mt-10 px-4">
    <div class="w-full max-w-[99%] mx-auto border border-gray-700
             dark:border-gray-300 bg-[#2A8FA3]/90 dark:bg-[#186774]/90
             text-black dark:text-white backdrop-blur-md shadow-md
             rounded-3xl px-4 py-2 mb-5 transition-colors duration-300">

      <!-- Title -->
      <h2 class="text-4xl font-bold text-center text-gray-900 dark:text-white mb-6">
        Languages
      </h2>

      <div class="w-24 h-1 bg-[#234A7A] rounded-full mx-auto mb-8"></div>

      <!-- Languages Grid -->
      <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">

        <!-- French -->
        <div class="flex flex-col items-center space-y-3">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/langfr-250px-Flag_of_France.svg.png"
            alt="French Language" class="h-48 w-48 object-cover rounded-full shadow-lg 
                   border border-gray-300 dark:border-gray-700
                   transition-transform duration-300 hover:scale-105" />
          <p class="text-xl font-semibold text-gray-900 dark:text-white">French</p>
          <p class="text-gray-200 dark:text-gray-400 text-sm">Native</p>
        </div>

        <!-- English -->
        <div class="flex flex-col items-center space-y-3">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/langfr-250px-Flag_of_the_United_Kingdom_%283-5%29.svg.png"
            alt="English Language" class="h-48 w-48 object-cover rounded-full shadow-lg 
                   border border-gray-300 dark:border-gray-700
                   transition-transform duration-300 hover:scale-105" />
          <p class="text-xl font-semibold text-gray-900 dark:text-white">English</p>
          <p class="text-gray-200 dark:text-gray-400 text-sm">Intermediate level</p>
        </div>

      </div>

    </div>
  </section>
</template>
