
### Timing test script ###

import time
import random
import statistics as st
import pandas
import Funcion

## VARIABLES ##
vector = []
n = int(input("n: "))
# n = 500  # Rango máximo de los números
l = 1000000  # Número de cálculos
rango = (1, n)  # Tupla rango de los números
lg = (0, l)  # Tupla numero de cálculos (accesos a vector)
kmax = 10  # Número de repeticiones
vector2 = [0] * l  # Creamos vector2, un array con n ceros.

# INIT #
k = 1

for i in range(lg[0], lg[1]):  # Ponemos en vector numeros aleatorios
    vector.append(random.randint(rango[0], rango[1]))

TiempoTOTAL = time.time()  # Empezamos a contar el tiempo total de cálculo

# Empezamos las kmax repeticiones
while(k <= kmax):

    Funcion.funcion_al_vector(vector, vector2)
    k = k + 1
# repeticiones acabadas, dejamos de contar el tiempo total.
TiempoTOTAL = time.time() - TiempoTOTAL
# Sacamos la media de los tiempos de ejecución de l operaciones,
#   con el vector tiempos que rellena la función
media = st.mean(Funcion.tiempos)


# Imprimimos los resultados! #
print("\n\n RESULTADOS SQRT:   MEDIA: " + str(media) + "  | TIEMPO TOTAL: " + str(TiempoTOTAL)
+ "\n\n n: " + str(n) + "  | l: " + str(l))
input("\n\n\n **** FIN DEL PROGRAMA **** ")
