import numpy as np
import random as rand
import csv
import math
import heapq as hp
import graphviz as gv

def adjlShow(L, labels=None, directed=False, weighted=False, path=[],
             layout="sfdp"):
  g = gv.Digraph("G") if directed else gv.Graph("G")
  g.graph_attr["layout"] = layout
  g.edge_attr["color"] = "gray"
  g.node_attr["color"] = "orangered"
  g.node_attr["width"] = "0.1"
  g.node_attr["height"] = "0.1"
  g.node_attr["fontsize"] = "8"
  g.node_attr["fontcolor"] = "mediumslateblue"
  g.node_attr["fontname"] = "monospace"
  g.edge_attr["fontsize"] = "8"
  g.edge_attr["fontname"] = "monospace"
  n = len(L)
  for u in range(n):
    g.node(str(u), labels[u] if labels else str(u))
  added = set()
  for v, u in enumerate(path):
    if u != None:
      if weighted:
        for vi, w in L[u]:
          if vi == v:
            break
        g.edge(str(u), str(v), str(w), dir="forward", penwidth="2", color="orange")
      else:
        g.edge(str(u), str(v), dir="forward", penwidth="2", color="orange")
      added.add(f"{u},{v}")
      added.add(f"{v},{u}")
  if weighted:
    for u in range(n):
      for v, w in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v), str(w))
        elif directed:
          g.edge(str(u), str(v), str(w))
  else:
    for u in range(n):
      for v in L[u]:
        if not directed and not f"{u},{v}" in added:
          added.add(f"{u},{v}")
          added.add(f"{v},{u}")
          g.edge(str(u), str(v))
        elif directed:
          g.edge(str(u), str(v))
  return g

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



 
nodes = readFile()
tamaño_node=len(nodes)

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

P=[3349, 3353, 3354, 3355, 3357, 3358, 3359, 3360, 3361, 3366, 3367, 3370, 3375, 3376, 3377, 3379, 3381, 3384, 3388, 3389, 3392, 3393, 3394, 3397, 3398, 3400, 3402, 3403, 3404, 3407, 3409, 3410, 3411, 3413, 3414, 3416, 3417, 3421, 3422, 3423, 3428,
3429, 3431, 3432, 3433, 3435, 3436, 3437, 3440, 3441, 3443, 3445, 3446, 3447, 3448, 3449, 3450, 3451, 3453, 3454, 3455, 3456, 3459, 3461, 3462, 3463, 3466, 3468, 3469, 3471, 3475, 3476, 3477, 3483, 3484, 3485, 3486, 3487, 3489, 3492, 3493, 3494,
3496, 3497, 3498, 3500, 3504, 3505, 3506, 3509, 3512, 3514, 3515, 3516, 3517, 3518, 3520, 3523, 3526, 3527, 3528, 3529, 3531, 3533, 3534, 3535, 3536, 3537, 3541, 3543, 3550, 3551, 3552, 3559, 3563, 3564, 3565, 3566, 3567, 3570, 3571, 3574, 3576,
3579, 3583, 3587, 3588, 3589, 3590, 3594, 3596, 3598, 3603, 3604, 3605, 3606, 3608, 3610, 3614, 3616, 3618, 3620, 3621, 3622, 3623, 3625, 3626, 3628, 3630, 3631, 3632, 3633, 3634, 3637, 3638, 3639, 3641, 3643, 3644, 3647, 3652, 3655, 3656, 3657,
3659, 3660, 3661, 3664, 3668, 3669, 3670, 3671, 3675, 3677, 3678, 3681, 3683, 3684, 3687, 3689, 3690, 3692, 3694, 3696, 3697, 3699, 3700, 3701, 3702, 3703, 3705, 3707, 3712, 3715, 3716, 3717, 3718, 3720, 3723, 3725, 3727, 3728, 3729, 3731, 3733,
3734, 3735, 3736, 3737, 3738, 3739, 3741, 3742, 3746, 3747, 3748, 3749, 3752, 3753, 3754, 3756, 3758, 3759, 3760, 3762, 3765, 3767, 3768, 3773, 3775, 3776, 3777, 3778, 3781, 3783, 3786, 3787, 3790, 3791, 3794, 3795, 3796, 3797, 3802, 3807, 3808,
3809, 3813, 3815, 3816, 3818, 3822, 3827, 3828, 3829, 3834, 3835, 3839, 3841, 3843, 3845, 3846, 3848, 3849, 3851, 3853, 3854, 3857, 3862, 3863, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3876, 3877, 3879, 3880, 3881, 3883, 3884, 3885, 3888, 3889,
3890, 3892, 3893, 3895, 3896, 3897, 3899, 3900, 3902, 3904, 3906, 3909, 3910, 3911, 3912, 3913, 3916, 3917, 3922, 3923, 3926, 3928, 3930, 3931, 3932, 3933, 3934, 3936, 3939, 3941, 3942, 3944, 3946, 3950, 3952, 3954, 3957, 3961, 3964, 3966, 3968,
3970, 3971, 3972, 3975, 3977, 3978, 3980, 3981, 3982, 3985, 3986, 3987, 3990, 3991, 3993, 3995, 3998, 3999, 4002, 4007, 4009, 4010, 4011, 4014, 4019, 4021, 4023, 4025, 4030, 4031, 4032, 4036, 4040, 4041, 4044, 4045, 4046, 4047, 4048, 4049, 4053,
4055, 4056, 4057, 4058, 4062, 4064, 4066, 4067, 4068, 4071, 4074, 4075, 4076, 4077, 4078, 4079, 4080, 4081, 4082, 4084, 4087, 4088, 4089, 4091, 4096, 4101, 4102, 4105, 4106, 4107, 4108, 4109, 4110, 4114, 4115, 4116, 4119, 4123, 4125, 4126, 4127,
4130, 4132, 4135, 4137, 4138, 4140, 4141, 4142, 4143, 4144, 4145, 4148, 4150, 4154, 4155, 4157, 4158, 4160, 4161, 4162, 4163, 4164, 4165, 4166, 4167, 4168, 4172, 4173, 4175, 4176, 4177, 4178, 4179, 4180, 4182, 4184, 4185, 4186, 4188, 4190, 4194,
4195, 4198, 4202, 4205, 4208, 4209, 4210, 4213, 4216, 4217, 4218, 4224, 4229, 4233, 4235, 4237, 4239, 4242, 4244, 4246, 4247, 4249, 4251, 4253, 4255, 4256, 4257, 4258, 4259, 4261, 4264, 4266, 4267, 4268, 4269, 4271, 4272, 4274, 4275, 4277, 4278,
4280, 4285, 4293, 4295, 4296, 4297, 4298, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4309, 4313, 4315, 4317, 4319, 4321, 4322, 4324, 4326, 4327, 4330, 4333, 4335, 4339, 4341, 4343, 4345, 4348, 4350, 4352, 4353, 4356, 4358, 4362, 4363, 4364,
4290, 4294, 4365, 4366, 4367, 4371, 4372, 4373, 4374, 4375, 4376, 4379, 4380, 4383, 4384, 4385, 4386, 4388, 4389, 4391, 4393, 4397, 4398, 4399, 4400, 4401, 4403, 4404, 4405, 4407, 4408, 4416, 4419, 4423, 4428, 4429, 4430, 4431, 4435, 4438, 4439]


points=[3211,3217,3302,3374,3472,3611,3891,3905,3915,4061,4181,4413,4437,4476]   #almacenes


def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hp.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hp.heappush(queue, (f, v))
  return path, cost

def Camino_Dijkstra(graph,points,P):
  with open("output2.txt",mode="w") as file:
    for p in points:
      path,cost = dijkstra(graph,p)
      file.write("Stock con indice al nodo  " + str(p) + "\n")
      for pd in puntosEntrega:
        file.write("Parent del nodo coincide con  " + str(pd.getID()) + " es: " + str(path[pd.getID()]) + "\n")
        file.write("Cost hacia el indice del nodo  " + str(cost[i]) + "\n")
        

path,cost = dijkstra(graph,3211)
print(path)
Camino_Dijkstra(graph,points,puntosEntrega)
adjlShow(graph,weighted=True,path=path)
