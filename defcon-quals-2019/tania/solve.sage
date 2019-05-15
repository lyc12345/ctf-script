p = 834233754607844004570804297965577358375283559517
Zmodp = Zmod(p)

h = 793725469310789348222479757421998121556400233934 
data = open('data').read()
exec 'data = '+ data
t = []
u = []
for d in data:
    r,s = d
    r = Zmodp(r)
    s = Zmodp(s)
    invs = s^-1
    t.append(int(r*invs))
    u.append(int(h*invs))

l = 60
d = len(data)
m = []
bound = 2**100
for i in range(d):
    tmp = [0] * (d+2)
    tmp[i] = p
    m.append(tmp)
m.append(t+[1/(2**(l+1)), 0])
m.append(u+[0, bound])
ma = matrix(QQ, m)
print 'Ready to LLL...'
mb = ma.LLL()
x = mb[1][-2] * (2**(l+1))
print x

ok = True
for i in xrange(40):
	a = (x*t[i]+u[i])%p
	if a > bound: ok = False
if ok:
  print "Successful"
else:
  print "Failed"
