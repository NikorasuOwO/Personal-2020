
### Timing test script ###

import time
import math
import random
import statistics as st
import os
import pandas

vector = []
vector2 = []
n = 100
rango = (-n,n)
kmax = 5
k = 1
tiempos = []

if( 4 < 2*( n * 32 / (1024*1024*1024) )* kmax ):
    input("Mucho n o k bro: n: " + str(n) + "k: " + str(k))

    #os.sys.exit() ó #exit() ó quit() Es lo mismo.

    kmax = -1
for i in range(0,2*n):
    vector.append(random.uniform(rango[0],rango[1]))


TiempoTOTAL = time.time()

while(k <= kmax):
    start_time = time.time()
    for i in range(0,2*n - 1):
        #print(i)
        a = vector[i]
        vector2.append(round(math.sqrt(a*a)))

    print("TIEMPO:" + "(" + str(k) + ")" + str(time.time()-start_time))
    tiempos.append(time.time()-start_time)

    k = k + 1

media = st.mean(tiempos)
TiempoTOTAL = time.time() - TiempoTOTAL
print("MEDIA: " + str(media) + "TIEMPO TOTAL: "+ str(TiempoTOTAL))
