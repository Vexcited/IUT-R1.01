from ex2 import estPalindrome, nmbVoyelles


def saisirNoms(noms: list[str]) -> None:
    valeur: str
    continuer: bool
    continuer = True

    while continuer:
        valeur = input("Entrez un nom: ").strip()
        noms.append(valeur)

        continuer = input("Encore un nom? (o/n): ").strip() == "o"


if __name__ == "__main__":
    noms: list[str]
    sélection: int

    noms = []
    sélection = 0

    while sélection != 4:
        print("""
1. Saisir un tableau de noms
2. afficher le nombre de voyelles par nom
3. afficher uniquement les noms étant des palindromes
4. Quitter
        """)

        sélection = int(input("Votre choix: ").strip())

        if sélection != 4:
            # si on veut saisir les noms
            if sélection == 1:
                saisirNoms(noms)
            # sinon on effectue les ops
            else:
                for nom in noms:
                    if sélection == 2:
                        print(f"{nmbVoyelles(nom)} voyelles dans {nom}.")
                    # sélection == 3
                    else:
                        if estPalindrome(nom):
                            print(nom)
