def glouton(dist, dmax):
    n = len(dist)
    d = dmax
    stations = []
    i = 0
    while i != n:
        while i < n and dist[i] <= d:
            d -= dist[i]
            i += 1
        stations.append(i-1)
        d = dmax
    return stations, dmax

from random import randint

trajet = 2300
tab = [randint(25, 100)]
while sum(tab) < trajet:
    tab.append(randint(25, 100))
tab[-1] = trajet - sum(tab[:-1])
res = 600

data = glouton(tab, res)

print(f"Avec une autonomie de {res} km, vous devez vous arrêter aux stations {data[0]} pour recharger votre véhicule.")
print(f"Vous parcourirez {sum(tab)} km avec {len(data[0])} arrêts.")

distList = []
for i in data[0]:
    distList.append(sum(tab[:i+1]))

print(f"Vous vous arrêterez aux kilomètres {distList}.")