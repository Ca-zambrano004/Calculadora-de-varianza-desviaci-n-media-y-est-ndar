import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir la lista en un arreglo 3x3
    matriz = np.array(lista).reshape(3, 3)

    # Construir el diccionario con los cálculos
    calculos = {
        'mean': [
            matriz.mean(axis=0).tolist(),   # columnas
            matriz.mean(axis=1).tolist(),   # filas
            matriz.mean().tolist()          # total
        ],
        'variance': [
            matriz.var(axis=0).tolist(),
            matriz.var(axis=1).tolist(),
            matriz.var().tolist()
        ],
        'standard deviation': [
            matriz.std(axis=0).tolist(),
            matriz.std(axis=1).tolist(),
            matriz.std().tolist()
        ],
        'max': [
            matriz.max(axis=0).tolist(),
            matriz.max(axis=1).tolist(),
            matriz.max().tolist()
        ],
        'min': [
            matriz.min(axis=0).tolist(),
            matriz.min(axis=1).tolist(),
            matriz.min().tolist()
        ],
        'sum': [
            matriz.sum(axis=0).tolist(),
            matriz.sum(axis=1).tolist(),
            matriz.sum().tolist()
        ]
    }

    return calculos
