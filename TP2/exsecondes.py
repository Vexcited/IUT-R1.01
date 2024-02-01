if __name__ == "__main__":
    menu_index : int

    secondes: int
    minutes: int
    heures: int
    jours: int
    semaines: int
    mois: int
    annees: int

    # On affiche le menu tant que l'utilisateur n'a pas fait une bonne sélection
    menu_index = -1
    while (menu_index != 1 and menu_index != 2):
        print("--- Menu de l'exercice secondes.")
        print("1 : Convertir des secondes en années, mois, semaines, ...")
        print("2 : Convertir des années, mois, semaines, ... en secondes")
        print("\nEntrez le numéro du menu que vous voulez sélectionner.")
        menu_index = int(input("Sélection (1 ou 2): "))
        # séparation d'une ligne
        print("")

    # Secondes -> Output
    if (menu_index == 1):
        print("--- Convertir des secondes en années, mois, semaines, ...")
        print("\nEntrez la valeur de secondes que vous souhaitez calculer.")
        
        secondes = int(input("Secondes: "))

        if (secondes < 0):
            print("Erreur: secondes est négatif.")
        else:
            print("\n--- Résultats:")

            minutes = secondes // 60
            secondes -= minutes * 60

            heures = minutes // 60
            minutes -= heures * 60

            jours = heures // 24
            heures -= jours * 24

            semaines = jours // 7
            jours -= semaines * 7

            mois = semaines // 4
            semaines -= mois * 4

            annees = mois // 12
            mois -= annees * 12

            print("annees:", annees)
            print("mois:", mois)
            print("semaines:", semaines)
            print("jours:", jours)
            print("heures:", heures)
            print("minutes:", minutes)
            print("secondes:", secondes)

    # Output -> Secondes
    elif (menu_index == 2):
        print("--- Convertir des années, mois, semaines, ... en secondes")

        secondes = int(input("secondes: "))
        minutes = int(input("minutes: "))
        heures = int(input("heures: "))
        jours = int(input("jours: "))
        semaines = int(input("semaines: "))
        mois = int(input("mois: "))
        annees = int(input("annees: "))

        secondes += (minutes * 60) + (heures * 60 * 60) + (jours * 60 * 60 * 24) + (semaines * 60 * 60 * 24 * 7) + (mois * 60 * 60 * 24 * 7 * 4) + (annees * 60 * 60 * 24 * 7 * 4 * 12)
        print("secondes:", secondes)
    else:
        print("Une erreur s'est produite, réessayez.")

    # à la ligne
    print()