import gmpy
import sys
# p = a+r q= a-r
# complexity = O(r/sqrt(a))

def close_factor(n, b):
    # approximate phi
    phi_approx = n - 2 * gmpy.sqrt(n) + 1
    # create a look-up table
    look_up = {}
    z = 1
    for i in range(0, b + 1):
        look_up[z] = i
        z = (z * 2) % n
    # check the table
    mu = gmpy.invert(pow(2, phi_approx, n), n)
    fac = pow(2, b, n)
    j = 0
    while True:
        mu = (mu * fac) % n
        j += b
        if mu in look_up:
            phi = phi_approx + (look_up[mu] - j)
            break
        if j > b * b:
            return
    m = n - phi + 1
    roots = (m - gmpy.sqrt(m ** 2 - 4 * n)) / 2, \
            (m + gmpy.sqrt(m ** 2 - 4 * n)) / 2
    return roots
 
n = int(sys.argv[1])
b = 100000
 
print close_factor(n, b)
