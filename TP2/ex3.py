if __name__ == "__main__":
    l_carreau : int
    h_carreau : int
    l_surface : int
    h_surface : int
    # espace entre les carreaux
    gap : int
    # résultat
    n : float

    l_carreau = int(input("Largeur du carreau : "))
    l_surface = int(input("Largeur de la surface : "))
    h_carreau = int(input("Hauteur du carreau : "))
    h_surface = int(input("Hauteur de la surface : "))

    gap = int(input("Espace entre les carreaux : "))

    if (l_surface <= l_carreau+2*gap) or (h_surface <= h_carreau+2*gap):
        print("L doit être > à l+2*e et H doit être > à h+2*e")
    else:
        if ((l_surface - gap) % (l_carreau + gap)) == 0 or ((h_surface - gap) % (h_carreau + gap)) == 0:
            print("L-e n'est pas multiple de l+e, ni H-e de h+e")
        else:
            n = ((l_surface - gap) // (l_carreau + gap)) + 1 * ((h_surface - gap) // (h_carreau + gap)) + 1
            print("Il faut", n, "carreaux pour recouvrir la surface.\n")
