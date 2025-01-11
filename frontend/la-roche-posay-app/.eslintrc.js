module.exports = {
  parser: '@typescript-eslint/parser',
  extends: [
    'next',
    'next/core-web-vitals',
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:prettier/recommended'
  ],
  plugins: ['@typescript-eslint', 'react', 'jsx-a11y', 'import', 'prettier'],
  rules: {
    'prettier/prettier': ['error', { 'endOfLine': 'auto' }]
  },
  settings: {
    react: {
      version: 'detect'
    }
  }
};
