def sommeR_récursif (n: int) -> int :
  """
  Fonction qui calcule la somme des n premiers entiers naturels
  de manière récursive.

  Entrée : n, un entier naturel.
  Sortie : la somme des n premiers entiers naturels.
  """
  if n == 1:
    return 1
  else:
    return n + sommeR_récursif(n - 1)

def sommeR_itératif (n: int) -> int :
  """
  Fonction qui calcule la somme des n premiers entiers naturels
  de manière itérative.

  Entrée : n, un entier naturel.
  Sortie : la somme des n premiers entiers naturels.
  """
  
  out : int
  out = 0

  for i in range(1, n + 1):
    out += i

  return out

if __name__ == "__main__":
  n : int
  somme : int

  n = int(input("Entrez un entier naturel : "))
  somme = sommeR_itératif(n)


  print("La somme des", n, "premiers entiers naturels est", somme)
