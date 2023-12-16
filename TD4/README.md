# TD4 - R1.01

## Exercice 1

Écrire un algorithme permettant d'afficher tous les nombres parfaits compris entre 1 et `n`, avec `n` saisi par l'utilisateur.

> Reminder : Un nombre est dit parfait lorsqu'il vaut la somme de tous ses diviseurs (lui-même exclu). Exemple : 6 est un nombre parfait, car 6 = 1 + 2 + 3

**Présenter cet algorithme sous la forme d'une fonction ainsi qu'un programme l'utilisant.**

## Exercice 2

Écrire une fonction permettant de vérifier qu'une date est valide (déjà fait en TP) sachant que :

- on se place exclusivement dans le cadre du calendrier grégorien, à partir de l'année 1583 (les dates plus anciennes seront considérées comme invalides) ;
- **aucun "si alors sinon" n'est autorisé dans la fonction** ;
- la fonction retourne un booléen et peut être utilisée dans le programme principal comme suit : `si dateValide(jour, mois, annee) alors ...`

## Exercice 3

La Société L, spécialisée dans le matériel électrique, emballe les ampoules qui lui sont commandées par des détaillants dans des cartons de type **grand** (contenant 200 ampoules), **moyen** (contenant 50 ampoules) et **petit** (contenant 10 ampoules). Les quantités commandées doivent être multiples de 10.

Écrire un programme qui saisit une quantité commandée et affiche les nombres de cartons **grand**, **moyen** et **petit** nécessaires. On cherche à utiliser le maximum d'emballages de grande contenance.

### Consigne

Le programme disposera d'un menu permettant de :

1. Entrer le nombre d'ampoules ;
2. Calculer et afficher les emballages ;
3. Quitter

Le programme doit faire usage de fonctions.

### Exemple

Pour une commande de 360 ampoules, il faut 1 carton de 200 ampoules, 3 cartons de 50 ampoules et 1 carton de 10 ampoules.
