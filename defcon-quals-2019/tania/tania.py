from pwn import *

data = []
for i in xrange(50):
    r = remote("tania.quals2019.oooverflow.io",5000)
    cmd = "the rules are the rules, no complaints"
    r.sendline("S")
    r.sendline(cmd)
    r.recvuntil("r: ")
    dr = int(r.recvline().strip())
    r.recvuntil("s: ")
    ds = int(r.recvline().strip())
    data.append((dr,ds))

print data
open("data","w").write(str(data))
