def reste(a, b):
    while a >= b:
        a -= b
    return a

print(reste(16, 4))

def pgcd(a, b):
    r = reste(a, b)
    while r!=0:
        a = b, b = r
        r = reste(a, b)
    return b

print(pgcd(60, 30))
