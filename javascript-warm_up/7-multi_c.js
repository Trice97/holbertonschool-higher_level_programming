#!/usr/bin/env node
// Récupère l'argument de la ligne de commande et le convertit en entier
const x = parseInt(process.argv[2]);
// Vérifie si la conversion a échoué
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Boucle for pour afficher "C is fun" x fois
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
