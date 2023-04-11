def valeur(obj):
    return obj[1]

def poids(obj):
    return 1/obj[2]

def rapport(obj):
    return obj[1]/obj[2]

def glouton(liste, poids_max, fonction):
    liste.sort(key=fonction, reverse=True)
    poids = 0
    valeur = 0
    resultat = []
    for obj in liste:
        if poids + obj[2] <= poids_max:
            poids += obj[2]
            valeur += obj[1]
            resultat.append(obj[0])
    return resultat, valeur, poids

objets = [("A", 126, 14), ("B", 32, 2), ("C", 20, 5), ("D", 5, 1), ("E", 18, 6), ("F", 80, 8)]

"""print(glouton(objets, 15, valeur))
print(glouton(objets, 15, poids))
print(glouton(objets, 15, rapport))"""

from itertools import combinations
import random

objets = [("1", 114, 4.57), ("2", 32, 0.63), ("3", 20, 1.65), ("4", 4, 0.085), ("5", 18, 2.15), ("6", 80, 2.71), ("7", 5, 0.32)]

def brute_force(liste, poids_max):
    #with itertools.combinations
    n = len(liste)
    max = 0
    resultat = []
    for i in range(1, n+1):
        for comb in combinations(liste, i):
            poids = 0
            valeur = 0
            for obj in comb:
                poids += obj[2]
                valeur += obj[1]
            if poids <= poids_max and valeur > max:
                max = valeur
                resultat = [obj[0] for obj in comb]
    return resultat, max

"""print(brute_force(objets, 5))"""

for i in range(1, 10):
    nb = i*5
    print(nb)
    #generate random sample of size nb
    liste = [(str(i), random.randint(0, 100), random.randint(0, 100)) for i in range(nb)]
    print(liste)
    print(brute_force(liste, 100))