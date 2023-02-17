import random
import time
from matplotlib import pyplot

def recherche(x, t): # x est l'élément recherché, t est la liste
    n = len(t) # n est la taille de la liste
    i = 0 # i est l'indice de parcours de la liste
    while (i < n and x != t[i]): # on continue tant que l'on n'a pas trouvé l'élément ou qu'on n'est pas arrivé à la fin de la liste
        i = i + 1 # on passe à l'élément suivant
    if i < n: # si on a trouvé l'élément
        return i # on renvoie son indice

def duree_n(n): # n est la taille de la liste
    t = random.sample(range(1, 10**9), n) # on crée une liste de taille n
    x = t[random.randint(0, len(t)-1)] # on choisit un élément de la liste
    debut = time.time() # on note le temps au début de la recherche
    resultat = recherche(x, t) # on effectue la recherche
    fin = time.time() # on note le temps à la fin de la recherche
    duree = fin - debut # on calcule la durée de la recherche
    return duree # on renvoie la durée de la recherche

##n = 100000
##print(duree_n(n))

liste_n = [10**i for i in range(0, 8)] # on crée une liste de taille 8
liste_duree = [duree_n(liste_n[i]) for i in range(0, len(liste_n))] # on crée une liste de durée de recherche

pyplot.plot(liste_n, liste_duree) # on trace le graphe
pyplot.xlabel('n') # on nomme l'axe des abscisses
pyplot.ylabel('duree') # on nomme l'axe des ordonnées
pyplot.show() # on affiche le graphe