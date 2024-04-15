import numpy as np 
#Matplotlib tiene muchos módulos. 
import matplotlib.pyplot as plt #pyplot es el modulo para hacer graficos

#Crear un ndarray de 1 dimensión, 100 elementos equiespaciados, de 0 a 2*PI

x=np.linspace(0,2*np.pi,100) #eje x
y=np.sin(x) #eje y

#usar matplotlib 

plt.figure(figsize=(8,4)) #dandole la figurita al dibujo #figsize es el tamaño

plt.title("Mi primer gráfico cientifica en PO")

plt.plot(x,y) #plot es graficar el eje x y el eje y en el arreglo

plt.xlabel("x") #nombre del eje x

plt.ylabel("seno de x") #nombre del eje y

plt.grid(True)

plt.show()
