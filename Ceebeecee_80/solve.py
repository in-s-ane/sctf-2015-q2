enc = open("flag.enc", "rb").read()
enc = [ord(x) for x in enc]

i = len(enc)-1
while i > 0:
    enc[i] = enc[i-1] ^ enc[i]
    i -= 1

print "".join([chr(x) for x in enc])

#flag{r3a11y_scr3wed_up_cbc_d1dnt_i}
