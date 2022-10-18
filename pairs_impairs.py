def pair_impair(x:tuple):
    """tuple -> tuple(list, list)"""
    pair, impair = [], []
    pair = [e for e in x if e%2==0]
    impair = [e for e in x if e%2!=0]
    return (pair, impair)

t = (1, 2, 3, 4, 5, 6, 7)
print(pair_impair(t))

#créer une liste par compréhension revoie un "generator object" et non pas un tuple 
l = (i for i in range(101))
print(l)
print(pair_impair(l))