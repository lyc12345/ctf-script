from gmpy2 import next_prime, powmod
from random import randint, getrandbits
from libnum import *


def pad(num, length):
	result = bin(num).lstrip('0b').strip('L')
	result = result + '0' * (length - len(result))
	return int(result, 2)

kk = -1
qq = -1
pp = -1
R = -1
def gen_key():
  global kk,qq,pp,R
  t1 = randint(768, 928)
  t2 = 1024 - t1
  if t1 > t2:
      t1, t2 = t2, t1
  assert t1 < t2
  p2 = pad(getrandbits(1024 - t2) << t2, 1024)
  p0 = pad(getrandbits(t1), t1)
  q2 = pad(getrandbits(1024 - t2) << t2, 1024)
  q0 = pad(getrandbits(t1), t1)
  r = pad(getrandbits(t2 - t1) << t1, t2)
  p = next_prime((p2 ^ r ^ p0))
  q = next_prime((q2 ^ r ^ q0))
  #p = (p2 ^ r ^ p0)
  #q = (q2 ^ r ^ q0)
  N = p * q
  mod = 1<<t1

  print 't1='+str(t1)
  print 't2='+str(t2)
  print 'p0='+str(p0)
  print 'q0='+str(q0)
  print 'r=' +str(r)
  print 'p2='+str(p2)
  print 'q2='+str(q2)
  print 'p='+str(p)
  print 'q='+str(q)

  qq = q%mod
  pp = p%mod
  kk = (p-q)%mod
  print p%mod
  print q%mod
  R = r
  return N, t2 - t1, p0 - q0
  
n,gamma,delta = gen_key()
print '=============================='

t2 = (1024+gamma)/2
t1 = 1024-t2
mod1 = 1<<t1
mod2 = 1<<t2

tmp = n%mod1
tmp2 = n%mod2
delta = delta%mod1

cnt = 0

f = open('data','wb')
f.write(str(n)+'\n')
f.write(str(t1)+'\n')
f.write(str(t2)+'\n')
for td in range(delta-500, delta+500):
  try:
    d = td%mod1
    if d == kk: print 'yes1'
    b = (d*d+4*tmp)%mod1
    sqrt = list(sqrtmod_prime_power(b,2,t1))
    cq = [ ((-d-v)/2)%mod1 for v in sqrt] + [ ((-d+v)/2)%mod1 for v in sqrt]
    cq = filter( lambda x: ((x+td)*x)%mod1 == tmp,cq)
    cp = [(q+td)%mod1 for q in cq] 
    for p0,q0 in zip(cp,cq):
      b,c = (p0+q0)%mod2, (p0*q0-tmp2)%mod2
      sqrt2 = list(sqrtmod_prime_power(b*b-4*c,2,t2))
      cr = [ ((-b-v)/2)%mod2 for v in sqrt2] + [ ((-b+v)/2)%mod2 for v in sqrt2]
      cr = filter( lambda x: ((x+p0)*(x+q0))%mod2 == tmp2,cr)
      for r in cr:
        f.write(str(p0)+" "+str(q0)+" "+str(r)+"\n")
        if p0 == pp and q0 == qq and r == R:
          print 'yes'
        cnt += 1
  except:
    pass
print cnt
f.close() 
      

  


