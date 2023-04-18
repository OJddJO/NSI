def glouton(p, r):
    n= len(p)
    i = n-1
    solution = n * [0]
    while r>0:
        while p[i]>r:
            i = i-1
        solution[i] += 1
        r -= p[i]
    return solution