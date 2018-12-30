from BitVector import BitVector
from challenge import *
from random import SystemRandom
from os import urandom



if __name__ == "__main__":
    key = BitVector(size=48,intVal=13276381*(2**24)+12041912)
    cipher = CodeBasedEncryptionScheme(key)
    print(cipher.key)
    s = b""
    for i in range(31):
      b = open("data/flag_%02d" % i,"rb").read()
      s += cipher.decrypt(b)
    print(s)
