p = 21652247421304131782679331804390761485569
data = open('output').readlines()
exec 'v = '+ data[0].strip()
exec 'm = '+ data[1].strip()

N= 40
def rand():
    return int(os.urandom(16).encode('hex'),16)

def keygen():
    return [rand() for _ in range(N)]

key = keygen()

Zmodp = Zmod(p)

m.append([1]+[0]*39)
M = matrix(Zmodp, m)
invM = M.inverse()

t = []
u = []

for i in xrange(40):
  mm = invM[i]
  val = sum([ x*y for x,y in zip(mm[:39],v)])
  val = int(val)
  u.append(int(val))
  t.append(int(mm[-1]))

l = 5
d = 40
m = []
bound = p / (2 ** (l+1))
bound = 2**128
for i in range(d):
    tmp = [0] * (d+2)
    tmp[i] = p
    m.append(tmp)
m.append(t+[1/(2**(l+1)), 0])
m.append(u+[0, bound])
ma = matrix(QQ, m)
print 'Ready to LLL...'
mb = ma.LLL()
print mb
flag_num = mb[1][-2] * (2**(l+1))
print flag_num

for i in xrange(40):
	a = (flag_num*t[i]+u[i])%p
	print i,a<bound 

keys = []
for i in xrange(40):
	a = (flag_num*t[i]+u[i])%p
	keys.append(a)
print keys
