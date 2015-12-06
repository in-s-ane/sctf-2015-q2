import cv2
import numpy as np
from matplotlib import pyplot as plt

templates = [cv2.imread("img"+str(x)+".png",0) for x in range(10)]

method = cv2.TM_CCORR_NORMED

for i,template in enumerate(templates):
    img_rgb = cv2.imread('shapes.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, method)
    threshold = 1
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv2.imwrite('res'+str(i)+'.png', img_rgb)

