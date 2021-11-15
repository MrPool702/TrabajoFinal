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

def Dijkstra(graph,start):
    n = len(graph)
    visited = [False]*n
    cost = [math.inf]*n
    path = [None]*n
    cost[start] = 0
    heap = [(start, 0)]
    while len(heap) > 0:
        u, g = hp.heappop(heap)
        if visited[u] == False:
            visited[u] = True
            for v, c in graph[u]:
                nc = g + c
                if nc < cost[v]:
                    cost[v] = nc
                    path[v] = u
                    hp.heappush(heap,(v,nc))
    return path, cost

def RoadGraphWithDijkstra(graph,points,puntosEntrega):
  with open("result.txt",mode="w") as file:
    for p in points:
      path, _ = Dijkstra(graph,p)
      file.write("Stock with node index equal to " + str(p) + "\n")
      for pd in puntosEntrega:
        file.write("Parent of the point with node index equal to " + str(pd.getID()) + " is: " + str(path[pd.getID()]) + "\n")

points = [162,178,570,575,680,748,767,805,840,999,1186,1197,1378,1395]
RoadGraphWithDijkstra(graph,points,puntosEntrega)