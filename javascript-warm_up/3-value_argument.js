#!/usr/bin/node

// Récupère le premier argument passé (après le nom du script)
const arg = process.argv[2];

// Vérifie si l'argument existe
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
