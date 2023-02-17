def dec(x):
    x = str(x)
    decimal = 0
    for i in range(len(x)):
        if int(x[i]) == 1:
            decimal += 2**(len(x)-i-1)
    return decimal

print(dec("11111111"))
