#!/usr/bin/env python
from z3 import *

"""
encyption algorithm:
    8 * (x & 0x18) | ((x & 0xE0) >> 2) | (x & 7)


"""
enc =  [0x1e, 0x5c, 0x19, 0x1f, 0xdb, 0x5d,
        0xd9, 0xd7, 0x9f, 0x8b, 0x89, 0x9b,
        0x9b, 0x5d, 0x8c, 0x5e, 0xd7, 0x9b,
        0x1b, 0x88, 0x9a, 0x1d, 0xd7, 0x89,
        0xda, 0xd7, 0x88, 0xd8, 0x16, 0x16,
        0xd7, 0x9c, 0x58, 0x8b, 0xd7, 0x1b,
        0x58, 0x8c, 0x9a, 0x8f, 0x9b, 0xdd,
        0x42]
s = Solver()
X = [BitVec("x_%s" % (i+1),32) for i in range(len(enc))]
s.add([enc[i] == (8 * (X[i] & 0x18) | ((X[i] & 0xE0) >> 2) | (X[i] & 7))
    for i in range(len(enc))])
if s.check() == sat:
    m = s.model()
    r = [m.evaluate(X[i]) for i in range(len(X))]
    r = [int(str(x)) for x in r]
    print "".join(chr(x) for x in r)
else:
    print "fail"