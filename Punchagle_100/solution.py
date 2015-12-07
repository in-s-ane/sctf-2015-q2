import cv2
import numpy as np
from matplotlib import pyplot as plt
import itertools

templates = [cv2.imread("img"+str(x)+".png",0) for x in range(10)]

method = cv2.TM_CCORR_NORMED

def round_to_nearest(number, base=5):
    return int(base * round(float(number)/base))

dec = ""
for x in range(1, 10001):
    data = {}
    for i,template in enumerate(templates):
        img_rgb = cv2.imread('images/img%s.png' % x)
        print "img%s" % x
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, method)
        threshold = .98
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            y = pt[1]
            rounded = str(round_to_nearest(y))
            if rounded not in data:
                data[rounded] = [i]
            else:
                data[rounded].append(i)
            # print y, pt, i
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        # cv2.imwrite('res'+str(i)+'.png', img_rgb)
    for row in data:
        for x in range(2, 4):
            for candidate in itertools.product(data[row], repeat=x):
                try:
                    char = "".join(str(x) for x in candidate)
                    dec += char
                except:
                    pass

open("dec.txt", "w").write(dec)
