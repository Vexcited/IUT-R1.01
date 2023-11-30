class Livre:
  titre : str
  auteur : str
  annee : int
  pages : int

def afficherLivre(livre: Livre) -> None:
  print(f"{livre.titre} de {livre.auteur} ({livre.annee})")

def afficherBibliothèque(bibliothèque: list[Livre]) -> None:
  # Afficher l'ensemble des livres de la bibliothèque
  for livre in bibliothèque:
    afficherLivre(livre)

def rechercherLivre(bibliothèque: list[Livre]) -> None:
  # Rechercher un livre (par le titre)
  titre = input("Titre : ")
  for livre in bibliothèque:
    if livre.titre == titre:
      afficherLivre(livre)

def ajouterLivre(bibliothèque: list[Livre]) -> None:
  livre = Livre()
  livre.titre = input("Titre : ")
  livre.auteur = input("Auteur : ")
  livre.annee = int(input("Année : "))
  livre.pages = int(input("Pages : "))
  bibliothèque.append(livre)

if __name__ == "__main__":
  # Création de la bibliothèque
  bibliothèque: list[Livre] = []
  choix = 0

  # Menu
  while choix != 4:
    print("1. Afficher l'ensemble des livres de la bibliothèque")
    print("2. Ajouter un nouveau livre")
    print("3. Rechercher un livre (par le titre)")
    print("4. Quitter")
    choix = int(input("Votre choix : "))

    if choix == 1:
      # Afficher l'ensemble des livres de la bibliothèque
      afficherBibliothèque(bibliothèque)
    elif choix == 2:
      # Ajouter un nouveau livre
      ajouterLivre(bibliothèque)
    elif choix == 3:
      rechercherLivre(bibliothèque)
