import numpy as np

# Definimos una matriz cuadrada (puedes elegir los valores que desees)
A = np.array([[2, 1],
              [1, 3]])

# Calculamos los valores propios y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(A)

# Imprimimos los valores propios y vectores propios
print("Valores propios:")
for value in eigenvalues:
    print(value)

print("\nVectores propios:")
for vector in eigenvectors.T:
    print(vector)
