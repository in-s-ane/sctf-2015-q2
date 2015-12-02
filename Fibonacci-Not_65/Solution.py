# Given F(x) = G(x) - W(x)
# G(x) = [G(x-1)+G(x-2)]^2
# W(x) = [W(x-1)]^2 + [W(x-2)]^2

# G(0) = 0, G(1) = 1
# W(0) = 0, W(1) = 1

# Find the sum of the digits in F(30)

G = [0, 1]
W = [0, 1]

# Generates G up to the ith term
def gen_g(i):
    while len(G) <= i:
        G.append((G[len(G) - 2] + G[len(G) - 1]) ** 2)

# Generates W up to the ith term
def gen_w(i):
    while len(W) <= i:
        W.append((W[len(W) - 2]) ** 2 + (W[len(W) - 1]) ** 2)

def sum_of_digits_of_2_nums(g, w):
    sum = 0
    carried = 0
    while g > 0 or w > 0:
        # print("G: " + str(g))
        # print("W: " + str(w))
        to_add = (g % 10) + (w % 10) + carried
        g = g / 10
        w = w / 10
        if to_add > 9:
            carried = to_add / 10
        else:
            carried = 0
        # print("Carried sum: " + str(carried))
        # print("Added: " + str(to_add % 10))
        sum += to_add % 10
    sum += carried
    print sum

# Finds the sum of the digits in the ith term of F
def sum_of_digits(i):
    gen_g(i)
    gen_w(i)
    sum_of_digits_of_2_nums(G[i], W[i])

sum_of_digits(20)

