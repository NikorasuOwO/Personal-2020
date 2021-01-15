
### Timing test script ###

import time
import math
import random
import statistics as st
import os
import pandas

def funcion(a):
    return round(1.0/math.sqrt(round(a)))

vector = []

n = 100
l = 100000
rango = (1,n)
lg = (0,l)
kmax = 10
k = 1
tiempos = []
vector2 = [0]*l # Creamos vector2, un array con n ceros.

if( 4 < ( n * 32 / (1024*1024*1024) )* kmax ):
    input("Mucho n o k bro: n: " + str(n) + "k: " + str(k))

    #os.sys.exit() ó #exit() ó quit() Es lo mismo.

    kmax = -1
for i in range(lg[0],lg[1]):
    vector.append(random.uniform(rango[0],rango[1]))


TiempoTOTAL = time.time()

while(k <= kmax):
    i = 0
    start_time = time.time()
    for i in range(lg[0],lg[1]):
    #    print(i)
        a = vector[i]
        vector2[i] = funcion(a)

    tiempos.append(time.time()-start_time)
    print("TIEMPO:" + "(" + str(k) + ")" + str(time.time()-start_time))
    k = k + 1

TiempoTOTAL = time.time() - TiempoTOTAL
media = st.mean(tiempos)
print("\n\n RESULTADOS:   MEDIA: " + str(media) + "  | TIEMPO TOTAL: "+ str(TiempoTOTAL))

input("\n\n\n**** FIN DEL PROGRAMA **** ")
