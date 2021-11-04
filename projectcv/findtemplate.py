import numpy as np
import cv2

def findtemplate(img, img2, template, color, method):
    h, w = template.shape




    # BITCOIN 
    result = cv2.matchTemplate(img, template, method)

    ## WHAT IS THIS LOL https://stackoverflow.com/questions/56977429/using-cv-matchtemplate-to-find-multiple-best-matches
    threshold = 0.03
    loc = np.where( result <= threshold) # filter the results

    matches = list(zip(*loc[::-1]))# Zipping the 2 array into an array of pairs of coordinates (x, y)

    count = 0
    mask = np.zeros(img.shape[:2], np.uint8)
    for pt in zip(*loc[::-1]):
        if mask[pt[1] + int(round(h/2)), pt[0] + int(round(w/2))] != 255:
            mask[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = 255
            #cv2.imshow('mask', mask)
            count += 1
            #cv2.rectangle(img2, pt, (pt[0] + w, pt[1] + h), 0, 4)
            pt2 = (pt[0]+w//2, pt[1]+w//2)
            cv2.circle(img2, pt2, w, color, 3)


    return (count)