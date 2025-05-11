#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Obtenir tous les noms définis dans le module hidden_4
    all_names = dir(hidden_4)

    # Filtrer les noms qui ne commencent pas par __
    filtered_names = [name for name in all_names if not name.startswith("__")]

    # Trier en ordre alphabétique et imprimer chaque nom sur une nouvelle ligne
    for name in sorted(filtered_names):
        print(name)
