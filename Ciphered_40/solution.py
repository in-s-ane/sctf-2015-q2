import string

enc = open("encrypted.txt", "r").read().strip()
alphabet = string.ascii_letters + string.digits

# Check if the base64 decryption of a candidate is valid text
def is_valid_base64(candidate):
    try:
        candidate.decode("base64").decode("utf-8")
        return True
    except:
        return False

def caesar(plaintext, shift):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

# Brute force the decryption
for x in range(80):
    if is_valid_base64(enc):
        # Valid base64, so let's decode it
        enc = enc.decode("base64")
    else:
        # Not valid, so let's brute force the caesar shift used and check each shift
        for y in range(1,len(alphabet)):
            if is_valid_base64(caesar(enc, y)):
                enc = caesar(enc, y)
                print "Decrypted with a shift of %s" % y
                break

print enc

# Looking at encrypt.py, its clear that we need to do some brute forcing,
# since RNG decides how and when to encrypt the flag.
# Running this script will yield the flag.

# sctf{thank_you_based_64}
