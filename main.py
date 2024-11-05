# main.py
"""
author = klaus.kapllani@esiee.fr
"""

#### Imports et définition des variables globales
import sys

# La limite en python étant de 1000 pour valider les tests unitaires,
# je décide de l'augmenter à 2000
sys.setrecursionlimit(2000)

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []

    l = []
    c_i = s[0]
    occurence = 0
    for c in s:
        if c == c_i:
            occurence += 1
        else:
            l.append((c_i, occurence))
            c_i = c
            occurence = 1
    l.append((c_i, occurence))
    return l

def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []
    # cas de base
    caractere = s[0]
    occurence = 1

    # recherche nombre de caractères identiques au premier
    while occurence < len(s) and s[occurence] == caractere:
        occurence += 1

    # appel récursif
    return [(caractere, occurence)] + artcode_r(s[occurence:])

def main():
    """
    Fonction principale qui print la liste de tuple d'abord en itératif,
    puis en récurcif.

    Returns :
        rien
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
