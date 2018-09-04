from pwn import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.number import *
from libnum import *
from sympy import *
from mt import untemper

r = remote('crypto.chal.ctf.westerns.tokyo', 5643)
#r = remote('127.0.0.1', 8888)

e = 65537

# ==============================
#
# get N
#
# ==============================

r.sendline('1')
r.sendlineafter('input plain text: ','\x02')
d1 = r.recvline().strip().split()[-1]
d1 = int(d1,16)
r.sendline('1')
r.sendlineafter('input plain text: ','\x03')
d2 = r.recvline().strip().split()[-1]
d2 = int(d2,16)
r.sendline('1')
r.sendlineafter('input plain text: ','\x04')
d3 = r.recvline().strip().split()[-1]
d3 = int(d3,16)
n = gcd(2**e-d1,3**e-d2)
n = gcd(4**e-d3,n)
n = int(n)
print n
while n%2 == 0: n = n/2
print n
# ==============================
#
# recover AES key
#
# ==============================
e2 = pow(2,e,n)

r.sendline('4')
r.recvuntil('here is encrypted key :)\n')
enc = int(r.recvline().strip(), 16)

val = enc
for i in xrange(1024):
	val = (val*e2)%n
	sleep(0.01)
	r.sendline('2')
	r.sendline(n2s(val).encode('hex'))

res = []
while len(res) != 1024:
	print len(res)
	response = r.recvrepeat(1)#.split('\n')
	response = response.split('\n')
	for line in response:
		if 'RSA' in line:
			resp = line.strip().split()[-1].decode('hex')
			if ord(resp[-1])%2 == 1: res.append(1)
			else: res.append(0)

UP,LOW = n,0
for i in range(1024):
  if res[i] == 0: UP = (UP + LOW)/2
  else: LOW = (UP + LOW)/2

print repr(n2s(UP))
key_prefix = n2s(UP)[:-1]

def pad(s):
    n = 16 - len(s)%16
    return s + chr(n)*n

plain = 'test12345'
r.sendline('1')
r.sendlineafter('input plain text: ', plain)
r.recvline()
res = r.recvline().strip().split()[-1].decode('hex')
iv = res[:16]
res = res[16:]


for i in xrange(256):
	key = key_prefix+chr(i)
	aes = AES.new(key, AES.MODE_CBC, iv)
	out = aes.encrypt(pad(plain))
	if out == res:
		print repr(key)
		break

# ==============================
#
# recover AES iv
#
# ==============================

values = []

for i in xrange(156):
	r.sendline('1')
	r.sendlineafter('input plain text: ', plain)
	r.recvline()
	res = r.recvline().strip().split()[-1].decode('hex')
	iv = res[:16]
	num = bytes_to_long(iv)
	for _ in xrange(4):
		values.append(num&0xffffffff)
		num = num >> 32

#print len(values)

mt_state = tuple(map(untemper, values[:624]) + [0])
random.setstate((3, mt_state, None))
for i in xrange(156): 
	print random.getrandbits(128)
#raw_input('@@')

iv = long_to_bytes(random.getrandbits(128),16)

r.sendline('3')
r.recvuntil('another bulldozer is coming!\n')
flag = r.recvline().strip().decode('hex')

def unpad(s):
    n = ord(s[-1])
    return s[:-n]

def aes_decrypt(aeskey,s,iv):
    aes = AES.new(aeskey, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(s[16:]))

print repr(aes_decrypt(key,flag,iv))

r.sendline('55')
r.close()
