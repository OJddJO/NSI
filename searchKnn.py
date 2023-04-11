import time
import random
from matplotlib import pyplot as plt

def voisins(L, k, element):
    start = time.time()
    rList = []
    for j in range(k):
        dist = abs(element-L[0])
        n = L[0]
        tmpList = L[1:-1]
        for i in range(len(tmpList)-1):
            tmp = abs(element-tmpList[i])
            if tmp < dist :
                dist = tmp
                n = tmpList[i]
        rList.append(n)
        L.remove(n)
    stop = time.time()
    return (rList, stop-start)


liste_n = [10**i for i in range(1, 7)]
liste_duree = [voisins([random.randint(0, 100000) for i in range(n)], 3, 50000)[1] for n in liste_n]

plt.plot(liste_n, liste_duree)
plt.show()