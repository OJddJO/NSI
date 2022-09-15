def dec():
    x = str(input("Binary: "))
    decimal = 0
    for i in range(len(x)):
        if int(x[i]) == 1:
            decimal += 2**(len(x)-i-1)
    print(decimal)

dec()
