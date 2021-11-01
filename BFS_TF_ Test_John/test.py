import ClassAndFuncions
import math
nodes = readFile()
puntosEntrega = writePoints(nodes)
graph = [0]*len(nodes)
for v  in range(len(graph)):
  graph[v] = []

for i in range(len(nodes)):
  for j in range(len(nodes)):
    if i != j:
      distancia = math.sqrt((nodes[j].getY()-nodes[i].getY())**2 + (nodes[j].getX()-nodes[i].getX())**2)
      if distancia <= 20:
        graph[i].append((j,round(distancia)))#limitando puntos a utilizar
#segundo conjunto de almacenes (15 to 28)
almacenes = [1404,1500,1629,1751,1862,1874,1928,1960,2071,2152,2155,2160,2188,2207]

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

def RoadGraphWithBFS(graph,almacenes,puntosEntrega):
  with open("result.txt",mode="w") as file:
    for p in almacenes:
      path = BFS(graph,p)
      file.write("Stock with node index equal to " + str(p) + "\n")
      for pd in puntosEntrega:
        file.write("Parent of the point with node index equal to " + str(pd.getID()) + " is: " + str(path[pd.getID()]) + "\n")

RoadGraphWithBFS(graph,almacenes,puntosEntrega)