import numpy as np

#item a
A = np.array([1 ,0, -1])
B = np.array([2 ,1 ,0])
D = np.array([-1, 0, 0])
#item b
AB = B - A
C = AB + D

print("Ponto C:", tuple(C),end="")

#item c
d = float(input("Digite a distância: "))
BD = D - B
N = np.cross(AB, BD)
Norma_N= np.linalg.norm(N)
Versor_Normal = N/Norma_N
CE = d * Versor_Normal
E = CE + C
print("Ponto E:", tuple(E)) 

#item d
O = (A + C)/2
print("Ponto O:", tuple(O)) 

#item e
BO = O - B
BE = E - B
ANGULO = np.degrees(np.arccos ( np.dot(BO, BE) / ( np.linalg.norm(BO) * np.linalg.norm(BE) )  
                                                       ) ) 
print("Ângulo θ:", ANGULO)

#item f
AD = D - A
V_Para = np.cross(AB, AD) 
V_Para = np.dot(V_Para, CE )
V_Pira = V_Para/3
print("Volume da Pirâmide:", V_Pira)