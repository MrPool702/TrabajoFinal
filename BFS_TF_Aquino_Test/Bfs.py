import numpy as np
import random as rand
import csv
import math
import heapq as hp

def BFS(G, S):
  parent = [None]*len(G)
  visited = [False]*len(G)
  visited[S] = True
  queue = [S]

  while len(queue) > 0:
    u = queue.pop(0)
    for v,c in graph[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)
  return parent;

class Punto:
  def __init__(self,x,y,Tipo,ide) -> None:
    self.x = x 
    self.y = y 
    self.Tipo = Tipo 
    self.id = ide
  def getID(self):
    return self.id
  def setID(self,ide):
    self.id = ide
  def out(self):
    return str(self.x) + ", " + str(self.y) + ", " + str(self.Tipo) + ", " + str(self.id) + "\n"
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def getTipo(self):
    return self.Tipo

def readFile():
  with open("nodes.txt") as file:
    lines = file.readlines()
    arreglo = []
    for l in lines:
      lista = l.strip().split(sep=",")
      aux = int(lista[0])
      aux2 = int(lista[1])
      aux3 = int(lista[3])
      elem = Punto(aux,aux2,lista[2],aux3)
      arreglo.append(elem)
  return arreglo

def EscribirPunto(arreglo):
  aux = []
  for i in arreglo:
    a = i.getTipo()
    if a == " punto":
      aux.append(i)
  return aux

nodes = readFile()
tamaño_node=len(nodes)
puntosEntrega = EscribirPunto(nodes)
graph = [0]*tamaño_node
n_graph=len(graph)
for v  in range(n_graph):
  graph[v] = []

for i in range(n_graph):
  for j in range(n_graph):
    if i != j:
      distancia = math.sqrt((nodes[j].getY()-nodes[i].getY())**2 + (nodes[j].getX()-nodes[i].getX())**2)
      if distancia <= 20:
        graph[i].append((j,round(distancia)))

points=[2256,2318,2459,2474,2569,2736,2742,2765,2854,2997,3022,3041,3160,3211]  

def Camino_Bfs(graph,points,puntosEntrega):
  with open("output.txt",mode="w") as file:
    for p in points:
      path = BFS(graph,p)
      file.write("Stock con indice al nodo  " + str(p) + "\n")
      for pd in puntosEntrega:
        file.write("Parent del nodo coincide con  " + str(pd.getID()) + " es: " + str(path[pd.getID()]) + "\n")

Camino_Bfs(graph,points,puntosEntrega)
