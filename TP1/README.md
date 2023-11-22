# TP1 - R1.01 - Introduction to Python

## Table of contents

- [TP1 - R1.01 - Introduction to Python](#tp1---r101---introduction-to-python)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Choice of IDE](#choice-of-ide)
  - [Installation](#installation)
    - [Visual Studio Code](#visual-studio-code)
    - [Python](#python)
    - [Python plugin for Visual Studio Code](#python-plugin-for-visual-studio-code)
    - [Git (optional)](#git-optional)
  - [Settings](#settings)
  - [Write our first program : `./first.py`](#write-our-first-program--firstpy)

## Introduction

There's many practical goals to achieve in this first TP, which will serve as a basis for all the following ones: have an idea of what an IDE is, write and test your first instructions and programs, put into practice the first notions of the course and the TD.

We will use the Python language, which is a very popular language, especially in the field of data science. It is also a language that is easy to learn and use, which will allow us to focus on the notions of the course rather than on the language itself.

## Choice of IDE

**Visual Studio Code**, which is an "extensible code editor" (and not an Integrated Development Environment IDE, even if the limit between the two becomes thin). It is specialized for programmers and has a plugin mechanism that adds to the editor features specific to languages for example. This year we will use the Microsoft "Python" plugin (available on Windows, Linux and macOS).

## Installation

### Visual Studio Code

Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).

### Python

Download and install Python from the [official website](https://www.python.org/downloads/) if you're on Windows or macOS.

Otherwise, if you're on Linux, you can install it from your distribution's package manager. For example, on Ubuntu, you can run the following command in a terminal:

```bash
sudo apt install python3
```

### Python plugin for Visual Studio Code

In Visual Studio Code, go to the "Extensions" tab (or press `Ctrl+Shift+X`), search for "ms-python.python" and install the plugin "Python" by Microsoft.

### Git (optional)

Look at the download and install instructions from the [official website](https://git-scm.com/downloads).

## Settings

We have to configure Visual Studio Code to use `strict` type checking mode, which will allow us to find more errors. To do this, open the settings (File > Preferences > Settings) and search for "python type checking mode". Then select "strict" in the dropdown menu.

## Write our first program : `./first.py`

```fr
programme HelloWorld
début
  afficher "Hello World!"
fin HelloWorld
```

Write a Python program that displays "Hello World!" on the screen.
