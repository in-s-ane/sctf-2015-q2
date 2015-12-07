import cv2
import numpy as np

templates = [cv2.imread("img"+str(x)+".png",0) for x in range(10)]

method = cv2.TM_CCORR_NORMED

dec = ""
for img in range(1, 10001):
    base = 2
    shapes = []
    for i,template in enumerate(templates):
        img_rgb = cv2.imread('images/img%s.png' % img)
        print "img%s template%s" % (img,i)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, method)
        threshold = .98
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]
            shapes.append((x, y, i))

    shapes = sorted(shapes, key=lambda x: x[1])

    while base <= len(shapes):
        row = sorted(shapes[:base])
        dec += "".join([str(x[2]) for x in row])
        shapes = shapes[base:]
        base += 1

index = dec.find("11599116102")
if index != -1:
    print "The flag is probably somewhere in this string: %s" % dec[index:index+100]
else:
    print "Could not find the flag :("

# Decode the outputted string into corresponding ascii values

# sctf{prettycoolrite}
