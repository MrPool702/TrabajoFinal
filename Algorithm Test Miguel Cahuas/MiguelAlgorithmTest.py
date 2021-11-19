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

def BFS(graph, start):
  parent = [None]*len(graph)
  visited = [False]*len(graph)
  visited[start] = True
  queue = [start]

  while len(queue) > 0:
    u = queue.pop(0)
    for v,c in graph[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)
  return parent;

def RoadGraphWithBFS(graph,points,puntosEntrega):
  with open("result.txt",mode="w") as file:
    for p in points:
      path = BFS(graph,p)
      file.write("Stock with node index equal to " + str(p) + "\n")
      for pd in puntosEntrega:
        file.write("Parent of the point with node index equal to " + str(pd.getID()) + " is: " + str(path[pd.getID()]) + "\n")

def algoritmoMiguel(G,nodes,start,end):
    n = len(G)
    distDefault = math.sqrt((nodes[end].getX()-nodes[start].getX())**2+(nodes[end].getY()-nodes[start].getY())**2)
    visited = [False]*n
    path = [None]*n
    cost = [-1]*n
    cost[start] = 0
    stack = [start]
    while stack:
        v = stack.pop()
        if v == end:
            break
        if visited[v] == False:
            visited[v] = True
            mini = distDefault
            nearest = 0
            weight = 0
            for u, w in G[v]:
                distance = math.sqrt((nodes[end].getX()-nodes[u].getX())**2+(nodes[end].getY()-nodes[u].getY())**2)
                if visited[u] == False:
                    if distance < mini:
                        mini = distance
                        nearest = u
                        weight = w
                    if distance == mini:
                        if w  < weight:
                            nearest = u
                            weight = w
            path[nearest] = v
            cost[nearest] = weight + cost[v]
            stack.append(nearest)
    return path, cost

def roadPath(path,start,end):
  p = []
  def _road(index):
    if path[index] == None:
      return
    p.append(index)
    _road(path[index])
  _road(end)
  p.append(start)
  return list(reversed(p))

def readDistributionPointsMiguel(G,nodes):
  almacenes = [162,178,570,575,680,748,767,805,840,999,1186,1197,1378,1395]
  with open("puntosMiguel.txt", mode="r") as file:
    for n in range(14):
        line = file.readline().strip().split(sep=",")
        for i in range(len(line)):
            line[i] = int(line[i].strip())
            path, _ = algoritmoMiguel(G,nodes,almacenes[n],line[i])
            print(roadPath(path,almacenes[n],line[i]))  
readDistributionPointsMiguel(graph,nodes)
