
def nmbVoyelles(text: str) -> int:
    """
    Fonction qui compte le nombre de voyelles dans le texte donné.
    """
    voyelles: list[str]
    compteur: int

    voyelles = ["a", "e", "i", "o", "u", "y", "é", "à",
                "ô", "â", "ù", "è", "ê", "ë", "ï", "î", "û"]
    compteur = 0

    for char in text:
        if char.lower() in voyelles:
            compteur += 1

    return compteur


def estPalindrome(text: str) -> bool:
    """
    Fonction qui vérifie si le texte donné est un palindrome.
    """

    i: int
    i_reverse: int
    est_palindrome: bool

    i = 0
    i_reverse = len(text) - 1
    est_palindrome = True

    while i < i_reverse:
        if text[i] != text[i_reverse]:
            est_palindrome = False
            break

        i += 1
        i_reverse -= 1

    return est_palindrome


if __name__ == "__main__":
    sélection: int
    sélection = 0
    nom: str

    while sélection != 3:
        print("""
1. Saisir un nom et afficher le nombre de voyelles
2. Saisir un nom et vérifier qu'il s'agit d'un palindrome.
3. Quitter
        """)

        sélection = int(input("Votre choix: ").strip())

        if sélection != 3:
            nom = input("Entrez un nom: ").strip()
            if sélection == 1:
                print(f"Il y a {nmbVoyelles(nom)} voyelles dans {nom}.")
            else:
                if estPalindrome(nom):
                    print(f"{nom} est un palindrome.")
                else:
                    print(f"{nom} n'est pas un palindrome.")
