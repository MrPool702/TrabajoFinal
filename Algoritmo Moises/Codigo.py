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
  def __str__(self):
    return "("+ str(self.x)+" ; " + str(self.y) + ")"
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
    nodos = []
    puntosEntrega = []
    almacenes = []
    for l in lines:
      lista = l.strip().split(sep=",")
      aux = int(lista[0])
      aux2 = int(lista[1])
      aux3 = int(lista[3])
      elem = Point(aux,aux2,lista[2],aux3)
      if lista[2] == str(" punto"):
        puntosEntrega.append(elem)
      elif lista[2] == str(" almacen"):
        almacenes.append(elem)
      nodos.append(elem)
  return nodos, puntosEntrega, almacenes

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
  return parent

nodos, puntosEntrega, almacenes = readFile()

grafo = [0]*len(nodos)
for v  in range(len(grafo)):
  grafo[v] = []

for i in range(len(grafo)):
  for j in range(len(grafo)):
    if i != j:
      if nodos[j].getY() == nodos[i].getY() or nodos[j].getX() == nodos[i].getX():
        distancia = math.sqrt((nodos[j].getY()-nodos[i].getY())**2 + (nodos[j].getX()-nodos[i].getX())**2)
        if distancia <= 20:
          grafo[i].append((j,round(distancia)))

def RoadGraphWithBFS(graph,almacenes,puntosEntrega):
  with open("result.txt",mode="w") as file:
    for p in almacenes:
      path = BFS(graph,p.getID())
      file.write("Stock with node index equal to " + str(p.getID()) + "\n")
      for pd in puntosEntrega:
        file.write("Parent of the point with node index equal to " + str(pd.getID()) + " is: " + str(path[pd.getID()]) + "\n")

visited = [False]*len(grafo)


def leerDatos():
  with open("MoisesEntregas.txt") as file:
    lines = file.readlines()
    puntosEntrega = [[] for i in range(len(lines))]
    i = 0
    for a in lines:
      linea = a.strip().split(sep= ', ')
      j = 0
      for numero in linea:
        puntosEntrega[i].append(int(numero))
      i += 1
    return puntosEntrega 

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
    if not visitados[actual]: #and actual in restriccion:
      visitados[actual] = True
      for vecino, costo in grafo[actual]:
        total = costoA + costo
        if total < costos[vecino]:# and vecino in restriccion:
          costos[vecino] = total
          padres[vecino] = actual
          queue.append((total, vecino))
  return padres, costos

distribucion = leerDatos()
a = almacenes[14:28]

def AlgoritmoMoises(grafo, almacenes, puntosEntrega):
  cont = 0
  with open("puntosMoises.txt", mode= "w") as file:
    for i in almacenes:
      p, c = dijkstra(grafo, i.getID(), puntosEntrega[cont])
      file.write("Almacen " + str(i.getID()) + " Costos:\n")
      for j in puntosEntrega[cont]:
        file.write("Punto " + str(j) + " Costo: " + str(c[cont][j]))
    cont += 1

a, b = AlgoritmoMoises(grafo,a,distribucion)
