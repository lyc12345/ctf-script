from pwn import *
from sympy import *

# SCTF{LCG_is_too_simple_to_be_a_good_CSPRNG}

r = remote('lcg.eatpwnnosleep.com', 12345)
a = []
for _ in xrange(10):
  r.sendline("1")
  a.append(int(r.recvline()))

b = []
for i in xrange(len(a)-1):
  b.append(a[i+1]-a[i])

c = []
for i in xrange(1,len(b)-2):
  c.append(b[i]*b[i]-b[i+1]*b[i-1])

d = []
for i in xrange(1,len(c)-2):
  v = c[i]*c[i]-c[i-1]*c[i+1]
  d.append(v)

m = gcd(d)
print m
print c[0]
y = (-c[1]*invert(c[0],m))%m
print y
x = ((b[2]-b[0]*y)*invert(b[1],m))%m
print x
z = (a[2]-a[1]*x-a[0]*y)%m
print z

n0,n1 = a[-2],a[-1]
for i in xrange(20):
  n2 = (n1*x+n0*y+z)%m
  r.sendline(str(n2))
  n0,n1 = n1,n2
  if i<6 :
    print n2
    print r.recvline()

r.interactive()
