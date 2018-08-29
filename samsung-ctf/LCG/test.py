import signal
import random


class LCG:
    def __init__(self, s, k):
        self.init_state = s

        k1, k2, k3 = k
        self.x = (k1 - 0xdeadbeef) % k3
        self.y = (k1 * 0xdeadbeef) % k3
        self.z = k2
        self.m = k3

    def __iter__(self):
        self.index = 0
        self.size = 32
        self.s0, self.s1 = self.init_state
        return self

    def __next__(self):
        if self.index >= self.size:
            raise StopIteration

        self.index += 1
        s0, s1 = self.s0, self.s1
        print(s0)
        print(s1)
        print((self.x * s1 + self.y * s0 + self.z) % self.m)
        self.s0, self.s1 = s1, (self.x * s1 + self.y * s0 + self.z) % self.m
        return self.s1


if __name__ == '__main__':
    #signal.alarm(60)

    s0, s1, k1, k2, k3 = [random.getrandbits(64) for i in range(5)]

    s = (s0, s1)
    k = (k1, k2, k3)
    s = (3885052174422946021, 7009760270621768804)
    k = (13960868133915151465, 15960649579003996051, 14854620408071017297)
    print(s)
    print(k)

    cnt = 16
    a = []
    for i, v in enumerate(LCG(s, k)):
        a.append(v)
    print(a[:16])

    if cnt >= 16:
        with open('flag.txt', 'r') as f:
            print(f.read())

