/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    colors: {
      'delete': '#AB001D',
      'save': '#004BE0',
      'cancel_label': '#5D626F',
      'section': "#F5F7F9"
    }
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

