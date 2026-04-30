<template>
  <footer id="contact" class="mt-10 px-4">
    <div class="box-border w-full max-w-[99%] mx-auto 
             border border-gray-800 dark:border-gray-300 
             p-10 rounded-3xl mb-5 shadow-lg dark:shadow-xl
             bg-[#234A7A]/90 dark:bg-[#0C203A]/90
             transition-colors duration-300">

      <!-- Title -->
      <h2 class="text-3xl font-bold text-center text-white mb-6">
        Contact
      </h2>

      <!-- Contact Form -->
      <section id="contact-form" class="mb-10">
        <form action="https://formsubmit.co/50d8c06973ec735f50236ccdf77b1483" method="POST"
          class="max-w-xl mx-auto space-y-6">

          <!-- Name -->
          <input type="text" name="name" placeholder="Your name" required
            class="w-full p-3 rounded-xl bg-white/20 text-white placeholder-gray-300" />

          <!-- Email -->
          <input type="email" name="email" placeholder="Your email" required
            class="w-full p-3 rounded-xl bg-white/20 text-white placeholder-gray-300" />

          <!-- Message -->
          <textarea name="message" placeholder="Your message" required
            class="w-full p-3 rounded-xl bg-white/20 text-white placeholder-gray-300 h-32"></textarea>

          <!-- Button -->
          <button type="submit"
            class="w-full bg-[#3CC7E8] text-black font-bold p-3 rounded-xl hover:scale-105 transition">
            Send
          </button>

          <!-- Security -->
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">

        </form>
      </section>

      <!-- Social Icons -->
      <div class="flex justify-center space-x-6 mt-10">

        <!-- GitHub -->
        <a href="https://github.com/Witeur" target="_blank">
          <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" class="w-10 h-10 hover:scale-110 transition" />
        </a>

        <!-- LinkedIn -->
        <a href="https://www.linkedin.com/in/enzo-bavigne/" target="_blank">
          <img src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png" alt="LinkedIn"
            class="w-10 h-10 hover:scale-110 transition" />
        </a>

        <!-- CV -->
        <a href="/CV-Enzo-BAVIGNE.pdf" target="_blank">
          <img src="../assets/cv-logo-template-icon-isolated-on-black-background-png_130993.jpg" alt="CV"
            class="w-10 h-10 hover:scale-110 transition" />
        </a>

      </div>

    </div>
  </footer>
</template>
