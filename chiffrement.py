def chiffrement(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = [c for c in alpha]
    message = message.upper()
    chiffre = ""
    for c in message:
        if c in alpha:
            x = alpha.index(c) - 3
            chiffre = chiffre + alpha[x]
    return chiffre

print(chiffrement("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel condimentum nisl. Suspendisse potenti. Nunc maximus sapien sit amet quam tristique, quis interdum nulla dictum. Pellentesque tincidunt eu nulla ullamcorper congue. Sed tincidunt lectus non turpis vehicula posuere. Nunc vel purus diam. Nulla eu neque nec est fringilla scelerisque porta eget nisl. Nullam dui neque, interdum at nisl hendrerit, bibendum aliquam ante. Nunc luctus, velit eu dictum porta, nisl erat auctor lectus, ac rutrum ipsum erat non metus. Pellentesque id imperdiet arcu. Morbi metus dolor, interdum vitae neque vel, pretium aliquet ligula. Etiam eget odio eget dui egestas tristique et sit amet nunc. Duis placerat ligula lacus, sit amet efficitur urna eleifend a. Vestibulum aliquam ac turpis quis rhoncus. Cras eu euismod eros, ut dictum ipsum. Curabitur diam erat, aliquet nec nulla vel, tempor ultrices turpis."))
print("\n")
print(chiffrement("Expériences sur les poids ; de plus le soir, au journal. Mille instructions n'auraient pu loger tout ce monde m'étourdit. Refuserez-vous de donner aux juges des explications qui les toucheraient ; et le vent d'hiver qui se mêlait à toutes ses idées dansaient dans sa tête ; nous en resterons là. Asseyez-vous là et écrivez à l'archevêque la quitta sur quelques méchantes paroles, mais il fallait danser. Vieux quartiers qu'il parcourut du faisceau lumineux venu de son chef. Politiquement parlant, leur présence est ici fort digne d'envie. Donnez-moi, je vous dis que je ne l'essaierai pas. Permettez que je prenne intérêt tant que durera votre absence ?"))
print("\n")

def epure(texte):
    texte = texte.upper()
    return texte.upper()

print(epure("bonjour\n"))

def dechiffrement_caesar(text:str, decalage:int):
    decode = ""
    for c in text:
        x = ord(c) - decalage
        decode = decode + chr(x)
    return decode

print(dechiffrement_caesar("erqmrxu", 3), "\n")

def casse_caesar(text):
    caractere = [chr(x) for x in range(65, 91)]
    text = epure(text)
    for i in range(26):
        decode = ""
        for c in text:
            x = caractere.index(c) - i
            decode = decode + caractere[x]
        print(decode)

casse_caesar("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX")
print("\n")

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

print(substitution("FGFDQOLSTHKGYRTHIBLOJWTQWLLOOSTLMLBDHQXWJWTETLMSTDTDT", "QZERTYUIOPASDFGHJKLMWXCVBN"), "\n")

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
print(stat(fichier), "\n")

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
            pass
    index = stats.index(mostProbable)
    return listOfDecodedText[index]

print(decalage("OHNLTOXSEXIKHYWBGYHKFTMBJNXEXIENLVETLLXWNFHGWX"))
print(decalage("PXIRQGBJXMMBIIBGBOBJV"))
print(decalage("ILOBJFMPRJALILOPFQXJBQZLKPBZQBQROXAFMFPZFKDBIFQCRPZBSBIZLKAFJBKQRJKFPIPRPMBKAFPPBMLQBKQFKRKZJXUFJRPPXMFBKPFQXJBQNRXJQOFPQFNRBNRFPFKQBOARJKRIIXAFZQRJMBIIBKQBPNRBQFKZFARKQBRKRIIXRIIXJZLOMBOZLKDRBPBAQFKZFARKQIBZQRPKLKQROMFPSBEFZRIXMLPRBOBKRKZSBIMRORPAFXJKRIIXBRKBNRBKBZBPQCOFKDFIIXPZBIBOFPNRBMLOQXBDBQKFPIKRIIXJARFKBNRBFKQBOARJXQKFPIEBKAOBOFQYFYBKARJXIFNRXJXKQBKRKZIRZQRPSBIFQBRAFZQRJMLOQXKFPIBOXQXRZQLOIBZQRPXZORQORJFMPRJBOXQKLKJBQRPMBIIBKQBPNRBFAFJMBOAFBQXOZRJLOYFJBQRPALILOFKQBOARJSFQXBKBNRBSBIMOBQFRJXIFNRBQIFDRIXBQFXJBDBQLAFLBDBQARFBDBPQXPQOFPQFNRBBQPFQXJBQKRKZARFPMIXZBOXQIFDRIXIXZRPPFQXJBQBCCFZFQROROKXBIBFCBKAXSBPQFYRIRJXIFNRXJXZQROMFPNRFPOELKZRPZOXPBRBRFPJLABOLPRQAFZQRJFMPRJZROXYFQROAFXJBOXQXIFNRBQKBZKRIIXSBIQBJMLORIQOFZBPQROMFP"))
print(decalage("BUMOFBKZBPPROIBPMLFAPABMIRPIBPLFOXRGLROKXIJFIIBFKPQORZQFLKPKXROXFBKQMRILDBOQLRQZBJLKABJQLROAFQOBCRPBOBWSLRPABALKKBOXRUGRDBPABPBUMIFZXQFLKPNRFIBPQLRZEBOXFBKQBQIBSBKQAEFSBONRFPBJIXFQQLRQBPPBPFABPAXKPXFBKQAXKPPXQQBKLRPBKOBPQBOLKPIXPPBVBWSLRPIBQZOFSBWIXOZEBSNRBIXNRFQQXPRONRBINRBPJZEXKQBPMXOLIBPJXFPFICXIIXFQAXKPBOSFBRUNRXOQFBOPNRFIMXOZLRORQARCXFPZBXRIRJFKBRUSBKRABPLKZEBCMLIFQFNRBJBKQMXOIXKQIBROMOPBKZBBPQFZFCLOQAFDKBABKSFBALKKBWJLFGBSLRPAFPNRBGBKBIBPPXFBOXFMXPMBOJBQQBWNRBGBMOBKKBFKQOQQXKQNRBAROBOXSLQOBXYPBKZB"))
