import base64
import random
import string

flag = open('flag.txt').read()

for i in range(80):
    if random.random() < 0.5:
        flag = base64.b64encode(flag.encode('utf8')).decode('utf8')
    else:
        alphabet = string.ascii_letters + string.digits
        shift = random.randint(1,len(alphabet))
        alphabet_shift = alphabet[shift:] + alphabet[:shift]
        flag = flag.translate(str.maketrans(alphabet, alphabet_shift))

open('encrypted.txt','w').write(flag)
