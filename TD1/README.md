# TD1 - R1.01

## Exercice 1

### Question

What is the problem with the following program and how to fix it?

```frr
programme toto
début
  avec a, b : entier

  saisir a
  afficher "a = ", a, " et b = ", b
fin toto
```

### Answer

The problem is that `b` is not initialized, so it can contain any value. To fix this, we can initialize it to `0` for example.

```frr
programme toto
début
  avec a, b : entier

  b <- 0
  saisir a
  afficher "a = ", a, " et b = ", b
fin toto
```

Or we can add `saisir b` instruction, if the value should be user inputted.

```frr
programme toto
début
  avec a, b : entier

  saisir a
  saisir b
  afficher "a = ", a, " et b = ", b
fin toto
```

Note that there's no `afficher` before the `saisir` instructions, so the user will not know what to input. We can fix this by adding `afficher` instructions before the `saisir` ones.

```frr
programme toto
début
  avec a, b : entier

  afficher "a = "
  saisir a
  afficher "b = "
  saisir b
  afficher "a = ", a, " et b = ", b
fin toto
```

## Exercice 2, 3 and 4

Refer to the [TP2](../TP2/) since those exercices are the same but we're asked to code them in another language than pseudo code in the TP2 which is more interesting.

Even though, I'll still write the pseudo code (`.fr` files) here for the sake of completeness.
