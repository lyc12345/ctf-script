f = [line.strip() for line in open('data').readlines()]
n = int(f[0])
t1 = int(f[1])
t2 = int(f[2])
f = f[3:]
A = 1<<t2
solve = False
cnt = 0
for line in f:
  cnt += 1
  if cnt%10 == 0: print cnt
  p0, q0, r = map(int,line.split())
  F.<x> = PolynomialRing(Zmod(n), implementation='NTL')
  B = r+p0
  f = A*x+B
  f = f.monic()
  roots = f.small_roots(X=2**t1, beta=0.3)
  for root in roots:
    p = int(A*root+B)
    if n%p == 0: 
      print p 
      solve = True
      break
  if solve: break
