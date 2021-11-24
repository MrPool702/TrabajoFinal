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
