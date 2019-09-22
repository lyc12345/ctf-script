from pwn import *


#r = remote("127.0.0.1",8888)
r = remote("secure-hash2.ctf.hackover.de",1337)

lines = [ line.strip() for line in open('zz').readlines()]

for i in xrange(1001):
  r.sendline("1")
  r.sendline("a")
  r.sendline(lines[i])

r.recvrepeat(3)

r.interactive()
