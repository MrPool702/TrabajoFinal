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
    def out(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.type) + ", " + str(self.id) + "\n"
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getType(self):
        return self.type

def readFile():
    with open("nodes.csv") as file:
        lines = file.readlines()
        arr = []
        for l in lines:
            lista = l.strip().split(sep=",")
            arr.append(Point(int(lista[0]),int(lista[1]),lista[2],int(lista[3])))
    return arr

def readPuntosEntrega():
    Entregas=[[]]*14
    with open("John.txt") as file:
            lines = file.readlines()
            for l in lines:
                lista = l.strip().split(sep=", ")
    id=0
    for i in lista:
        if len(Entregas[id])%14==0:
            id+=1
        Entregas[id].append(int(i))
    return Entregas

Entregas=readPuntosEntrega()
Almacenes=[2256,2318,2459,2474,2569,2736,2742,2765,2854,2997,3022,3041,3160,3211]
nodos = readFile()
Grafo=[0]*len(nodos)
for v in range(len(nodos)):
    Grafo[v]=[]

for i in range(len(nodos)):
    for j in range(len(nodos)):
        if i != j:
            if nodos[j].getY() == nodos[i].getY() or nodos[j].getX() == nodos[i].getX():
                distancia = ((nodos[j].getY()-nodos[i].getY())**2 + (nodos[j].getX()-nodos[i].getX())**2)*0.5
                if distancia <= 20:
                    Grafo[i].append((j,round(distancia)))    

def IsNear(a,b):
    euclid=(((nodos[a].getY()-nodos[b].getY())**2 + (nodos[a].getX()-nodos[b].getX())**2)*0.5)
    if euclid<=20:
        return True
    else:
        return False
def compare(x,a,b):
    e1=(((nodos[a].getY()-nodos[x].getY())**2 + (nodos[a].getX()-nodos[x].getX())**2)*0.5)
    e2=(((nodos[b].getY()-nodos[x].getY())**2 + (nodos[b].getX()-nodos[x].getX())**2)*0.5)
    if e1<e2:
        return a
    else:
        return b
def VRP(nodes, start, end, costPer):
    n=len(nodes)
    interation=0
    comparable=[]
    way=[start]
    if start==end:
        return way,interation*costPer
    if IsNear(start,end):
        interation+=1
        return way,interation*costPer
    while way[-1]!=end:
        for i in range(len(nodos)):
            if i!=start and i!=end:
                if IsNear(way[-1],i):
                    comparable.append(i)
                    if len(comparable)==2:
                        if compare(way[-1],comparable[0],comparable[1])==comparable[0]:
                            comparable.pop(1)
                        else:
                            comparable.pop(0)
                        way.append(comparable[0])
                        interation+=1
    return way, interation*costPer

