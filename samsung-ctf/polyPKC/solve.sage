data = [ s.strip().split(':')[-1] for s in open('enc').readlines()]
exec 'order = ' + data[0]
exec 'key = ' + data[1]
exec 'N = ' + data[2]
exec 'result =' + data[3]

Zn = Zmod(N)
PR.<x> = PolynomialRing(Zn)

eq1 = x^order-1
eq2 = 0
for i in xrange(len(key)):
  eq2 += key[i]*x^i

while eq2 != 0:
  r = eq1 % eq2
  eq1,eq2 = eq2, r

eq = eq1.monic()
t = Integer(N - eq.coefficients()[0])

ans = 0 
for i in xrange(len(result)):
  ans = (ans + result[i]*t^i)%N

print hex(ans).decode('hex')
# SCTF{B4S1C_ARITHMET1C_WITH_P0LYNOM14L}
