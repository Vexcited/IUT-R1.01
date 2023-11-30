from random import randint


def randomiser_tableau(tab: list[int]) -> None:
    """
    Procédure qui modifie le tableau donné.
    """

    for i in range(len(tab)):
        tab[i] = randint(0, 100)


if __name__ == "__main__":
    tab_10: list[int]
    tab_2d: list[list[int]]
    taille: int

    # Remplissage d'un tableau de 10 éléments
    tab_10 = [0] * 10
    for i in range(10):
        tab_10[i] = int(input(f"Entrez un nombre pour l'index {i}: ").strip())

    # Affichage du tableau
    for index in range(len(tab_10)):
        print(f"tab_10[{index}] = {tab_10[index]}")

    taille = int(input("Taille du tableau 2D: ").strip())
    tab_2d = [[0] * taille for _ in range(taille)]
    # Remplissage de la première ligne du tableau
    for i in range(taille):
        tab_2d[0][i] = int(input(
            f"Entrez un nombre pour l'index {i} de la première ligne du tableau: ").strip())

    # Affichage du tableau
    for i in range(len(tab_2d)):
        for j in range(len(tab_2d[i])):
            print(tab_2d[i][j], end=" ")

        # à la ligne
        print()
    # à la ligne
    print()

    # Appel de la procédure
    randomiser_tableau(tab_10)
    # Affichage du tableau
    for index in range(len(tab_10)):
        print(f"tab_10[{index}] = {tab_10[index]}")
