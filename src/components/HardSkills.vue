<template>
  <section id="hardskills">
    <div class="box-border w-full max-w-[99%] mx-auto 
           border border-gray-800 dark:border-gray-300 
           p-10 rounded-3xl mb-5
           bg-[#2996AE]/90 dark:bg-[#1A3A63]/90
           transition-colors duration-300">


      <h2 class="text-4xl font-bold text-center text-white mb-6">
        Hard Skills
      </h2>

      <div class="w-24 h-1 bg-[#234A7A] rounded-full mx-auto mb-8"></div>

      <!-- Carousel -->
      <div class="flex gap-8 overflow-x-auto snap-x snap-mandatory px-4 pb-4">
        <div v-for="skill in skills" :key="skill.name" class="min-w-37.5 snap-center flex flex-col items-center">
          <img :src="skill.img" :alt="skill.name" class="w-28 h-28 object-contain rounded-xl shadow-lg
                 transition-transform duration-300 hover:scale-110" />
          <p class="text-white text-lg font-semibold mt-3">{{ skill.name }}</p>
        </div>
      </div>
    </div>

  </section>
</template>

<script setup>
const skills = [
  { name: "Python", img: "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" },
  { name: "HTML5", img: "https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" },
  { name: "CSS", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/250px-CSS3_logo_and_wordmark.svg.png" },
  { name: "PHP", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/PHP-logo.svg/1200px-PHP-logo.svg.png" },
  { name: "SQL", img: "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" },
  { name: "JavaScript", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Javascript-shield.svg/500px-Javascript-shield.svg.png" },
  { name: "Docker", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Docker_Logo.png/960px-Docker_Logo.png" },
  { name: "Vue.js", img: "https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg" },
  { name: "OWASP", img: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/OWASP_black_logo.svg/250px-OWASP_black_logo.svg.png" },
  { name: "Bash", img: "https://upload.wikimedia.org/wikipedia/commons/4/4b/Bash_Logo_Colored.svg" },
  { name: "Bootstrap", img: "https://upload.wikimedia.org/wikipedia/commons/b/b2/Bootstrap_logo.svg" },
  { name: "Tailwind CSS", img: "https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" },
  { name: "Burp Suite", img: "https://th.bing.com/th/id/OIP.DMTfM26XGoaULINkIq9SNQHaDt?w=326&h=175&c=7&r=0&o=7&pid=1.7&rm=3" }
];
</script>
