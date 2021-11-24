import random
points = []
id = 0
for i in range(1000):
    for j in range(1000):
        points.append((id,i, j))
        id+=1

random.shuffle(points)
Al=70
PE=3000

ListAl=[]
ListPE=[]
for i in points[:Al]:
    ListAl.append(i[0])
for i in points[Al:PE+Al]:
    ListPE.append(i[0])

with open("Almacenes.csv", "w") as f:
    f.write("id,x,y\n")
    for i in points[:Al]:
        f.write( str(i[0]) + ","+ str(i[1]) + "," + str(i[2]) + "\n") 
with open("PuntoEntrega.csv", "w")  as f:
    f.write("id,x,y\n")
    for i in points[Al:PE+Al]:
        f.write(str(i[0]) + ","+ str(i[1]) + "," + str(i[2])  + "\n")

points.sort()
with open("Puntos.csv", 'w') as f:
    f.write("id,x,y,tipo\n")
    for i in points:
        if i[0] in ListAl:
            f.write(str(i[0]) + ","+ str(i[1]) + "," + str(i[2]) +",Almacen"+ "\n")
        elif i[0] in ListPE:
            f.write(str(i[0]) + ","+ str(i[1]) + "," + str(i[2]) +",PuntoEntrega"+ "\n")
        else:
            if random.randint(1,100) == 1:
                f.write(str(i[0]) + ","+ str(-1) + "," + str(-1) +",CaminoObstruido"+ "\n")
            else:
                f.write(str(i[0]) + ","+ str(i[1]) + "," + str(i[2]) +",CaminoTransitable"+ "\n")