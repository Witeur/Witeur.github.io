<template>
  <section id="projects" class="mt-10 px-4">
    <div class="box-border w-full max-w-[99%] mx-auto 
             border border-gray-800 dark:border-gray-300 
             p-10 rounded-3xl mb-5 shadow-lg dark:shadow-xl
             bg-[#234A7A]/90 dark:bg-[#0C203A]/90
             transition-colors duration-300">

      <!-- Title -->
      <h2 class="text-4xl font-bold text-center text-white mb-6">
        Projects
      </h2>

      <div class="w-24 h-1 bg-[#F29F32] rounded-full mx-auto mb-8"></div>

      <!-- Projects Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">

        <!-- Yowl Project -->
        <div class="bg-white dark:bg-[#0C203A] p-4 rounded-2xl shadow-lg 
                 border border-gray-300 dark:border-gray-700
                 transition-transform duration-300 hover:scale-105">
          <a href="/B-TBM-100-RUN-1-1-yowl-2.zip" download="yowl.zip">
            <img src="../assets/Pasted-image (2).png" alt="Yowl" class="w-full h-40 object-cover rounded-xl mb-4" />
          </a>

          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            Yowl
          </h3>

          <p class="text-gray-700 dark:text-gray-300 text-sm mt-2">
            Yowl Project: documentation and market analysis to adapt a social network to user needs.
          </p>
        </div>

        <!-- E‑Todo Project -->
        <div class="bg-white dark:bg-[#0C203A] p-4 rounded-2xl shadow-lg 
                 border border-gray-300 dark:border-gray-700
                 transition-transform duration-300 hover:scale-105">
          <a href="/e-Todo.zip" download="e-Todo.zip">
            <img src="../assets/Homepage.png" alt="E‑Todo" class="w-full h-40 object-cover rounded-xl mb-4" />
          </a>

          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            E‑Todo
          </h3>

          <p class="text-gray-700 dark:text-gray-300 text-sm mt-2">
            Web-based task management application, deployed using Docker.
          </p>
        </div>

        <!-- Ti Data Project -->
        <div class="bg-white dark:bg-[#0C203A] p-4 rounded-2xl shadow-lg 
                 border border-gray-300 dark:border-gray-700
                 transition-transform duration-300 hover:scale-105">
          <a href="/B-TBM-100-RUN-1-1-productdesignhackathon-3.zip"
            download="B-TBM-100-RUN-1-1-productdesignhackathon-3.zip">
            <img src="../assets/Pasted-image.png" alt="Ti Data" class="w-full h-40 object-cover rounded-xl mb-4" />
          </a>

          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            Ti Data
          </h3>

          <p class="text-gray-700 dark:text-gray-300 text-sm mt-2">
            Hackathon project: a website highlighting local information rarely showcased in Réunion Island.
          </p>
        </div>

      </div>

    </div>
  </section>
</template>
