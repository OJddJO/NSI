from matplotlib import pyplot
from searchKnn import voisins

x = [1, 3, 5, 9, 10, 13, 13, 12, 17, 10]
y = [3, 5, 3, 2, 5, 2, 5, 11, 5, 2]

def gluttony(x, y):
    for i in range(len(x)):
        

pyplot.scatter(x, y)
pyplot.show()