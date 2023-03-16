import time
import random
from matplotlib import pyplot as plt

def bubble_sort(liste):
    start = 0
    tri = True
    t1 =  time.time()
    while tri:
        tri = False
        for i in range(0, len(liste)-start-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                tri = True
        start += 1
    t2 = time.time()
    print(liste)
    return t2-t1

liste_n = [2**i for i in range(1, 15)]
liste_duree = [bubble_sort([random.randint(0, 100000) for i in range(n)]) for n in liste_n]

plt.plot(liste_n, liste_duree)
plt.show()
