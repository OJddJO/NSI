def somme_list(l):
    somme = 0
    for element in l:
        somme += element
    return somme

def max_list(l):
    m = l[0]
    for element in l:
        if element > m:
            m = element
    return m
