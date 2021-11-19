import random
import matplotlib.pyplot as plt
import gc
import csv

class Node:
    def __init__(self,value,nxt=None,back=None) -> None:
        self.value = value
        self.next = nxt
        self.back = back
    def setNext(self,nxt):
        self.next = nxt
    def setBack(self,back):
        self.back = back
    def getNext(self):
        return self.next
    def getBack(self):
        return self.back
    def getValue(self):
        return self.value
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.end = None
        self.size = 0
        self.aux = None
    def pushBack(self,value):
        newNode = Node(value)
        if self.size == 0:
            self.head = newNode
            self.end = newNode
            self.size += 1
        else:
            self.end.setNext(newNode)
            newNode.setBack(self.end)
            self.end = newNode
            self.size += 1
    def printList(self):
        self.aux = self.head
        while self.aux != None:
            print(self.aux.getValue())
            self.aux = self.aux.getNext()
        print("nullptr")
    def popBack(self):
        if self.size  == 0:
            return
        elif self.size == 1:
            del self.head
            gc.collect()
            self.head = None
            self.end = None
            self.size -= 1
        else:
            self.end = self.end.getBack()
            value = self.end.getNext()
            del value
            gc.collect()
            self.end.setNext(None)
            self.size -= 1
    def getSize(self):
        return self.size
    def top(self):
        return self.end.getValue()

n = 800
arr = [[7]*n for i in range(n)]

def drawMaze(maze):
  _, ax = plt.subplots(figsize=(18, 18))
  ax.imshow(maze)
  ax.axis("off")

def partitionTree(arr, rowI , rowF, colI, colF):
    dif1 = colF - colI
    dif2 = rowF - rowI
    for a in range(colI,colF):
        arr[rowI][a] = 1
        arr[rowF][a] = 1
        for j in range(1,6):
            arr[rowI+j][a] = 1
            arr[rowF-j][a] = 1
    for b in range(rowI,rowF):
        arr[b][colI] = 1
        arr[b][colF] = 1
        for j in range(1,6):
            arr[b][colI+j] = 1
            arr[b][colF-j] = 1
    if dif1 >= random.randint(50,120):
        mid = (colI + colF)//2
        partitionTree(arr,rowI,rowF,colI,mid)
        partitionTree(arr,rowI,rowF,mid+1,colF)
    elif dif2 >= random.randint(50,120):
        mid = (rowI + rowF)//2
        partitionTree(arr,rowI,mid,colI,colF)
        partitionTree(arr,mid+1,rowF,colI,colF)
    else:
        return
def partitionTree2(arr,rowI,rowF,colI,colF,corners):
    callStack = [(rowI,rowF,colI,colF)]
    while callStack:
        ri, rf, ci, cf = callStack.pop()
        dif1 = cf - ci
        dif2 = rf -  ri
        for a in range(ci,cf):
            arr[ri][a] = 1
            arr[rf][a] = 1
        for b in range(ri,rf):
            arr[b][ci] = 1
            arr[b][cf] = 1
        if dif1 >= random.randint(20,30):
            mid = (ci + cf)//2
            arr[ri][mid] = 0
            arr[rf][mid] = 0
            corners.append((ri,mid))
            corners.append((rf,mid))
            callStack.append((ri,rf,ci,mid))
            callStack.append((ri,rf,mid+1,cf))
        elif dif2 >= random.randint(20,30):
            mid = (ri + rf)//2
            arr[mid][ci] = 0
            arr[mid][cf] = 0
            corners.append((mid,ci))
            corners.append((mid,cf))
            callStack.append((ri,mid,ci,cf))
            callStack.append((mid+1,rf,ci,cf))

corners = []
partitionTree2(arr,0,799,0,799,corners)
drawMaze(arr)
alm = LinkedList()
pts = LinkedList()
for i in range(0,140):
    if i % 2 == 0:
        alm.pushBack(corners[i])
    else:
        pts.pushBack(corners[i])
for j in range(141,3071):
    pts.pushBack(corners[j])

print(len(corners),alm.getSize(),pts.getSize())

with open('almacenes.csv',mode='w') as almacenesFile:
    almacenesWriter = csv.writer(almacenesFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    almacenesWriter.writerow(["#Almacenes","X","Y"])
    cont = 0
    while alm.getSize() > 0:
        y,x = alm.top()
        almacenesWriter.writerow([str(cont),str(x),str(y)])
        alm.popBack()
        cont += 1
with open('puntos.csv',mode='w') as puntosFile:
    puntosWriter = csv.writer(puntosFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    puntosWriter.writerow(["#Puntos","X","Y"])
    cont = 0
    while pts.getSize() > 0:
        y,x = pts.top()
        puntosWriter.writerow([str(cont),str(x),str(y)])
        pts.popBack()
        cont += 1
with open('otherNodes.csv',mode='w') as otherFile:
    otherWriter = csv.writer(otherFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    otherWriter.writerow(["#Node","X","Y"])
    cont = 0
    for i in range(3071,len(corners)):
        y,x = corners[i]
        otherWriter.writerow([str(cont),str(x),str(y)])
        cont += 1
        
