/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    'node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}'
  ],
  theme: {
    extend: {
      opacity: {
        '10': '0.1',
        '85': '0.85',
        '95': '0.95',
                }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
  darkMode: 'media',
}