def chiffrement(message):
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

print(dechiffrement_caesar("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX", 2))

def casse_caesar(text):
    caractere = [chr(x) for x in range(65, 91)]
    text = epure(text)
    for i in range(26):
        decode = ""
        for c in text:
            x = caractere.index(c) - i
            decode = decode + caractere[x]
        print(decode)

print(casse_caesar("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX"))

def substitution(text:str, alphabet:str):
    new_alphabet = [c for c in alphabet]
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = [c for c in alpha]
    text = text.upper()
    encode = ""
    for c in text:
        i = new_alphabet.index(c)
        encode = encode + alpha[i]
    return encode

print(substitution("FGFDQOLSTHKGYRTHIBLOJWTQWLLOOSTLMLBDHQXWJWTETLMSTDTDT", "QZERTYUIOPASDFGHJKLMWXCVBN"))

def stat(txt: str):
    txt = txt.upper()
    dictionnary = {}
    for character in txt:
        if character.isupper():
            try:
                dictionnary[character] = dictionnary[character] + 1
            except:
                dictionnary[character] = 1
    return dictionnary

fichier = open("Document.txt", "r").read()
print(stat(fichier))

def decalage(text):
    caractere = [chr(x) for x in range(65, 91)]
    text = epure(text)
    listOfDecodedText = []
    for i in range(26):
        decode = ""
        for c in text:
            x = caractere.index(c) - i
            decode = decode + caractere[x]
        listOfDecodedText.append(decode)
    stats = []
    for text in listOfDecodedText:
        stats.append(stat(text))
    nbOfE = 0
    mostProbable = None
    for statistic in stats:
        try:
            if nbOfE < statistic['E']:
                mostProbable = statistic
                nbOfE = statistic['E']
        except Exception as e:
            print(e)
    index = stats.index(mostProbable)
    return listOfDecodedText[index]

print(decalage("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX"))