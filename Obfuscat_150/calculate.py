import string

alphabet = string.ascii_letters + string.digits

def calc(stringy):
    result = 0
    for char in stringy:
        result += pow(ord(char)^95, 4)
    return result

def calc_query28():
    for x in alphabet:
        if pow((3111809 - ord(x)), .25).is_integer():
            print x
            print chr(int(pow((3111809 - ord(x)), .25)) ^  95)

def calculate_query27():
    i = 0
    while True:
        if i ^ -857229653 & 255 == 115:
            print i
            break
        i += 1

calculate_query27()
