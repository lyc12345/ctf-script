n = 32
p = 131
Zmodp = Zmod(p)


data = open('data').readlines()
exec 'v = '+ data[3].strip()
exec 'm = '+ data[4].strip()

M = matrix(Zmodp, m)
V = vector(Zmodp,v)
invM = M.inverse()
out = list(invM * V)
print ''.join(map(chr,out))

#SCTF{Try_MQ_be_happy!}
