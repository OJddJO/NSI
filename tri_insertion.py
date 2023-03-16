import time
import random
from matplotlib import pyplot as plt

def tri_insertion(liste):
    start = time.time()
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j-1] > liste[j]:
            liste[j], liste[j-1] = liste[j-1], liste[j]
            j -= 1
    stop = time.time()
    print(liste)
    return stop - start

liste_n = [2**i for i in range(1, 15)]
liste_duree = [tri_insertion([random.randint(0, 100000) for i in range(n)]) for n in liste_n]

plt.plot(liste_n, liste_duree)
plt.show()