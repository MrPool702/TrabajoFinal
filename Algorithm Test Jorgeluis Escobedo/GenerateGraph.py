import math
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

def PuntosEntregasXintegrante():
    with open("PuntoEntrega.csv", "r") as f:
        lines = f.readlines()
        lines.pop(0)
        PuntosEntrega = []
        i = 0
        for line in lines:
            PuntosEntrega.append(int(line.split(",")[0]))
    with open("PuntosEntrega-John.txt", "w") as f:
        for i in range(0,700):
            if i%50==0 and i!=0:
                f.write("\n")
            f.write(str(PuntosEntrega[i]) + ",")
    with open("PuntosEntrega-Miguel.txt", "w") as f:
        for i in range(700,1400):
            if i%50==0 and i!=700:
                f.write("\n")
            f.write(str(PuntosEntrega[i]) + ",")
    with open("PuntosEntrega-Moises.txt", "w") as f:
        for i in range(1400,2100):
            if i%50==0 and i!=1400:
                f.write("\n")
            f.write(str(PuntosEntrega[i]) + ",")
    with open("PuntosEntrega-Jorgeluis.txt", "w") as f:
        for i in range(2100,2800):
            if i%50==0 and i!=2100:
                f.write("\n")
            f.write(str(PuntosEntrega[i]) + ",")
    with open("PuntosEntrega-Fernando.txt", "w") as f:
        for i in range(2800,3500):
            if i%50==0 and i!=2800:
                f.write("\n")
            f.write(str(PuntosEntrega[i]) + ",")

def AlmacenesXintegrante():
    with open("Almacenes.csv", "r") as f:
        lines = f.readlines()
        lines.pop(0)
        Almacenes = []
        for line in lines:
            Almacenes.append(int(line.split(",")[0]))
    Almacenes.sort()
    with open("Almacenes-John.txt", "w") as f:
        for i in range(0,14):
            f.write(str(Almacenes[i]) + ",")
    with open("Almacenes-Miguel.txt", "w") as f:
        for i in range(14,28):
            f.write(str(Almacenes[i]) + ",")
    with open("Almacenes-Moises.txt", "w") as f:
        for i in range(28,42):
            f.write(str(Almacenes[i]) + ",")
    with open("Almacenes-Jorgeluis.txt", "w") as f:
        for i in range(42,56):
            f.write(str(Almacenes[i]) + ",")
    with open("Almacenes-Fernando.txt", "w") as f:
        for i in range(56,70):
            f.write(str(Almacenes[i]) + ",")

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

def dijkstra(grafo, inicio, restriccion):
  nodos = len(grafo)
  visitados = [False]*nodos
  padres = [None]*nodos
  costos = [math.inf]*nodos
  costos[inicio] = 0
  restriccion.append(inicio)
  queue = [(0,inicio)]
  while queue:
    costoA, actual = queue.pop(0)
    if not visitados[actual]:
      visitados[actual] = True
      for vecino, costo in grafo[actual]:
        total = costoA + costo
        if total < costos[vecino]:
          costos[vecino] = total
          padres[vecino] = actual
          queue.append((total, vecino))
  return padres, costos

def AlgoritmoJorgeluis(grafo, almacenes, puntosEntrega):
  cont = 0
  with open("puntosJorgeluisVersionFinal.txt", mode= "w") as file:
    for i in almacenes:
      _, distancia = dijkstra(grafo, i, puntosEntrega[cont])
      file.write("Almacen " + str(i) + " :\n")
      for j in puntosEntrega[cont]:
        file.write("Punto de Entrega " + str(j) + " Distancia: " + str(distancia[j]) + "\n")
      cont += 1

#PuntosEntregasXintegrante()
#AlmacenesXintegrante()
nodos= readNodes("Puntos.csv")
grafo=createGrah(nodos)
puntosEntrega = readPuntosEntrega("PuntosEntrega-Jorgeluis.txt")
almacenes = readAlmacenes("Almacenes-Jorgeluis.txt")

AlgoritmoJorgeluis(grafo, almacenes, puntosEntrega)
'''
    para obtener el grafo:
    nodos= readNodes("Puntos.csv")
    grafo=createGrah(nodos)
    
'''