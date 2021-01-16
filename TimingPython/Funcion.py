
### Aquí está la función, que asignará a un segundo array, los números del primero, transformados ###

import time
import math
import statistics as st
tiempos = []

def funcion(a):
    return math.log2(a)

def funcion_al_vector(vector, vector2):
    start_time = time.time()
    for i in range(0,len(vector)):
        #    print(i)
        a = vector[i]
        vector2[i] = funcion(a)

    tiempos.append(time.time()-start_time)
    print("TIEMPO:" + str(time.time()-start_time))
