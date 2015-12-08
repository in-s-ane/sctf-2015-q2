import cv2
import numpy as np
import sys

templates = [cv2.imread("img"+str(x)+".png",0) for x in range(10)]

method = cv2.TM_CCORR_NORMED

dec = ""
for img in range(1, 10001):
    shapes = []

    for i,template in enumerate(templates):
        img = 144
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
            # Correct some template offsets
            if i == 6:
                y += 1
            elif i == 9:
                y -= 4
            elif i == 1:
                y -= 1
            elif i == 2:
                y -= 1
            if i == 3:
                print img
                sys.exit(0)
            shapes.append((x, y, i))

    shapes = sorted(shapes, key=lambda x: (x[1], x[0]))

    dec += "".join([str(x[2]) for x in shapes])
    index = dec.find("1159911610212") # sctf and { without the "3" in ascii
    if index != -1:
        print "Flag signature found within img%s.png" % img
        sys.exit(0)

# Some shapes are missing from the images, so we won't be able to just search for sctf{ like in the last problem.
# It is especially noteworthy that there are no unfilled boxes, so no threes will ever appear, which
# makes it impossible for "123" to appear, which signified a "{"
# However, by stringing together the output from the shapes we DO have, we can grep for sctf.
# Running this script, we find a match from image 144. Opening up this image and looking for the signature,
# we can find out which shapes are missing where, and kind of form the flag.

    # From img 144:
    # 115 s
    # 99  c
    # 116 t
    # 102 f
    # 123 { # can assume that a "3" was missing
    # 10_
    # 101 e
    # 10_
    # 10_
    # 111 o
    # 10_
    # 101 e
    # 10_
    # 10_
    # 111 o
    # 125 }

# Considering that _ may replace any number 0-9, we need to use the alphabet d-m
# Flag looks something like this: sct{_e__o_e__o}
# godlike guessing skills = flag

# sctf{hellohello}
