import networkx as nx
from pwn import *

def print_matrix(matrix):
  for i in xrange(7):
    s = ''
    for j in xrange(7): 
      s += '%5d ' % matrix[i][j]
    print s

def solve(matrix):
  G = nx.DiGraph()
  for i in xrange(7):
    G.add_edge(49, 7*i, distance = matrix[i][0])
  for i in xrange(7):
    G.add_edge(7*i+6, 50, distance = 0)
  for i in xrange(7):
    for j in xrange(7):
      if j != 6:
        G.add_edge(7*i+j  ,7*i+j+1, distance = matrix[i][j+1])
        G.add_edge(7*i+j+1,7*i+j  , distance = matrix[i][j])
      if i != 6:
        G.add_edge(7*i+j  ,7*i+j+7, distance = matrix[i+1][j])
        G.add_edge(7*i+j+7,7*i+j  , distance = matrix[i][j]) 
  #return nx.dijkstra_path(G, 49, 50, 'distance')
  return nx.dijkstra_path_length(G, 49, 50, 'distance')

r = remote('110.10.147.104',15712)
r.sendline('G')

flag = ''
for i in xrange(100):
  print r.recvuntil('*** STAGE ')+r.recvline()
  matrix = []
  for i in xrange(7):
    d = r.recvline().strip().split()
    matrix.append(map(int,d))
  ans = solve(matrix)
  print_matrix(matrix)
  r.sendline(str(ans))
  print ans
  flag += chr(ans)
  print flag
r.interactive()
