import time
import random
from matplotlib import pyplot as plt

def bubble_sort(liste):
    start = 0
    tri = True
    t1 =  time.time()
    while tri:
        tri = False
        for i in range(len(liste)-start-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                tri = True
        start += 1
    t2 = time.time()
    print(liste)
    return t2-t1

def insertion_sort(liste):
    start = time.time()
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j-1]:
            liste[j], liste[j-1] = liste[j-1], liste[j]
            j -= 1
    stop = time.time()
    print(liste)
    return stop-start

def selection_sort(liste):
    start = time.time()
    for i in range(len(liste)):
        min = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min]:
                min = j
        liste[i], liste[min] = liste[min], liste[i]
    stop = time.time()
    print(liste)
    return stop-start

liste_n = [2**i for i in range(1, 15)]
liste_duree = [bubble_sort([random.randint(0, 10000000) for i in range(n)]) for n in liste_n]
plt.plot(liste_n, liste_duree)

liste_duree = [selection_sort([random.randint(0, 10000000) for i in range(n)]) for n in liste_n]
plt.plot(liste_n, liste_duree)

liste_duree = [insertion_sort([random.randint(0, 10000000) for i in range(n)]) for n in liste_n]
plt.plot(liste_n, liste_duree)

plt.show()
