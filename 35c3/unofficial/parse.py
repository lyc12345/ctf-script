import os

names = os.listdir('data')
ports = []
for name in names:
  p = name.split('.')[-1]
  if int(p) != 1337:
    ports.append(int(p))

prefix = '192.168.002.100.01337-192.168.002.100.'
pattern = '192.168.002.100.{}-192.168.002.100.01337'
v = []
m = []
for port in ports:
  if 'ACCESS GRANTED' not in open('data/'+prefix+str(port)).read():
    continue
  out = open('data/'+prefix+str(port)).readline().strip().split()
  res = map(int,out)
  out = open('data/'+pattern.format(str(port))).readline().strip()
  v.append(int(out))
  #res.append(out)
  m.append(res)

print m
print v
