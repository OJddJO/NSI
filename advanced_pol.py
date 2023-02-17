def f(x):
    return x**2-2

def dichotomie(A:float, B:float, epsilon:float, f):
    if f(A)*f(B) >= 0:
        return ("f(A)f(B) < 0 is not verified")
    while B-A >= epsilon:
        C = (A+B)/2
        if f(A)*f(C) < 0:
            B = C
        else:
            A = C
    return C

print(dichotomie(-1, 10, 0.000001, f))