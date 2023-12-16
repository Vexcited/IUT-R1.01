# TP2 - R1.01

## Table of contents

Every exercices given are from the [TD1](../TD1/README.md), except for the exercise 1 which is just a syntax issue to solve.

Also, there's an additional exercise at the end of the TP, "Secondes", which is not from the TD.

- [TD1 - Exercice 2: Compare two integers](#td1---exercice-2-compare-two-integers)
- [TD1 - Exercice 3: A small mathematical problem](#td1---exercice-3-a-small-mathematical-problem)

## TD1 - Exercice 2: Compare two integers

Write a program that allows to enter two integers, then to display them with the right order symbol among <, > and = (if the user enters `5` and `9`, we want to display `5 < 9`)

- [x] [Python 3](./ex2.py)
- [x] [Rust](./ex2.rs)
- [x] [Zig](./ex2.zig)
- [x] [`frr`](./ex2.fr)
- [ ] C

## TD1 - Exercice 3: A small mathematical problem

Given a rectangular surface `S`, of size `L*H` (`L` and `H` are integers, and represent millimeters), which we want to tile using rectangular tiles, of size `l*h` (also integers, in millimeters).

We will assume that between each tile there is a cement area of thickness `e` (also an integer, in millimeters).

**What is the number N (integer) of tiles needed to cover S?**

We will assume to simplify the problem that if a tile needs to be "cut", the reject (i.e. the remaining part) cannot be reused, even if this reject is of a large size.

We will also assume that `L>l+2*e` and `H>h+2*e`, and that `L-e` is not a multiple of `l+e`, nor `H-e` of `h+e`.

- [x] [Python 3](./ex3.py)
- [ ] Rust
- [ ] Zig
- [x] [`frr`](./ex3.fr)
- [ ] C
