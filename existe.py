def existe(x, l):
    if x in l:
        return True
    return False

def existe2(x, l):
    for element in l:
        if element == x:
            return True
    return False

def existe3(x, l):
    n = 0
    while n != len(l)-1:
        if l[n] == x:
            return True
        n += 1
    return False
