
# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_32 = Integer(32); _sage_const_131 = Integer(131); _sage_const_4 = Integer(4)
n = _sage_const_32 
p = _sage_const_131 
Zmodp = Zmod(p)


data = open('data').readlines()
exec 'v = '+ data[_sage_const_3 ].strip()
exec 'm = '+ data[_sage_const_4 ].strip()

M = matrix(Zmodp, m)
V = vector(Zmodp,v)
invM = M.inverse()
out = list(invM * V)
print ''.join(map(chr,out))

