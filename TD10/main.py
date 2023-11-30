from typing import TextIO

if __name__ == "__main__":
    attend_chaîne: bool
    char_actuel: str
    nb_répétition: int
    répétition_chaîne: str
    f: TextIO

    f = open("fichier.txt", "r")
    char_actuel = f.read(1)

    f.close()
