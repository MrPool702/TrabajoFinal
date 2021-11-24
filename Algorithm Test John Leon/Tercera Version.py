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

Almacenes = readAlmacenes("Almacenes-John.txt")
Entregas = readPuntosEntrega("PuntosEntrega-John.txt")
nodo = readNodes("Puntos.csv")
g = createGrah(nodo)

def distance(a,b):
    return round(abs(((15*(nodo[a].getY()-nodo[b].getY()))**2 + (10*(nodo[a].getX()-nodo[b].getX()))**2)*0.5))

def compare(x,a,b):
    if distance(x,a)<=distance(x,b):
        return True
    else:
        return False

def toFinish(l,n):
    for x in l:
        if n == x[0]:
            return True
        else:
            continue
    return False

def VRP(start, end):
    way = list()
    way = [start]
    cost = 0
    nonway = list()
    while way[-1] != end:
        p = g[way[-1]]
        if toFinish(p,end):
            way.append(end)
        else:
            for _ in range(len(p)):
                minid = max(p,key=lambda x:x[1])[0]
                min = max(p,key=lambda x:x[1])[1]
                for x in p:
                    if x[1] <= min and x[0] not in way and x[0] not in nonway:
                        minid = x[0]
                        min = x[1]
                if compare(end,minid,way[-1]):
                    way.append(minid)
                    break
                for x in p:
                    if x[0] in nonway:
                        if len(way) > 2:
                            nonway.append(way[-1])
                            way.pop(-1)
                        else: 
                            return 0,str("No se ha podido pudo calcular una ruta optima")
                else:
                    nonway.append(minid)
    for i in range(len(way)-1):
        for j in g[way[i]]:
            if j[0] == way[i+1]:
                cost += j[1]
    return way, cost