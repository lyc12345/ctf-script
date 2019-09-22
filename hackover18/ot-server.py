#!/usr/bin/env python3

import os
import sys
from gmpy2 import powmod
from phe import paillier  # pip install phe


def ot_server(m0, m1):

    n = int(sys.stdin.readline().strip())
    pk = paillier.PaillierPublicKey(n)
    c = int(sys.stdin.readline().strip())

    r0 = pk.get_random_lt_n()
    r1 = pk.get_random_lt_n()
    r1 = 243177556574988839779497363265289180068663982359533559639352108292302112523373762773459610438065730375862587787366975039374570630208358261735093850550722
    sys.stderr.write(str(r0)+"\n")
    sys.stderr.write(str(r1)+"\n")
    x0 = int.from_bytes(m0, 'big')
    x1 = int.from_bytes(m1, 'big')
    sys.stderr.write(str(x0)+"\n")
    sys.stderr.write(str(x1)+"\n")

    c0 = powmod(pk.raw_encrypt(1) * powmod(c, (pk.n-1), pk.nsquare), x0, pk.nsquare) * powmod(c, r0, pk.nsquare)
    c1 = powmod(c, x1, pk.nsquare) * powmod(pk.raw_encrypt(1) * powmod(c, (pk.n-1), pk.nsquare), r1, pk.nsquare)
    sys.stdout.write('{}\n'.format(c0))
    sys.stdout.write('{}\n'.format(c1))


def main():
    with open('flag.txt', 'rb') as f:
        flag = f.readline().strip()
    m1 = os.urandom(len(flag))
    m2 = bytes(x ^ y for x, y in zip(flag, m1))
    m1 = bytes(b"a"*20)
    m2 = bytes(b"b"*20)
    ot_server(m1, m2)


if __name__ == '__main__':
    main()
