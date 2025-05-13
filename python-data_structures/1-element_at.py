#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None  # Si l'index est négatif, on retourne None
    elif idx >= len(my_list):
        return None  # Si l'index est hors de portée, on retourne None
    else:
        return my_list[idx]  # Sinon, on retourne l'élément à l'index idx
