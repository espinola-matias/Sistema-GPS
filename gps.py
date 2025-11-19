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

    for direccion in direcciones:
        nueva_fila = fila_entrada + direccion[0]
        nueva_columna = columna_entrada + direccion[1]
        if 0 <= nueva_fila < dimension and 0 <= nueva_columna < dimension:
            if ciudad[nueva_fila][nueva_columna] != edificio and ciudad[nueva_fila][nueva_columna] != agua:
                if(nueva_fila, nueva_columna) not in posicion_obstaculo_opcional:
                    movimientos_validos.append((nueva_fila, nueva_columna))
    return movimientos_validos

def encontrar_camino(entrada, salida, posicion_edificio, posicion_agua, posicion_obstaculo_opcional, dimension, ciudad):
    if entrada == salida:
        return [entrada]
    
    cola = deque([(entrada, [entrada])])
    visitados = {entrada}

    while cola:
        posicion_actual, camino_actual = cola.popleft()
        vecinos = movimientos_validos(posicion_actual, posicion_edificio, posicion_agua, posicion_obstaculo_opcional, dimension, ciudad)
        
        for vecino in vecinos:
            if vecino == salida:
                return camino_actual + [vecino]
            
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = camino_actual + [vecino]
                cola.append((vecino, nuevo_camino))
    
    return None # si no se encuentra camino 

def mostrar_camino(ciudad, camino, entrada, salida, inicio, destino, ruta):
    ciudad_con_camino = [fila[:] for fila in ciudad] # copia para no dañar el original
    
    for fila, columna in camino:
        if (fila, columna) == entrada:  
            ciudad_con_camino[fila][columna] = inicio
        elif (fila, columna) == salida:  
            ciudad_con_camino[fila][columna] = destino
        else: 
            ciudad_con_camino[fila][columna] = ruta

        for fila in ciudad_con_camino:
            print(" ".join(fila))

# configuracion inicial de los parametros del gps 
def inicio_gps():

    inicio = "✅"
    destino = "❌"
    ruta = "◾"
    camino = "⬜"
    edificio = "🏨"
    agua = "♒"
    caracter_obstaculo = "🧱"
    porcentaje_agua = 4
    dimension_min = 5

    print("-- ¡Bienvenido a la ciudad! --")
    while True:
        try:
            dimension = int(input(f"*Dime el tamaño de la ciudad. OBS('El tamaño debe ser mayor a {dimension_min}!'): "))
            if dimension <= dimension_min:
                print(f"El valor debe ser mayor a {dimension_min}, ajustamos a un valor por defecto!")
                dimension = dimension_min
            break
        except ValueError:
            print("Favor solo ingresar numeros!")

    mapa_ciudad = crear_ciudad(dimension, edificio, agua, porcentaje_agua, camino)
    print("\n--- Configuremos tu destino ---")

    while True:
        try:    
            fila_entrada = int(input("Dime la fila del punto de partida: "))
            columna_entrada = int(input("Dime la columna del punto de partida: "))
            entrada = (fila_entrada, columna_entrada)

            if not (0 <= fila_entrada < dimension and 0 <= columna_entrada < dimension):
                print(f"Este punto esta fuera de los limites de la ciudad {fila_entrada, columna_entrada}")
            elif mapa_ciudad[fila_entrada][columna_entrada] == edificio:
                print(f"Aqui no puedes colocar, hay un edificio {fila_entrada, columna_entrada}")
            elif mapa_ciudad[fila_entrada][columna_entrada] == agua:
                print(f"Aqui no puedes colocar, hay un rio {fila_entrada, columna_entrada}")
            else:
                print(f"*Colocaste la entrada en {fila_entrada, columna_entrada}")
                break
        except ValueError:
            print("Favor solo ingrese numeros")

    while True:
        try:    
            fila_salida = int(input("Dime la fila del punto de llegada: "))
            columna_salida = int(input("Dime la columna del punto de llegada: "))
            salida = (fila_salida, columna_salida)

            if not (0 <= fila_salida < dimension and 0 <= columna_salida < dimension):
                print(f"Este punto esta fuera de los limites de la ciudad {fila_salida, columna_salida}")
            elif mapa_ciudad[fila_salida][columna_salida] == edificio:
                print(f"Aqui no puede colocar, hay un edificio {fila_salida, columna_salida}")
            elif mapa_ciudad[fila_salida][columna_salida] == agua:
                print(f"Aqui no puedes colocar, hay un rio {fila_salida, columna_salida}")
            elif salida == entrada:
                print(f"Estas colocando en el mismo punto de inicio {fila_salida, columna_salida}")
            else:
                print(f"Colocaste la salida en {fila_salida, columna_salida}")
                break

        except ValueError:
            print("Favor solo ingrese numeros")

    mapa_ciudad[fila_entrada][columna_entrada] = inicio
    mapa_ciudad[fila_salida][columna_salida] = destino

    obstaculo_opcional = []
    camino = encontrar_camino(entrada, salida, edificio, agua, obstaculo_opcional, dimension, mapa_ciudad)

    if camino:
        print("\n-- ¡Encontramos el camino! --")
        mostrar_camino(mapa_ciudad, camino, entrada, salida, inicio, destino, ruta)
    else:
        print("\nNo se pudo llegar al punto, las calles estan bloqueadas!")
        for fila in mapa_ciudad:
            print(" ".join(fila))
        return
    
    while True:
        try:
            obstaculo = int(input("\nIngrese el numero de la opcion que desea 1- Quiero ingresar un obstaculo 2- No deseo agregar nada(Salir): "))
            if obstaculo == 1:
                fila_obstaculo = int(input("Dime la fila del obstaculo: "))
                columna_obstaculo = int(input("Dime la columna del obstaculo: "))
                obstaculo_agregado = (fila_obstaculo, columna_obstaculo)

                if not (0 <= fila_obstaculo < dimension and 0 <= columna_obstaculo < dimension):
                    print(f"Esta posicion no es valida ya que esta fuera de la ciudad {fila_obstaculo, columna_obstaculo}")
                elif obstaculo_agregado == entrada or obstaculo_agregado == salida:
                    print(f"No se puede agregar obstaculo ya que esta en el punto de Partida/Llegada ({fila_obstaculo, columna_obstaculo})")
                elif mapa_ciudad[fila_obstaculo][columna_obstaculo] == edificio:
                    print(f"No se puede agregar aqui ya que es un Edificio {fila_obstaculo, columna_obstaculo}")
                elif mapa_ciudad[fila_obstaculo][columna_obstaculo] == agua:
                    print(f"No se puede agregar aqui ya que es un Rio {fila_obstaculo, columna_obstaculo}")
                elif obstaculo_agregado in obstaculo_opcional:
                    print(f"Aqui ya agregaste un obstaculo!!{fila_obstaculo, columna_obstaculo}")
                else:
                    obstaculo_opcional.append(obstaculo_agregado)
                    print(f"Agregaste un obstaculo temporal en la posicion {fila_obstaculo, columna_obstaculo}")

                    mapa_ciudad[fila_obstaculo][columna_obstaculo] = caracter_obstaculo
                    camino = encontrar_camino(entrada, salida, edificio, agua, obstaculo_opcional, dimension, mapa_ciudad)
                    if camino:
                        print("\n-- ¡Encontramos el camino! --")
                        mostrar_camino(mapa_ciudad, camino, entrada, salida, inicio, destino, ruta)
                    else:
                        print("\n-- ¡No se pudo llegar al punto, las calles estan bloqueadas! --")
                        for fila in mapa_ciudad:
                            print(" ".join(fila))
                        break

            elif obstaculo == 2:
                break
            else:
                print("Opcion no valida favor lea las opciones e ingrese el numero")
        except ValueError:
            print("Favor solo ingrese numeros")

if __name__ == "__main__":
    inicio_gps()