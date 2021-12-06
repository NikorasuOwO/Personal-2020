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
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def print_coords():
    while True:
        if(keyboard.is_pressed('f')):
            pyautogui.position()

def find_finish(nombre_template):
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    method = cv2.TM_SQDIFF_NORMED
    
    template = cv2.imread(nombre_template)
    h, w, c= template.shape

    img = np.array(pyautogui.screenshot())
    img = img[:, :, ::-1].copy() # RBG to BGR
    result = cv2.matchTemplate(img, template, method)
    loc = np.where( result <= 0.1) # filter the results
    if np.shape(loc) == (2,0): return None
    #print(np.shape(loc))
    yav = loc[0][0]+(h//2)
    xav = loc[1][0]+(w//2)
    print(f" {nombre_template} Match at: {xav};{yav}")
    return (xav, yav)
    #cv2.imshow("Captura", img)
    #cv2.imshow("Resultado", result)
    #print(loc)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

coordx = 824
coordy = 350
video_res = None

#video_res = find_finish("video.PNG")
#win32api.SetCursorPos((video_res[0], video_res[1]))
while True:
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
        for i in range(0, 6, 1): #823 Y:  347
            if keyboard.is_pressed('q') == False:
                click(coordx + 47*i, coordy+47*j, 0.20)
            else: exit(10)
    if video_res:
        print("Esperando a que pase el anuncio: MODO MANUAL. Pulsa c para seguir o q para terminar el programa", flush=True)
        while(keyboard.is_pressed('c') == False):
            if keyboard.is_pressed('q'):
                exit()
            else:
                sleep(0.1)
        video_res = None
        print("Reanudamos: MODO AUTOMATICO. Pulsa q para terminar elñ programa", flush=True)