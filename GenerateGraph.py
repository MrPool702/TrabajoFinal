class Point:
    def __init__(self,x,y,types,ide) -> None:
        self.x = x
        self.y = y
        self.type = types
        self.id = ide
    def getID(self):
        return self.id
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getType(self):
        return self.type

def readNodes(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines.pop(0)
        arr = []
        for l in lines:
            lista = l.strip().split(sep=",")
            arr.append(Point(int(lista[1]),int(lista[2]),lista[3],int(lista[0])))
    return arr

def readPuntosEntrega(filename):
    arr=[[]for _ in range(14)]
    e=[[]for _ in range(14)]
    with open(filename) as file:
        lines = file.readlines()
        ide=0
        for l in lines:
            lista = l.strip().split(",")
            arr[ide]=lista
            ide+=1
    ide=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            e[i].append(int(arr[i][j]))
    return e

def readAlmacenes(filename):
    arr=[]
    with open(filename) as file:
        lines = file.readlines()
        for l in lines:
            lista = l.strip().split(",")
            arr=lista
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    return arr

def createGrah(n):
    g=[[] for _ in range(len(n))]
    for i in range(len(n)):
        if  n[i].getID()-1 >= 0 and n[i].getID() % 1000!=0 and n[i-1].getType() != "CaminoObstruido":
            g[i].append(((n[i].getID()-1),10))
        if n[i].getID()+1 < len(n) and n[i].getID() % 1000 != 999 and n[i+1].getType() != "CaminoObstruido":
            g[i].append(((n[i].getID()+1),10))
        if n[i].getID()+1000<len(n) and n[i+1000].getType() != "CaminoObstruido":
            g[i].append(((n[i].getID()+1000),15))
        if n[i].getID()-1000 >= 0 and n[i-1000].getType() != "CaminoObstruido":
            g[i].append(((n[i].getID()-1000),15))
    return g


PuntosEntregasXintegrante()
AlmacenesXintegrante()

'''
    para obtener el grafo:
    nodos= readNodes("Puntos.csv")
    grafo=createGrah(nodos)
    
'''
