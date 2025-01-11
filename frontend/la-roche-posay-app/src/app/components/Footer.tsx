// src/components/Footer.tsx
import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-la-roche-posay-dark-blue text-la-roche-posay-white p-4 mt-auto">
      <p className="text-center">&copy; {new Date().getFullYear()} La Roche-Posay. Tous droits réservés.</p>
    </footer>
  );
};

export default Footer;
