
def calculAnnee (d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int :
  """
  Écrire une fonction qui calcule le nombre d'années (entières) qui s'écoulent entre deux dates (jour, mois, année),
  la première date étant antérieure à la seconde.

  On return -1 si les dates ne sont pas valides ou si elles ne sont pas dans le bon ordre.
  """

  # On vérifie que les dates sont valides
  if not (1 <= d1 <= 31 and 1 <= d2 <= 31 and 1 <= m1 <= 12 and 1 <= m2 <= 12):
    return -1

  # On vérifie que les dates sont dans le bon ordre
  if y1 > y2 or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
    return -1

  # On calcule le nombre d'années
  nbAnnées = y2 - y1

  # On vérifie si on a dépassé la date anniversaire
  if m1 > m2 or (m1 == m2 and d1 > d2):
    nbAnnées -= 1

  return nbAnnées

def calculQualifié (age: int) -> str :
  """
  On qualifie une personne en fonction de son âge selon les critères suivant (on suppose que
  l'âge de la retraite est 65 ans) :
  - « mineure »
  - « majeure »
  - « vingtenaire »
  - « trentenaire »
  - « quadragénaire »
  - « quinquagénaire »
  - « sexagénaire »
  - « retraitée »

  La vérification de l'âge se fait dans la fonction principale.
  """

  out : str
  out = ""

  if age < 18:
    out = "mineure"
  else:
    out = "majeure"

  if age >= 20 and age < 30:
    out += ", vingtenaire"
  elif age >= 30 and age < 40:
    out += ", trentenaire"
  elif age >= 40 and age < 50:
    out += ", quadragénaire"
  elif age >= 50 and age < 60:
    out += ", quinquagénaire"
  elif age >= 60 and age < 70:
    out += ", sexagénaire"
  
  if age >= 65:
    out += ", retraitée"

  return out

if __name__ == "__main__":
  age : int
  qualifié : str
  d1: int
  m1: int
  y1: int
  d2: int
  m2: int
  y2: int

  # On demande à l'utilisateur de rentrer les dates
  d1 = int(input("Jour de la première date : "))
  m1 = int(input("Mois de la première date : "))
  y1 = int(input("Année de la première date : "))
  d2 = int(input("Jour de la seconde date : "))
  m2 = int(input("Mois de la seconde date : "))
  y2 = int(input("Année de la seconde date : "))

  # On calcule le nombre d'années
  age = calculAnnee(d1, m1, y1, d2, m2, y2)

  # On vérifie que les dates sont valides
  if age == -1:
    print("Les dates ne sont pas valides ou ne sont pas dans le bon ordre.")
  else:
    # On qualifie l'âge
    qualifié = calculQualifié(age)

    # On affiche le résultat
    print("La personne est", qualifié)
