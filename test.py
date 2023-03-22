liste = [3, 5, 2, 6, 2, 6]
def tri_insertion(liste):
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j-1] > liste[j]:
            liste[j], liste[j-1] = liste[j-1], liste[j]
            j -= 1
            
tri_insertion(liste)
print(liste)