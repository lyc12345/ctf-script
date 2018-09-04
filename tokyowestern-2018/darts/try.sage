lines = open('data').readlines()
dic = {}
idx = 0
for i in xrange(100):
  a = int(lines[idx].strip())
  b = map(int,lines[idx+1].split(','))
  dic[a] = b
  idx += 2


P2.<x> = GF(2)[];
p = x^8 + x^4 + x^3 + x + 1;
GF256 = GF(2^8, 'x', modulus=p)

def trans(v):
    v = bin(v)[2:][::-1]
    now = 0
    res = 0
    for c in v:
        if c == '1': res += x^now
        now += 1
    return res

mp = []
for i in range(256): mp.append(trans(i))


def lookup(s):
  for i in xrange(256):
    if str(mp[i]) == str(s):
      return i
  return ''


flag = []
for c in xrange(71):
  mat = []
  vals = []
  for a in dic:
    aa = mp[a]
    res = dic[a][c]
    tmp = [ (aa^i)%p for i in range(99,-1,-1)]
    mat.append(tmp)
    vals.append((mp[res]-(aa^100%p))%p)
    
  m = Matrix(GF256,mat)
  ans = m.solve_right(vector(vals))
  print ans[-1]
  flag.append(lookup(ans[-1]))
  print flag
  #break
print flag
