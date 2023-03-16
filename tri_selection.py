import time
import random
from matplotlib import pyplot as plt

def tri_selection(liste):
    start = time.time()
    for i in range(len(liste)):
        mini = i
        for j in range(i+1, len(liste)):
            if liste[mini] > liste[j]:
                mini = j
        liste[i], liste[mini] = liste[mini], liste[i]
    stop = time.time()
    print(liste)
    return stop-start

liste_n = [2**i for i in range(1, 15)]
liste_duree = [tri_selection([random.randint(0, 100000) for i in range(n)]) for n in liste_n]

plt.plot(liste_n, liste_duree)
plt.show()
