#methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


import numpy as np
import cv2
from matplotlib import pyplot as plt
from findtemplate import findtemplate

img = cv2.imread('board.PNG', 0)
templateBTC = cv2.imread('btc.PNG', 0)
templateETH = cv2.imread('eth.PNG', 0)
templateLTC = cv2.imread('ltc.PNG', 0)
templateUSDC = cv2.imread('usdc.PNG', 0)
templateXRP = cv2.imread('xrp.PNG', 0)

if img is None:
    print("img or template not found")
    quit()

img2 = img.copy()
total = {}
#BTC
total["BTC"]= findtemplate(img, img2, templateBTC, 150, cv2.TM_SQDIFF_NORMED)

#ETH
total["ETH"]= findtemplate(img, img2, templateETH, 50, cv2.TM_SQDIFF_NORMED)
#LTC
total["LTC"]= findtemplate(img, img2, templateLTC, 100, cv2.TM_SQDIFF_NORMED)
#USDC
total["USDC"]= findtemplate(img, img2, templateUSDC, 0, cv2.TM_SQDIFF_NORMED)
#XRP
total["XRP"]= findtemplate(img, img2, templateXRP, 255, cv2.TM_SQDIFF)


cv2.imshow('Image', img)
cv2.imshow('Match', img2)
#cv2.imshow('res', result)
#cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(total) 
