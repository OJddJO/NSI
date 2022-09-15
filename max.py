def max2(a, b):
    if a > b:
        return a
    elif a < b:
        return b

def max3(a, b, c):
    if max2(a, b)==a and max2(a, c)==a:
        return a
    elif max2(b, c)==b and max2(b, a)==b:
        return b
    elif max2(c, a)==c and max2(c, b)==c:
        return c

print(max3(4, 7, 1))