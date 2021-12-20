from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import cv2
import numpy as np
from funciones import *

coordx = 824
coordy = 350
video_res = None
RED_BACKGROUND = (217, 20, 66)

if not en_partida() and (find_finish("video.PNG") is None):
    if intenta_salir() == False: pass
    sleep(5)
    intenta_salir()
    if find_finish("wait_img.PNG") is not None:
        print("ESPERAMOS 35 MINUTOS", flush=True)
        sleep(60*35)
        click(1161, 660, 0.4) #Click en OK
print("EMPEZANDO A JUGAR", flush=True)
while True:
    click(1900, 954, 0.2)
    click(1900, 954, 0.2)
    click(1900, 954, 0.2)
    click(1900, 954, 0.2)
    if find_finish("wait_img.PNG") is not None:
        print("ESPERAMOS 35 MINUTOS", flush=True)
        sleep(60*35)
        click(1161, 660, 0.4) #Click en OK
    clicks_linea = 6
    clicks_col = 10
    for j in range(0,10,1):
        finish_res = find_finish("final.PNG")
        if finish_res is not None:
            click(finish_res[0], finish_res[1], 0.4)
            sleep(1)
            video_res = find_finish("video.PNG")
            if video_res is not None: click(video_res[0], video_res[1], 0.4)
            break
        else:
            video_res = find_finish("video.PNG")
            if video_res is not None:
                click(video_res[0], video_res[1], 0.4)
                sleep(2)
                break
        for i in range(0, clicks_linea, 1): #823 Y:  347
            if keyboard.is_pressed('q') == False:
                while pixelMatchesColor(coordx + 47*i, coordy+47*j, RED_BACKGROUND, tolerance=25):
                    print(f"{i}:{j}", flush=True)
                    i=(i+1)%clicks_linea
                    j = (j + 1)%clicks_col if i==5 else j 
                click(coordx + 47*i, coordy+47*j, 0.20)
            else: exit(10)
    if video_res and not en_partida():
        print("Esperando a que pase el anuncio.", flush=True)
        sleep(40)
        print("Probando click hacia atrás.", flush=True)
        click(1900, 954, 0.2)
        click(1900, 954, 0.2)
        sleep(2)
        if(en_partida()): continue
        print("Esperando a que pase el anuncio 10s.", flush=True)
        sleep(10)
        if not en_partida():
            print("Esperando otra vez a que pase el anuncio: 10s.", flush=True)
            sleep(10)
        else:
            continue
        if intenta_salir() == True:
            sleep(0.5)
            sleep(1)
            video_res = None
            print("Reanudamos: MODO AUTOMATICO. Pulsa q para terminar elñ programa", flush=True)
        else:
            print("NO PODEMOS SALIR", flush=True)
            click(950, 520, 0.4) #CLIK AL AZAR
            sleep(2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            sleep(3)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            if(not en_partida() and intenta_salir()==False):    
                if find_finish("wait_img.PNG") is not None:
                    print("ESPERANDO 35 MINUTOS!", flush=True)
                    sleep(60*35)
                    click(1161, 660, 0.4) #Click en OK
                else:
                    click(950, 520, 0.4) #CLIK AL AZAR
                    sleep(2)
                    click(1900, 954, 0.2)
                    click(1900, 954, 0.2)
                    sleep(2)
                    if intenta_salir()==True:
                        break
                    pass
