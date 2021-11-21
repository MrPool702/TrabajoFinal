import matplotlib.pyplot as plt
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
  with open("nodes.txt") as file:
    lines = file.readlines()
    arr = []
    for l in lines:
      lista = l.strip().split(sep=",")
      aux = int(lista[0])
      aux2 = int(lista[1])
      aux3 = int(lista[3])
      elem = Point(aux,aux2,lista[2],aux3)
      arr.append(elem)
  return arr
def writePoints(arr):
  aux = []
  for i in arr:
    a = i.getType()
    if a == " punto":
      aux.append(i)
  return aux

nodes = readFile()
puntosEntrega = writePoints(nodes)
graph = [0]*len(nodes)
for v  in range(len(graph)):
  graph[v] = []

for i in range(len(nodes)):
  for j in range(len(nodes)):
    if i != j:
      if nodes[j].getY() == nodes[i].getY() or nodes[j].getX() == nodes[i].getX():
        distancia = math.sqrt((nodes[j].getY()-nodes[i].getY())**2 + (nodes[j].getX()-nodes[i].getX())**2)
        if distancia <= 20:
          graph[i].append((j,round(distancia)))

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
  road = ""
  closedList.pop(0)
  for w,n in closedList:
    road += str(n) + "-->"
  road += "fin del camino"
  return road
def readDistributionPointsMiguel(G,nodes):
  almacenes = [162,178,570,575,680,748,767,805,840,999,1186,1197,1378,1395]
  with open("puntosMiguel.txt", mode="r") as file:
    for n in range(14):
        line = file.readline().strip().split(sep=",")
        for i in range(len(line)):
          line[i] = int(line[i].strip())
          print("\nEl camino de el nodo",almacenes[n],"hasta",line[i],"es\n")
          print(MiguelAlgorithm(G,almacenes[n],line[i],nodes))     
readDistributionPointsMiguel(graph,nodes)
