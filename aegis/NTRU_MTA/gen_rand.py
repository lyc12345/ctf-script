
lines = open('out').readlines()
cipher = []
ans = [0]*167
for line in lines:
    coe = line.strip()[1:-1].split(',')
    coe = map(int, coe)
    for i in xrange(167):
        if coe[i] == 2: ans[i] = 1
        elif coe[i] == 126: ans[i] = 127
print ans
print ans.count(1)
print ans.count(127)



for line in lines:
    out = [0]*167
    coe = line.strip()[1:-1].split(',')
    coe = map(int, coe)
    for i in xrange(167):
        out[i] = (coe[i]-ans[i])%128
    print out
    print out.count(1)
    print out.count(127)
    print '==================='
