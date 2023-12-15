if __name__ == "__main__":
  n1: int
  n2: int

  print("TP2.Ex2: Compare two integers.\n")
  
  n1 = int(input("n1 = "))
  n2 = int(input("n2 = "))

  print("\nResult : ", end="")

  if n1 > n2:
    print(f"{n1} > {n2}")
  elif n1 == n2:
    print(f"{n1} = {n2}")
  else:
    print(f"{n1} < {n2}")
  