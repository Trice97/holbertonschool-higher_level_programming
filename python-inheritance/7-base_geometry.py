#!/usr/bin/python3
"""Module contenant la classe BaseGeometry avec une méthode de validation d'entier."""

class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Méthode qui doit être implémentée dans les classes filles."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier strictement positif.

        Args:
            name (str): le nom du paramètre (utilisé dans le message d'erreur).
            value (int): la valeur à valider.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est inférieur ou égal à 0.

        Examples:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 5)
            >>> bg.integer_validator("height", "10")
            Traceback (most recent call last):
            ...
            TypeError: height must be an integer
            >>> bg.integer_validator("height", 0)
            Traceback (most recent call last):
            ...
            ValueError: height must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

