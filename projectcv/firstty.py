from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2
import numpy as np

def click(x,y, delay):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def print_coords():
    while True:
        if(keyboard.is_pressed('f')):
            pyautogui.position()

def find_finish(nombre_template):
    
    th=0.1

    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    method = cv2.TM_SQDIFF_NORMED
    
    template = cv2.imread(nombre_template)
    h, w, c= template.shape

    img = np.array(pyautogui.screenshot())
    img = img[:, :, ::-1].copy() # RBG to BGR
    result = cv2.matchTemplate(img, template, method)
    loc = np.where( result <= th) # filter the results
    if np.shape(loc) == (2,0):
        print(f"No se encuentra {nombre_template}", flush=True)
        return None
    #print(np.shape(loc))
    yav = loc[0][0]+(h//2)
    xav = loc[1][0]+(w//2)
    print(f" {nombre_template} Match at: {xav};{yav}")
    
    #cv2.imshow("Captura", img)
    #cv2.imshow("Resultado", result)
    #print(loc)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return (xav, yav)

def intenta_salir():

    lista = ["flechita", "flechita2", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x13"]
    #lista = ["flechita", "flechita2"]

    for template in lista:
        loc = pyautogui.locateOnScreen(f'C:/Users/Nicolas/Desktop/Programacion/Personal-2020/projectcv/{template}.PNG', grayscale=False, confidence=0.8)
        if loc is not None:
            x, y = pyautogui.center(loc)
            click(x, y, 0.4)
            print(f"encontrada {template}", flush=True)
            #click(1900, 954, 0.2)
            #click(1900, 954, 0.2)
            return True
        else:
            print(f"NO encontrada {template}", flush=True)
    return False

def en_partida():
    posicion_template = find_cross("partida_img.PNG")
    if posicion_template is not None:
        return True
    else:
        return False

coordx = 824
coordy = 350
video_res = None

#video_res = find_finish("video.PNG")
#win32api.SetCursorPos((video_res[0], video_res[1]))
intenta_salir()
while False:
    clicks_linea = 6
    for j in range(0,10,1):
        finish_res = find_finish("final.PNG")
        if finish_res is not None:
            click(finish_res[0], finish_res[1], 0.4)
            sleep(2)
            video_res = find_finish("video.PNG")
            click(video_res[0], video_res[1], 0.4)
            break
        else:
            video_res = find_finish("video.PNG")
            if video_res is not None:
                click(video_res[0], video_res[1], 0.4)
                break
            if clicks_linea == 6:
                pared_res = find_finish("pared.PNG")
                if pared_res is not None:
                    clicks_linea = 5
        for i in range(0, clicks_linea, 1): #823 Y:  347
            if keyboard.is_pressed('q') == False:
                click(coordx + 47*i, coordy+47*j, 0.20)
            else: exit(10)
    if video_res and not en_partida():
        print("Esperando a que pase el anuncio.", flush=True)
        sleep(30)
        print("Probando click hacia atrás.", flush=True)
        click(1900, 954, 0.2)
        click(1900, 954, 0.2)
        if(en_partida()): break
        print("Esperando a que pase el anuncio 10s.", flush=True)
        sleep(10)
        if intenta_salir() == True:
            video_res = None
            print("Reanudamos: MODO AUTOMATICO. Pulsa q para terminar elñ programa", flush=True)
        else:
            print("NO PODEMOS SALIR", flush=True)
            exit(28)
