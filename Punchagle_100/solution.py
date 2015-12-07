import cv2
import numpy as np
from matplotlib import pyplot as plt
import itertools

templates = [cv2.imread("img"+str(x)+".png",0) for x in range(10)]

method = cv2.TM_CCORR_NORMED

def round_to_nearest(number, base=5):
    return int(base * round(float(number)/base))

dec = ""
#for img in range(1, 10001):
for i,template in enumerate(templates):
    data = {}
    #img_rgb = cv2.imread('images/img%s.png' % img)
    img_rgb = cv2.imread('example1.png')
    #print "img%s template%s" % (img,i)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, method)
    threshold = .98
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #i think this x,y shit is wrong. doesn't match up with Pinta.
        #flipped and complemented or something
        x = round_to_nearest(pt[0])
        y = round_to_nearest(pt[1])
        if (x,y) in data:
            assert False, "something wrong here"
        data[(x,y)] = i
        # print y, pt, i
        # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    #make assoc array
    data = zip(data.keys(), data.values())
    #sort by y
    print i
    # y1 > y2: y1 above
    # x1 > x2: x1 on left
    def compare(a,b):
        return (b[0][1] - a[0][1]) * 10000 + (b[0][0] - a[0][0])
    for p in sorted(data, cmp=compare):
        print p

    # cv2.imwrite('res'+str(i)+'.png', img_rgb)
# for row in data:
#     for x in range(1,4):
#         for candidate in itertools.product(data[row], repeat=x):
#             try:
#                 char = "".join(str(x) for x in candidate)
#                 dec += char
#             except:
#                 pass
