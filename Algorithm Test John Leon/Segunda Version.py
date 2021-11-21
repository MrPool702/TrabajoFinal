class Point:
    def __init__(self,x,y,types,ide) -> None:
        self.x = x
        self.y = y
        self.type = types
        self.id = ide
    def getID(self):
        return self.id
    def setID(self,ide):
        self.id = ide
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getType(self):
        return self.type

def readNodes():
    with open("nodes.csv") as file:
        lines = file.readlines()
        arr = []
        for l in lines:
            lista = l.strip().split(sep=",")
            arr.append(Point(int(lista[0]),int(lista[1]),lista[2],int(lista[3])))
    return arr

def readPuntosEntrega():
    arr=[[]for _ in range(14)]
    e=[[]for _ in range(14)]
    with open("John.txt") as file:
        lines = file.readlines()
        ide=0
        for l in lines:
            lista = (l.strip().split(" ,"))
            arr[ide]=lista
            ide+=1
    ide=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            e[i].append(int(arr[i][j]))
    return e

def createGrah(n):
    g=[[] for _ in range(len(n))]
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                if n[j].getY() == n[i].getY() or n[j].getX() == n[i].getX():
                    distancia = ((n[j].getY()-n[i].getY())**2 + (n[j].getX()-n[i].getX())**2)**(1/2)
                    if distancia <= 20:
                        g[i].append((j,round(distancia)))
    return g

Entregas=readPuntosEntrega()
Almacenes=[2256,2318,2459,2474,2569,2736,2742,2765,2854,2997,3022,3041,3160,3211]
nodos = readNodes()
grafo = createGrah(nodos)

def distance(a,b):
    return abs(((nodos[a].getY()-nodos[b].getY())**2 + (nodos[a].getX()-nodos[b].getX())**2)*0.5)

def IsNear(a,b):
    if distance(a,b) <= 20 and nodos[a].getY() == nodos[b].getY() or nodos[a].getX() == nodos[b].getX():
        return True
    else:
        return False

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

def VRP_John(start, end):
    way = list().clear()
    way = [start]
    cost = 0
    nonway = list()
    while way[-1] != end:
        p = grafo[way[-1]]
        if toFinish(p,end):
            way.append(end)
        else:
            for _ in range(len(p)):
                minid = max(p,key=lambda x:x[1])[0]
                min = max(p,key=lambda x:x[1])[1]
                if way == []:
                    return 0,str("No se pudo calcular una ruta optima")
                for x in p:
                    if x[1] <= min and x[0] not in way and x[0] not in nonway:
                        minid = x[0]
                        min = x[1]
                if compare(end,minid,way[-1]):
                    way.append(minid)
                    break
                for x in p:
                    if x[0] in nonway:
                        if way != []:
                            nonway.append(way[-1])
                            way.pop(-1)
                        else: 
                            return 0,str("No se pudo calcular una ruta optima")
                else:
                    nonway.append(minid)
                    continue
    for i in range(len(way)-1):
        for j in grafo[way[i]]:
            if j[0] == way[i+1]:
                cost += j[1]
    
    return way, cost

with open("salida.txt", "w") as f:
    for inicio in Almacenes:
        for _f in Entregas:
            for final in _f:
                way, cost = VRP_John(inicio, final)
                if type(way) == 0:
                    f.write(str(cost) + "\n")
                else:
                    f.write(str("Ruta: " + str(way) + "\n Costo: "+ str(cost)+ "\n"))
    