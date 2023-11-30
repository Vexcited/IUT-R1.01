def calculR (a: int, n: int) -> int:
  """
  Fonction qui calcule récursivement a^n.

  Entrée : a, un entier.
           n, un entier positif ou nul.
  Sortie : a^n.
  """

  calcul : int

  if n == 0:
    return 1
  elif n % 2 == 0:
    calcul = calculR(a, n // 2)
    return calcul * calcul
  else:
    calcul = calculR(a, (n - 1) // 2)
    return a * calcul * calcul
  
if __name__ == "__main__":
  a : int
  n : int
  out : int

  a = int(input("Entrez un entier : "))
  n = int(input("Entrez un entier positif ou nul : "))
  out = calculR(a, n)

  print(a, "^", n, "=", out)
