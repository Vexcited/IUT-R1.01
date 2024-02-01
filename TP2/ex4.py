import math

if __name__ == "__main__":
    a : float
    b : float
    c : float
    delta : float

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # bx + c = 0
    # x = -c/b 
    if a == 0:
        print("Equation du premier degré: x =", -c/b)
    else:
        delta = b**2-4*a*c
        if (delta < 0):
            print("pas de solution, delta < 0")
        else:
            if (delta == 0):
                print("une seule solution, x =", -b/(2*a))
            else:
                print("deux solutions: x1 =", (-b+math.sqrt(delta))/(2*a), "; x2 =", (-b-math.sqrt(delta))/(2*a))
