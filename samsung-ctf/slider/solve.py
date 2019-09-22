from Crypto.Cipher import AES
from os import urandom
from pwn import xor

aeskey = ''.join(map(chr,range(16)))
bxor = xor

def crypt(m, k):
    if len(m) != 4:
        return None

    l, r = m[0:2], m[2:4]

    P = AES.new(aeskey, AES.MODE_ECB).encrypt
    def f(x):
        return P(x + '\x00'*14)[:2]

    #keys = k*4
    #for rkey in keys:
    l, r = r, bxor(l, f(bxor(r, k)))

    return r + l
"""
def encrypt(self, m):
    k = (self.k0, self.k1, self.k0, self.k2)
    return self._crypt(m, k)

def decrypt(self, m):
    k = (self.k2, self.k0, self.k1, self.k0)
    return self._crypt(m, k)
"""

k = '\xaa\xbb'
m = '\x00\x00\x00\x00'

print repr(crypt(m,k))
