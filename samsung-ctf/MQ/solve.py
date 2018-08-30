from pwn import *
from sympy import *

r = remote('mq.eatpwnnosleep.com',12345)

mq = r.recvline().strip().split('+')
matrix = [[0 for _ in xrange(32)] for _ in xrange(32)]
uni = [0 for _ in xrange(32)]
c = 0
p = 131

for term in mq:
  cnt = term.count('x')
  if cnt == 2:
    st = term.split('x')
    val,i,j = int(st[0]), int(st[1])-1, int(st[2])-1
    matrix[i][j] = matrix[j][i] = val
  elif cnt == 1:
    st = term.split('x')
    val,i = int(st[0]), int(st[1])-1
    uni[i] = val
  else:
    c = int(term)

r.send('\x00'*32)
zero = int(r.recvline().strip()[2:],16)

value = []
for i in xrange(32):
  data = '\x00'*i + '\x01' + '\x00'*(31-i)
  r.send(data)
  value.append(int(r.recvline().strip()[2:],16))

for i in xrange(32):
  value[i] = (value[i] - zero - uni[i] - matrix[i][i])%p
  matrix[i][i] = (2*matrix[i][i])%p

print value
print matrix
r.close()
