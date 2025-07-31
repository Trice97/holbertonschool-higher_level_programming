#!/usr/bin/node

// Fonction récursive pour calculer la factorielle
function factorial (n) {
  if (isNaN(n) || n < 0) return 1;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}

// Récupère l'argument et le convertit en entier
const n = parseInt(process.argv[2]);

// Affiche le résultat
console.log(factorial(n));
