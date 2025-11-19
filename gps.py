from collections import deque
import random

def crear_ciudad(dimension, caracter_edificio, caracter_agua, porcentaje, camino):
    matriz = [[camino for _ in range(dimension)] for _ in range(dimension)]

    for fila in range(0, dimension, 2):
        for columna in range(0, dimension, 2):
            matriz[fila][columna] = caracter_edificio

        for fila in range(dimension):
            for columna in range(dimension):
                if matriz[fila][columna] == camino:
                    if random.randint(0, 100) <= porcentaje:
                        matriz[fila][columna] = caracter_agua
    
    for fila in matriz:
        print(' '.join(fila))
    
    return matriz

def movimientos_validos(posicion_entrada, edificio, agua, posicion_obstaculo_opcional, dimension, ciudad):
    fila_entrada, columna_entrada = posicion_entrada
    movimientos_validos = []
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]