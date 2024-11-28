/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        background: '#171a21', // Casi negro
        primary: '#1b2838', // Azul oscuro
        secondary: '#2a475e', // Azul claro
        accent: '#66c0f4', // Azul claro
        neutral: '#c7d5e0', // blanco
        'base-100': '#c7d5e0', // Blanco
        info: '#3B82F6', // Azul claro
        success: '#22C55E', // Verde claro
        warning: '#FBBF24', // Amarillo claro
        error: '#EF4444', // Rojo
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

