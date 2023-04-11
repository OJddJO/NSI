import time
import random
from matplotlib import pyplot
from math import sqrt

def nextPoint(pList, k, point):
    start = time.time()
    rList = []
    for j in range(k):
        pos1 = pList[0]
        norm1 = sqrt((point-pos1)**2)
        dist = abs(element-L[0])
        n = L[0]
        tmpList = L[1:-1]
        for i in range(len(tmpList)-1):
            tmp = abs(element-tmpList[i])
            if tmp < dist :
                dist = tmp
                n = tmpList[i]
        rList.append(n)
        L.remove(n)
    stop = time.time()
    return stop-start
