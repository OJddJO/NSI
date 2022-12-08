def horner(x:str, B:int, symbole:tuple=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")):
    xList = []
    for e in x:
        xList.append(e)
    P = 0
    for i in range(len(xList)):
        P = P * symbole.index(xList[i])
    return P

print(horner("110", 2))