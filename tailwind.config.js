export default {
  darkMode: 'media',
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  safelist: [
    'bg-light-pattern',
    'dark:bg-dark-pattern'
  ],
  theme: {
    extend: {
      backgroundImage: {
        'light-pattern': "url('/background-light.png')",
        'dark-pattern': "url('/background-dark.png')",
      },
    },
  },
  plugins: [],
}
