def somme(n):
    x = 0
    for i in range(1, n+1):
        x += i
    return x

print(somme(1000000))