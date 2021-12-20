from pyautogui import *
import pyautogui
import time
import keyboard
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
        #print(f"No se encuentra {nombre_template}", flush=True)
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
    click(20, 1015, 0.4)
    click(20, 1015, 0.4)
    sleep(0.5)
    click(1900, 954, 0.2)
    click(1900, 954, 0.2)
    lista = ["flechita", "flechita2", "x2", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x13", "x14", "x15", "x16", "x17", "x19", "x20"]
    #lista = ["flechita", "flechita2"]

    for template in lista:
        loc = pyautogui.locateOnScreen(f'C:/Users/Nicolas/Desktop/Programacion/Personal-2020/projectcv/{template}.PNG', grayscale=True, confidence=0.8)
        if loc is not None:
            x, y = pyautogui.center(loc)
            click(x, y, 0.4)
            print(f"encontrada {template}", flush=True)
            return True
        else:
            #print(f"NO encontrada {template}", flush=True)
            pass
    return buscar_y_probar_salir()
    
def en_partida():
    posicion_template = find_finish("partida_img.PNG")
    return posicion_template is not None
def buscar_y_probar_salir():

    #Arriba derecha
    for y in range(10):
        for x in range(10):
            click(1152+x*10, 70+y*10, 0.5)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            video_res = find_finish("video.PNG")
            if video_res is not None:
                click(video_res[0], video_res[1], 0.4)
                return True

    #Arriba muy derecha
    for y in range(10):
        for x in range(10):
            click(1750+x*10, 57+y*10, 0.5)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            click(1900, 954, 0.2)
            video_res = find_finish("video.PNG")
            if video_res is not None:
                click(video_res[0], video_res[1], 0.4)
                return True
    return False