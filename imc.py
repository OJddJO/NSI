def imc(masse:float, taille:float):
    """float * float -> float\n
    masse en kg, taille en m\n
    Retourne l'imc"""
    imc = masse/taille**2
    return imc

def imc_status(masse:float, taille:float):
    """float * float -> str\n
    masse en kg, taille en m\n
    Retourne votre status"""
    i = imc(masse, taille)
    if i < 18:
        return 'Vous êtes en sous poids'
    elif i < 24.9:
        return 'Vous êtes normal'
    elif i < 29.9:
        return 'Vous êtes en surpoids'
    elif i < 34.9:
        return 'Vous êtes obèse'
    elif i <= 35:
        return 'Vous êtes en obésité sévère'

print(imc_status(49, 1.74))
