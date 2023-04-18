from operator import itemgetter
tabIntervalles = [[0, 7, "1"], [4, 5, "2"], [6, 8, "3"], [1, 2, "4"], [5, 6, "5"], [0, 2, "6"], [4, 7, "7"], [0, 1, "8"], [3, 6, "9"], [1, 3, "10"], [2, 5, "11"], [6, 8, "12"], [0, 2, "13"], [5, 7, "14"], [1, 4, "15"]]


def sort(liste):
    return sorted(liste, key=itemgetter(1, 0))

def ordonnancement(liste):
    liste = sort(liste)
    returnedList = [liste[0]]
    for i in range(1, len(liste)):
        if liste[i][0] >= returnedList[-1][1]:
            returnedList.append(liste[i])
    return returnedList

print(ordonnancement(tabIntervalles))
