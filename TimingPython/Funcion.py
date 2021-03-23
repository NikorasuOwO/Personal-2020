
### Aquí está la función, que asignará a un segundo array,
# los números del primero, transformados ###

import time
import math
tiempos = []


def funcion_factorial(a):
    print("hola")


def funcion(a):
    return math.sqrt(a)


def funcion2(a):
    return math.sqrt(a)


def funcion_al_vector(vector, vector2):
    start_time = time.time()

    for i in range(0, len(vector)):
        #    print(i)
        a = vector[i]
        vector2[i] = funcion(a)

    tiempos.append(time.time() - start_time)
    print("TIEMPO:" + str(time.time() - start_time))
