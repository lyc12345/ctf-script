from pwn import *
context.arch = 'amd64'

binary = open('king','rb').read()
idx = [0x341d,0x2d55,0x20e2,0x1b0a,0x11bb]
key = ['lOv3','D0l1','HuNgRYT1m3','F0uRS3aS0n','T1kT4kT0Kk']
size = [0xf0,0xfa,0x18b,0xf0,0x131]

for i in xrange(5):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  #aa = disasm(data1)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]


#'========================================================================================================='


idx = [0x330f,0x33ff,0x32c0,0x32de,0x3197,0x30d4]
key = ['lOv3']*6
size = [0xf0,0x1e,0x1e,0x31,0x129,0xc3]

for i in xrange(len(idx)):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]

#'========================================================================================================='

idx = [0x2c25,0x2d37,0x27e9,0x29b9,0x2b2b,0x271c,0x28b5,0x299b,0x2aed,0x2a9f,0x2871,0x282d]
key = ['D0l1']*len(idx)
size = [0x112,0x1e,0x44,0xe6,0xfa,0xcd,0xe6,0x1e,0x3e,0x4e,0x44,0x44]

for i in xrange(len(idx)):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]
print map(hex,idx)

#'========================================================================================================='

idx = [0x201f]
key = ['HuNgRYT1m3']*len(idx)
size = [0xc3]

for i in xrange(len(idx)):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]
print map(hex,idx)
#'========================================================================================================='
idx = [0x19f2,0x1aec,0x192c,0x19d4,0x16d0]
key = ['F0uRS3aS0n']*len(idx)
size = [0xfa,0x1e,0xa8,0x1e,0xc3]

for i in xrange(len(idx)):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]
print map(hex,idx)
#'========================================================================================================='

idx = [0xf25,0x108b,0x1001,0x101f,0x106d,0xde7,0xf07,0xc8c]
key = ['T1kT4kT0Kk']*len(idx)
size = [0xdc,0x130,0x1e,0x4e,0x1e,0x120,0x1e,0x158]

for i in xrange(len(idx)):
  data = binary[idx[i]:idx[i]+size[i]]
  kk = key[i]
  m = len(data)/len(kk)
  k = (kk*(m+1))[:len(data)]
  data1 = xor(data,k)
  binary = binary[:idx[i]]+data1+binary[idx[i]+size[i]:]
print map(hex,idx)
open('modify','wb').write(binary)
