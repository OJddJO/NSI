def bissextile(n):
    return n%4==0 and (n//100)%4==0

print(bissextile(2000))