def chiffrement(message) :
    chiffre = ""
    for c in message:
        x = ord(c) + 3
        chiffre = chiffre + chr(x)
    return chiffre

print(chiffrement("bonjour"))

def epure(texte):
    texte = texte.upper()
    return texte.upper()

print(epure("bonjour"))

def dechiffrement_caesar(text:str, decalage:int):
    decode = ""
    for c in text:
        x = ord(c) - decalage
        decode = decode + chr(x)
    return decode

print(dechiffrement_caesar("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX", 3))

def casse_caesar(text):
    caractere = [chr(x) for x in range(65, 91)]
    text = epure(text)
    for i in range(26):
        for c in text:
            x = caractere.find(c) - i