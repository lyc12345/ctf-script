
now = [0]*5

maybe = []
maybe.append((now,[]))

def expand(maybe,candi):
  a = []
  for m in maybe:
    for c in candi:
      x = map(sum,zip(m[0],c))
      a.append((x,m[1]+[candi.index(c)]))
  return a

print maybe
maybe = expand(maybe,[(2,0,0,1,0),(2,0,1,0,0),(2,0,2,1,0)])
maybe = expand(maybe,[(0,0,1,0,2),(0,-1,0,0,-1),(0,2,0,0,0)])
print maybe
maybe = expand(maybe,[(-1,0,-1,1,0),(1,1,0,0,0),(1,2,0,0,0)])
maybe = expand(maybe,[(1,1,1,2,0),(1,1,1,1,2),(1,2,2,1,2)])
print maybe
maybe = expand(maybe,[(0,0,1,1,0),(0,-1,2,0,0),(0,-1,1,1,0)])
maybe = expand(maybe,[(1,-1,-1,2,2),(0,0,0,0,0),(1,0,0,0,1)])
print maybe
maybe = expand(maybe,[(0,1,1,2,0)])
maybe = expand(maybe,[(0,1,1,1,0),(0,1,0,0,0)])
print maybe
maybe = expand(maybe,[(-1,0,0,1,1),(0,0,1,2,1),(0,0,0,2,2)])

for m in maybe:
  if m[0] == [5,5,5,5,5]:
    print m
