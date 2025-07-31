#!/usr/bin/node

// Définition de la fonction d'addition
function add (a, b) {
  return a + b;
}

// Récupération et conversion des arguments en entiers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

// Affichage du résultat
console.log(add(a, b));
