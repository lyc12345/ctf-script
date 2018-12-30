
from challenge import CodeBasedEncryptionScheme

from random import SystemRandom
from os import urandom



if __name__ == "__main__":
    cipher = CodeBasedEncryptionScheme.new()
    print(cipher.key)
    random = SystemRandom()
    for i in range(1):
        pt = urandom(2)
        ct = cipher.encrypt(pt)
        with open("plaintext_{:03d}".format(i), "wb") as f:
            f.write(pt)
        with open("ciphertext_{:03d}".format(i), "wb") as f:
            f.write(ct)
        assert(pt == cipher.decrypt(ct))
