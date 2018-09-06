
def calc(a):
  b = []
  v = 0
  one = False
  for i in a:
    #if '401faf' in i or '401fc4' in i: 
    if '401f97' in i: 
      assert not one 
      one = True
    elif '401fdf' in i:
      v = v*2
      if one: 
        b.append(1)
        v = v+1
        #v = v+1
      else: 
        b.append(0)
      one = False

  b = b[::-1]
  v = 0
  for i in b:
    if i == 1: v += 1
    v *=2

  return v/2

a = open('parse.log').readlines()
print calc(a)
