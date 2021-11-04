#methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


import numpy as np
import cv2
from matplotlib import pyplot as plt
from findtemplate import findtemplate

img = cv2.imread('board.PNG')

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()