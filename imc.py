def imc(masse:float, taille:float):
    """float * float -> float\n
    masse en kg, taille en m\n
    Retourne l'imc"""
    imc = masse/taille**2
    print(f"IMC = {imc}")

imc(49, 1.74)
