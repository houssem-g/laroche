import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        'la-roche-posay-blue': '#005A9C',       // Bleu principal
        'la-roche-posay-white': '#FFFFFF',      // Blanc
        'la-roche-posay-gray': '#F5F5F5',       // Gris clair
        'la-roche-posay-dark-blue': '#003366',  // Bleu foncé
        // Ajoutez d'autres couleurs spécifiques si nécessaire
      },
    },
  },
  plugins: [],
};
export default config;
