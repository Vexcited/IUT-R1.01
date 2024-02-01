from typing import Optional

# structure de maillon
class Maillon:
    data: int
    suivant: Optional["Maillon"]

# structure de liste
class ListeChainee:
    tete: Optional[Maillon]

def longueur(li: ListeChainee) -> int:
  """
  Fonction qui retourne la longueur de la liste chaînée.

  use docstring:
  https://www.python.org/dev/peps/pep-0257/

  Entrée:
  
  """
  courant = li.tete
  length = 0
  while courant:
      length += 1
      courant = courant.suivant
  return length
   

def afficheLC(li: ListeChainee):
    """Fonction qui affiche les éléments de la liste

    Dans cette version, chaque élément est affiché sur une ligne

    Entrée:
        li (ListeChainee): la liste que l'on veut afficher
    """
    courant = li.tete
    while(courant):
        print(courant.data)
        courant = courant.suivant


def ajoutQueue(li: ListeChainee, val: int):
  nouveau_maillon = Maillon()
  nouveau_maillon.data = val
  nouveau_maillon.suivant = None

  if li.tete is None:
    li.tete = nouveau_maillon
  else:
    courant = li.tete
    while courant.suivant:
      courant = courant.suivant
    courant.suivant = nouveau_maillon


def ajoutTete(li: ListeChainee, val: int):
  nouveau_maillon = Maillon()
  nouveau_maillon.data = val
  nouveau_maillon.suivant = li.tete
  li.tete = nouveau_maillon

def ajoutEnPos(li: ListeChainee, indice: int, val: int):
  if indice < 0:
    print("Indice invalide")
    return

  if indice == 0:
    ajoutTete(li, val)
    return

  courant = li.tete
  for _ in range(indice - 1):
    if courant is None:
      print("Indice invalide")
      return
    courant = courant.suivant

  if courant is None:
    print("Indice invalide")
    return

  nouveau_maillon = Maillon()
  nouveau_maillon.data = val
  nouveau_maillon.suivant = courant.suivant
  courant.suivant = nouveau_maillon


def suppTete(li: ListeChainee):
  if li.tete is None:
    print("La liste est vide")
    return

  li.tete = li.tete.suivant


def suppQueue(li: ListeChainee):
  if li.tete is None:
    print("La liste est vide")
    return

  if li.tete.suivant is None:
    li.tete = None
    return

  courant = li.tete
  while courant.suivant.suivant:
    courant = courant.suivant
  courant.suivant = None


def suppEnPos(li: ListeChainee, indice: int):
  if indice < 0:
    print("Indice invalide")
    return

  if indice == 0:
    suppTete(li)
    return

  courant = li.tete
  for _ in range(indice - 1):
    if courant is None:
      print("Indice invalide")
      return
    courant = courant.suivant

  if courant is None or courant.suivant is None:
    print("Indice invalide")
    return

  courant.suivant = courant.suivant.suivant


def recherche(li: ListeChainee, val: int) -> int:
  courant = li.tete
  indice = 0
  while courant:
    if courant.data == val:
      return indice
    courant = courant.suivant
    indice += 1
  return -1


if __name__ == "__main__":
    maLC = ListeChainee()
    maLC.tete = None

    # Test ajoutTete
    ajoutTete(maLC, 42)
    ajoutTete(maLC, 23)

    # Test afficheLC
    afficheLC(maLC)

    # Test longueur
    print("Longueur de la liste:", longueur(maLC))  # On attend: 2
