import random
import time


def créer_liste(N: int) -> list[int]:
    liste: list[int]
    index: int

    liste = [0] * N

    for index in range(N):
        liste[index] = random.randint(0, 100)

    return liste


def afficher_liste(liste: list[int]) -> None:
    index: int

    for index in range(len(liste)):
        print(index, liste[index])


def tri_à_bulle(liste):
    start: float
    end: float
    i: int
    j: int

    start = time.time()
    for i in range(len(liste)):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    end = time.time()
    print(f"Temps pour le tri à bulle : {end - start} secondes")
    return liste


def tri_par_insertion(liste):
    start: float
    end: float
    i: int
    j: int

    start = time.time()
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    end = time.time()
    print(f"Temps pour le tri par insertion : {end - start} seconds")
    return liste


def recherche(liste: list[int], x: int):
    bas: int
    haut: int
    mid: int

    bas = 0
    haut = len(liste) - 1
    while bas <= haut:
        mid = (haut + bas) // 2
        if liste[mid] < x:
            bas = mid + 1
        elif liste[mid] > x:
            haut = mid - 1
        else:
            return mid
    return -1


def menu():
    liste: list[int]
    choix: str

    liste = []
    choix = "-1"

    while choix != "6":
        print("1. créer un nouveau tableau")
        print("2. afficher le tableau de manière lisible")
        print("3. trier le tableau (tri à bulle), et afficher le temps de traitement")
        print("4. trier le tableau (tri par insertion), et afficher le temps de traitement")
        print("5. rechercher un élément (dans un tableau trié) ")
        print("6. quitter")
        choix = input("Entrez votre choix : ").strip()

        if choix == "1":
            N = int(input("Taille de la liste : "))
            liste = créer_liste(N)
        elif choix == "2":
            afficher_liste(liste)
        elif choix == "3":
            liste = tri_à_bulle(liste)
        elif choix == "4":
            liste = tri_par_insertion(liste)
        elif choix == "5":
            x = int(input("Entier à rechercher dans la liste: "))
            result = recherche(liste, x)
            if result != -1:
                print("Entier présent à l'index", str(result))
            else:
                print("Entier n'est pas dans la liste")
        elif choix == "6":
            break
        else:
            print("Choix invalide.")


menu()
