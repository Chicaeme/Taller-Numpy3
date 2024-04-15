#Numpy: Biblioteca para realizar calculos numericos en arreglos
#ndimensionales. 

import numpy as np

#crear un arreglo ndarray de 2 dimensiones a partir de una lista

A=np.array([[1,5],[7,9]])
B=np.array([[2,0],[1,3]])

#producto punto entre ndarrays
C=np.dot(A,B)
print(C)

#Solución de un sistema de ecuaciones con numpy para generar X1 y X2
m_solucion=np.array([5,17])

m=np.linalg.solve(A,m_solucion)  #para obtener X1 y X2
print(m)
