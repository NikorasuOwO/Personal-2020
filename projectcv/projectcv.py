#methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


import numpy as np
import cv2
from matplotlib import pyplot as plt
from findtemplate import findtemplate

### COLORS ###
# (B, G, R)
white = (255, 255, 255)
green = (100, 255, 0)
black = (0,0,0)
blue = (255, 10, 10)
red = (10, 10, 255)


img = cv2.imread('board3.PNG')
H, W, C = img.shape
templateBTC = cv2.imread('btc.PNG')
templateETH = cv2.imread('eth.PNG')
templateLTC = cv2.imread('ltc.PNG')
templateUSDC = cv2.imread('usdc.PNG')
templateXRP = cv2.imread('xrp.PNG')
templateBOMB = cv2.imread('bomb.PNG')
if img is None:
    print("img or template not found")
    quit()

img2 = img.copy()
info = {}
#BTC
info["BTC"] = {}
info["BTC"]["count"], info["BTC"]["points"] = findtemplate(img, img2, templateBTC, green, cv2.TM_SQDIFF_NORMED, th=0.08) # t=0.2

#ETH
info["ETH"] = {}
info["ETH"]["count"], info["ETH"]["points"] = findtemplate(img, img2, templateETH, green, cv2.TM_SQDIFF_NORMED, th=0.28) # t=0.2

#LTC
info["LTC"] = {}
info["LTC"]["count"], info["LTC"]["points"] = findtemplate(img, img2, templateLTC, green, cv2.TM_SQDIFF_NORMED, th=0.07) # t=0.2
#USDC
info["USDC"] = {}
info["USDC"]["count"], info["USDC"]["points"] = findtemplate(img, img2, templateUSDC, green, cv2.TM_SQDIFF_NORMED, th=0.16) # t=0.2
#XRP
info["XRP"] = {}
info["XRP"]["count"], info["XRP"]["points"] = findtemplate(img, img2, templateXRP, green, cv2.TM_SQDIFF_NORMED, th=0.35) # t=0.2
#BOMB
info["BOMB"] = {}
info["BOMB"]["count"], info["BOMB"]["points"] = findtemplate(img, img2, templateBOMB, red, cv2.TM_SQDIFF_NORMED, th=0.35) # t=0.2

cv2.imshow('Image', img)
cv2.imshow('Match', img2)
#cv2.imshow('res', result)
#cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(info)
print(sum( [coin["count"] for coin in info.values() ] ))


#MAPPING TO ONE GRID

grid = np.zeros((10, 6))


# ASIGNING COINS POSITIONS ON THE GRID
i = 1

#coords_list = [BTCpoints, ETHpoints, LTCpoints, USDCpoints, XRPpoints, BOMBpoints]

for coin in info.values():
    coin["grid_index"] = []
    for point in coin["points"]:
        x, y = point
        xgrid = int(np.interp(x, [0, W], [0, 6]))
        ygrid = int(np.interp(y, [0, H], [0, 10]))
        coin["grid_index"].append((xgrid, ygrid))
        try:
            grid[ygrid][xgrid] = i
        except IndexError:
            print("ERROR INDEXING" + str(i) + "coords list at indexes: " + str(point) )
    i = i + 1

print(grid)
print()
print(info["BTC"])