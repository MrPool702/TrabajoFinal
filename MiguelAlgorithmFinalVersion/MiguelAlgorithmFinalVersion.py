import numpy as np
import random as rand
import csv
import math
import heapq as hp

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



def MiguelAlgorithm(graph,start,end,nodes):
  #Función Heurística
  def getDistance(point):
    return math.sqrt((nodes[end].getX()-nodes[point].getX())**2 + (nodes[end].getY()-nodes[point].getY())**2)
  n = len(graph)
  visited = [False]*n
  cost = [float("inf")]*n
  cost[start] = 0
  openList = [(0,start)]
  closedList = [(0,start)]
  while openList:
    w, u = hp.heappop(openList)
    if not visited[u]:
      visited[u] = True
      closedList.append((w,u))
      if u == end:
        break
      for v, c in graph[u]:
        distance = getDistance(v)
        newCost = cost[u] + c
        if newCost < cost[v]:
          cost[v] = newCost
          nc = newCost + distance
          hp.heappush(openList,(nc,v))
  closedList.pop(0)
  return cost[end]


def readDistributionPointsMiguel(G,nodes,almacenes):
  with open("puntosMiguel.txt", mode="r") as file:
    for n in range(14):
        line = file.readline().strip().split(sep=",")
        for i in range(len(line)):
          line[i] = int(line[i].strip())
          print("\nDe",almacenes[n],"hasta",line[i],"\n")
          costo = MiguelAlgorithm(G,almacenes[n],line[i],nodes)
          print("El minimo costo es",costo)
          galones = round(costo*0.010,2)
          print("Se requieren ",galones,"galones de Gasohol 90")
          print("El envió le costará a la empresa",round(galones*15,2),"soles\n")

def main():
  nodos= readNodes("Puntos.csv")
  grafo=createGrah(nodos)
  almacenes = readAlmacenes("AlmacenesMiguel.txt")
  readDistributionPointsMiguel(grafo,nodos,almacenes)
  # Demora aproximadamente 22 minutos en terminar de ejecutarse
  # Cada Vehículo soporta 40 galones
  # Se pierden 0.010 galones por unidad de espacio, sea m o km
  # Cada Galón (Gasohol 90)  cuesta 15 soles
if __name__ == "__main__":
  main()
