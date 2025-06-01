#!/usr/bin/python3
"""Module contenant la classe BaseGeometry avec validation d'entiers."""


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Méthode à implémenter dans les classes filles."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que value est un entier > 0.

        Args:
            name (str): le nom du paramètre.
            value (int): la valeur à valider.

        Raises:
            TypeError: si value n'est pas un int.
            ValueError: si value <= 0.

        Examples:
            >>> bg = BaseGeometry()
            >>> bg.integer_validator("width", 10)
            >>> bg.integer_validator("width", "10")
            Traceback (most recent call last):
            ...
            TypeError: width must be an integer
            >>> bg.integer_validator("width", 0)
            Traceback (most recent call last):
            ...
            ValueError: width must be greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
