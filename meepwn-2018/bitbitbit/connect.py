from pwn import *
from hashlib import sha256
r = remote('206.189.92.209',54321)

raw = r.recvline().strip().split()[-1].decode('hex')
c = 0
while True:
  challenge = str(c)
  temp = sha256(raw + challenge).hexdigest()
  if temp.startswith('25455'):
    print temp,challenge
    r.sendline(challenge)
    break
  c += 1

r.interactive()
