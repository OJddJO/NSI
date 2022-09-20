from math import sqrt
def polynome(a:float, b:float, c:float):
    """Calcule le discriminant, puis les solutions d'une équation du second degré\n
    Retourne les solutions"""
    delta = b**2-4*a*c
    if delta < 0:
        return None, None
    elif delta == 0:
        x0 = -b/(2*a)
        return x0, None
    elif delta > 0:
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        return x1, x2

print("Ce code résout les équations du second degrés.")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
solutions =  polynome(a, b, c)

if solutions == [None, None]:
    print(f"L'équation {a}x^(2)+{b}x+{c} n'admet pas de solutions.")
elif solutions[1] == None:
    print(f"L'équation {a}x^(2)+{b}x+{c} admet une solutions. \nx0 = {solutions[0]}")
else:
    print(f"L'équation {a}x^(2)+{b}x+{c} admet deux solutions. \nx1 = {solutions[0]}; x2 = {solutions[1]}")

