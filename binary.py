def bin(x):
    binary = ""
    binRes = 0
    while x!=0:
        binRes = x % 2
        x = x // 2
        binary = str(binRes) + binary
    return binary

print(bin(255))
