# Utiliser une image Node.js officielle comme image de base
FROM node:18-alpine

# Définir le répertoire de travail
WORKDIR /frontend/la-roche-posay-app

# Copier les fichiers de dépendances
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier le reste de l'application
COPY . .


# Exposer le port sur lequel l'application Next.js va tourner
EXPOSE 3000

# Commande pour lancer l'application Next.js en production
CMD ["npm", "start"]
