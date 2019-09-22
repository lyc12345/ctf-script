from pwn import *
from hashlib import *
import os

r = remote('206.189.32.108',13579)

prefix = r.recvline().strip().split()[-1].decode('hex')
r.recvuntil('> ')
while True:
  data = os.urandom(10).encode('hex')
  tmp = sha256(prefix + data).hexdigest()
  if tmp.startswith('00000'):
    r.sendline(data)
    break

r.recvuntil('> ')
r.sendline('3')
enc_flag = r.recvline().strip()
print enc_flag
f = open('data','wb')
f.write(prefix+'\n')
f.write(enc_flag+'\n')

for _ in range(255):
  r.recvuntil('> ')
  r.sendline('1')
  r.recvuntil("give me a string: ")
  r.sendline(str(_))
  data = r.recvline().strip()
  print _,data
  f.write(data+'\n')

f.close()
