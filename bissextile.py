def bissextile1(n):
    return n%4==0 and (n//100)%4==0

print(bissextile1(2000))